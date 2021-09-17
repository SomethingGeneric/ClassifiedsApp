import os

from users import userdb

if os.path.exists("db"):
    os.system("rm -rf db/")

db = userdb()
db.register("matt", "Matt C", "mdc028@bucknell.edu", "FooBar", "admin")
db.list_all()
print(str(db.check("matt","Lmao")))
print(str(db.check("matt","FooBar")))