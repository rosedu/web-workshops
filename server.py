import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    topics = [
        "Foo",
        "Bar",
    ]
    return flask.render_template('index.html', topics=topics)


@app.route("/signup", methods=['POST'])
def signup():
    print flask.request.form
    return "thank you"


if __name__ == "__main__":
    app.run(debug=True)
