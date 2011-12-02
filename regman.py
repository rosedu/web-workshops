import os
import json
import re
import flask

# Config module
import regconf

app_dir = os.path.dirname(__file__)
app = flask.Flask(__name__)
app.config.from_object('regconf.InstructorConfig')

@app.route("/")
def index():
    config = app.config
    return flask.render_template('index.html', lines=config['LINES'],
                                 cols=config['COLS'],
                                 profiles=config['PROFILES'],
                                 contact=config['CONTACT'],
                                 followup=config['FOLLOWUP'])

@app.route("/signup", methods=['POST'])
def signup():
    form = flask.request.form

    # Why are we doing this twice?
    if re.match(r'^\S+@\S+\.\S+$', form['email']) is None:
        return "Missing email address :("

    with open(app.config['SIGNUP_FILE'], 'ab') as f:
        # Do NOT flatten!
        # All the checkboxes are named form-topic-{vreau,stiu} and flattening
        # would only keep the last preference"
        json.dump(form.to_dict(flat=False), f)
        f.write('\n---\n')

    return "Thanks for signing up! We'll keep you posted ;)"

# @app.route('/functions.js')
# def functions_js():
#     with open('functions.js', 'r') as js:
#         return js.read()

if __name__ == "__main__":
    app.run(debug=True)
