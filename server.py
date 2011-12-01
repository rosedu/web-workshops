import os
import json
import flask


app_dir = os.path.dirname(__file__)
app = flask.Flask(__name__)
app.config['SIGNUP_FILE'] = os.path.join(app_dir, 'signup.yaml')


@app.route("/")
def index():
    topics = [
        "Foo",
        "Bar",
    ]
    return flask.render_template('index.html', topics=topics)


@app.route("/signup", methods=['POST'])
def signup():
    with open(app.config['SIGNUP_FILE'], 'ab') as f:
        json.dump(flask.request.form.to_dict(), f)
        f.write('\n---\n')
    return "thank you"


if __name__ == "__main__":
    app.run(debug=True)
