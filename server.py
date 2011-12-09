import os
from datetime import datetime
import json
import re
import flask


app_dir = os.path.dirname(__file__)
app = flask.Flask(__name__)
app.config['SIGNUP_FILE'] = os.path.join(app_dir, 'signup.yaml')


@app.route("/")
def index():
    topics = [
        "HTML",
        "CSS",
        "JavaScript",
        "MVC",
        "Securitate",
        "REST",
        "Caching",
        "Scaling",
        "Deployment",
        "Analytics",
    ]
    return flask.render_template('index.html', topics=topics)


@app.route("/signup", methods=['POST'])
def signup():
    form = flask.request.form

    if re.match(r'^\S+@\S+\.\S+$', form['email']) is None:
        return "Missing email address :("

    with open(app.config['SIGNUP_FILE'], 'ab') as f:
        data = form.to_dict()
        data['topic-stiu'] = form.getlist('topic-stiu')
        data['topic-vreau'] = form.getlist('topic-vreau')
        data['time'] = datetime.utcnow().isoformat()
        json.dump(data, f)
        f.write('\n---\n')

    return flask.render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
