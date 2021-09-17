import os,sys,hashlib

class user:
    def __init__(self, username):
        if os.path.exists("db/users/" + username):
            with open("db/users/" + username) as f:
                data = f.read().split("\n")
            self._username = username
            self._display_name = data[0]
            self._email = data[1]
            self._password = data[2]
            self._type = data[3]
            self._unlocked = False
        else:
            print("No user: " + username)
            sys.exit(1)
    def __repr__(self):
        return "Username: " + self._username + "<br/>Real Name: " + self._display_name + "<br/>Email: " + self._email + "<br/>Type: " + self._type 
    def validate(self, attempt):
        test = hashlib.sha1(attempt.encode()).hexdigest()
        if test == self._password:
            self._unlocked = True
            return True
        else:
            return False
    def get_username(self):
        return self._username
    def get_type(self):
        return self._email
    def get_display_name(self):
        return self._display_name
    def edit(self, prop, val):
        if self._unlocked:
            self._unlocked = False
            if prop == "username":
                self._username = val
            elif prop == "display_name":
                self._display_name = val
            elif prop == "email":
                self._email = val
            elif prop == "password":
                self._password = str(hashlib.sha1(val.encode()).hexdigest())
            elif prop == "type":
                self._type = val
            return True
        else:
            return False

class userdb:
    def __init__(self):
        if not os.path.exists("db/users/"):
            os.makedirs("db/users")
        self.users = []
        self.populate_users()
    def populate_users(self):
        for username in os.listdir("db/users"):
            new = user(username)
            self.users.append(new)
    def list_all(self):
        total = ""
        for user in self.users:
            total += str(user)+"<br/>"+"-"*10+"<br/>"
        print(total)
        return total
    def retrieve(self,username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None
    def check(self,username,password):
        user = self.retrieve(username)
        if user != None:
            if user.validate(password):
                return True
        return False
    def typeof(self,username):
        user = self.retrieve(username)
        if user != None:
            return user.get_type()
        else:
            return "No user"
    def register(self,username,displayname,email,password,type):
        if self.retrieve(username) == None:
            safe_pw = hashlib.sha1(password.encode()).hexdigest()
            with open("db/users/" + username, "w") as f:
                f.write(displayname + "\n" + email + "\n" + safe_pw + "\n" + type)
            self.populate_users()
            return True
        else:
            return False
