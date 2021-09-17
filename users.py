import os,sys,hashlib

class user:
    def __init__(self, username):
        if os.path.exists("db/users/" + username):
            with open("db/users/" + username) as f:
                data = f.read().split("\n")
            self.username = username
            self.display_name = data[0]
            self._password = data[1]
            self.type = data[2]
        else:
            print("No user: " + username)
            sys.exit(1)
    def __repr__(self):
        return "Username: " + self.username + "\nReal Name: " + self.display_name + "\nType: " + self.type 
    def validate(self, attempt):
        test = hashlib.sha1(attempt.encode()).hexdigest()
        if test == self._password:
            return True
        else:
            return False

class userdb:
    def __init__(self):
        if not os.path.exists("db/users/"):
            os.makedirs("db/users")
        self.users = []
    def populate_users(self):
        for username in os.listdir("db/users"):
            new = user(username)
            self.users.append(new)
    def list_all(self):
        for user in self.users:
            print(str(user)+"\n"+"-"*10)
    def retrieve(self,username):
        for user in self.users:
            if user.username == username:
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
            return user.type
        else:
            return "E"
    def register(self,username,displayname,password,type):
        if self.retrieve(username) == None:
            safe_pw = hashlib.sha1(password.encode()).hexdigest()
            with open("db/users/" + username, "w") as f:
                f.write(displayname + "\n" + safe_pw + "\n" + type)
            self.populate_users()
            return True
        else:
            return False
