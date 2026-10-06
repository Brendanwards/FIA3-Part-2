import sqlite3
from datastore import datastore 

class Datastore:

    def __int__(self):
        self.connection = sqlite3.connect("TableTopGamers.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

        
