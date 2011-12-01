import os
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
        json.dump(form.to_dict(), f)
        f.write('\n---\n')

    return "thank you"


if __name__ == "__main__":
    app.run(debug=True)
