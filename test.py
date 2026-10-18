from datastore import Datastore

db = Datastore("TableTopGamers.db")

print(db.update_loan(0))