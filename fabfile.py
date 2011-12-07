from StringIO import StringIO
from fabric.api import env
from fabric.api import local, run, cd, put
from fabric.contrib.files import exists


if env['host_string'] is None:
    env['host_string'] = 'webdev@rosedu.org'
    REMOTE_REPO = '/home/webdev/landing'


APP_WSGI_TMPL = """\
activate_this = '%(sandbox)s/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys; sys.path.append('%(repo)s')
from server import app as application
"""


def deploy():
    if not exists(REMOTE_REPO):
        run("git init '%s'" % REMOTE_REPO)

    git_remote = "%s:%s" % (env['host_string'], REMOTE_REPO)
    local("git push -f '%s' HEAD:incoming" % git_remote)
    with cd(REMOTE_REPO):
        run("git reset incoming --hard")

    sandbox = REMOTE_REPO + '/sandbox'
    if not exists(sandbox):
        run("virtualenv --no-site-packages '%s'" % sandbox)
        run("echo '*' > '%s/.gitignore'" % sandbox)

    with cd(REMOTE_REPO):
        run("sandbox/bin/pip install -r requirements.txt")

    app_wsgi = APP_WSGI_TMPL % {'sandbox': sandbox, 'repo': REMOTE_REPO}
    put(StringIO(app_wsgi), sandbox + '/app.wsgi')
