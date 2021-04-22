import sqlite3
class sql1:
    def __init__(self):
        self.db = sqlite3.connect("vacancy1.db")
        self.cursor = self.db.cursor()
    # get all data from db
    def fetchall(self,sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.db.commit()
        return results
    #get single data from database
    def fetchone(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result
    # create and delete and more edit
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
       # print("Edit success!")
        except:
            self.db.rollback()
            # print("Edit failed!")
    def close(self):
        self.cursor.close()
        # print("closed")
        self.db.close()