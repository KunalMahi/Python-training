import sqlite3
class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect("Information2.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists admins(ID integer primary key autoincrement,name text,age int)")
        self._db.commit()

    def Add(self,Name,Age):
        self._db.row_factory = sqlite3.Row
        self._db.execute("insert into admins(name,age) values(?,?)",(Name,Age))
        self._db.commit()
        print("record is added")

    def ListAdmins(self):
        cursor=self._db.execute("Select * from admins")
        for row in cursor:
            print("ID:{},Name:{},Age:{},".format(row["ID"],row["Name"],row["Age"]))

    def Delete(self,ID):
        self._db.row_factory = sqlite3.Row
        self._db.execute("Delete from admins where ID={}".format(ID))
        self._db.commit()
        print("record is deleted")

    def Update(self,ID,Age):
        self._db.row_factory = sqlite3.Row
        self._db.execute("Update admins set Age=? where ID=?",(Age,ID))
        self._db.execute("Update admins set Age=? where ID=?",(Age,ID))
        self._db.commit()
        print("record is updated")

def main():
    dbconnect=DBConnect()
    while 1:
        IndexOp=int(input("Select operation:\n1-Add\n2-List admins\n3-Delete record\n4-Update Record\n0-Break"))
        if(IndexOp==1):
            Name=input("Enter the Name")
            Age=int(input("Enter the Age"))
            dbconnect.Add(Name,Age)
        elif(IndexOp==2):
            dbconnect.ListAdmins()
        elif(IndexOp==3):
            ID=input("Enter the ID of the record to be deleted:")
            dbconnect.Delete(ID)
        elif(IndexOp==4):
            ID=input("Enter the ID of the record to be updated:")
            Age=int(input("Enter the new Age:"))
            dbconnect.Update(ID,Age)
        elif(IndexOp==0):
            break;
if __name__ == '__main__':main()
