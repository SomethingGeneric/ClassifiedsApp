from flask import Flask,render_template

from users import userdb

app = Flask(__name__)

logindb = userdb()

@app.route("/")
def hello():
    return render_template("basic.html", title="Home", content="<p>Empty page :(</p>")

@app.route("/register")
def register():
    return render_template("basic.html", title="Register", content="<p>Empty page :(</p>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)