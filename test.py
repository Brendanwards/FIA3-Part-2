from datastore import Datastore

db = Datastore("TableTopGamers.db")

print(db.get_members())