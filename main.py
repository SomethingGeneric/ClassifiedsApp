from flask import Flask,render_template,redirect,url_for,request

from users import userdb

app = Flask(__name__)

logindb = userdb()

@app.route("/")
def hello():
    return render_template("basic.html", title="Home", content="<p>Empty page :(</p>")

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template("basic.html", title="Register", content=render_template("register.html"))
    elif request.method == 'POST':
        un = request.form['username']
        dn = request.form['displayname']
        em = request.form['email']
        pw = request.form['password']
        result = logindb.register(un,dn,em,pw,"user")
        if result:
            return render_template("basic.html", title="Registration Complete", content="<p>You've been registered, " + dn + "</p>") 
        else:
            return render_template("basic.html", title="Registration Failed", content="<p>Failed to register new user: " + un + "</p>")
    else:
        return render_template("basic.html", title="Something went wrong", content="<p>How did we get here?</p>")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template("basic.html", title="Login", content=render_template("login.html"))
    elif request.method == 'POST':
        un = request.form['username']
        pw = request.form['password']
        result = logindb.check(un,pw)
        if result:
            return render_template("basic.html", title="Login Complete", content="<p>Correct password.</p>") 
        else:
            return render_template("basic.html", title="Login Failed", content="<p>Failed to authenticate user " + un + "</p>")
    else:
        return render_template("basic.html", title="Something went wrong", content="<p>How did we get here?</p>")

@app.route("/profiles")
def users():
    return render_template("basic.html", title="Our Users", content=logindb.list_all())

@app.route("/profile/<username>")
def profile(username):
    obj = logindb.retrieve(username)
    if obj != None:
        return render_template("basic.html", title=obj.get_display_name() + "'s Profile", content=str(obj))
    else:
       return render_template("basic.html", title="Something went wrong", content="<p>No user: " + username + "</p>") 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)