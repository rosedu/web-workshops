import os
import json
import re
import flask
import regconf

app_dir = os.path.dirname(__file__)
app = flask.Flask(__name__)
app.config.from_object(regconf)

@app.route("/")
def index():
    with open(app.config['TOPICS_FILE'], 'r') as topics:
        return flask.render_template('index.html', topics=topics.readlines())

@app.route("/signup", methods=['POST'])
def signup():
    form = flask.request.form

    if re.match(r'^\S+@\S+\.\S+$', form['email']) is None:
        return "Missing email address :("

    with open(app.config['SIGNUP_FILE'], 'ab') as f:
        json.dump(form.to_dict(), f)
        f.write('\n---\n')

    return "Thanks for signing up! We'll keep you posted ;)"

if __name__ == "__main__":
    app.run(debug=True)
