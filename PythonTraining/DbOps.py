import sqlite3
db = sqlite3.connect("Information2.db")

def CreateTable():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists admins(ID integer primary key autoincrement,name text,age int)")
    db.commit()

def Add(Name,Age):
    db.row_factory = sqlite3.Row
    db.execute("insert into admins(name,age) values(?,?)",(Name,Age))
    db.commit()
    print("record is added")

def ListAdmins():
    cursor=db.execute("Select * from admins")
    for row in cursor:
        print("ID:{},Name:{},Age:{},".format(row["ID"],row["Name"],row["Age"]))

def Delete(ID):
    db.row_factory = sqlite3.Row
    db.execute("Delete from admins where ID={}".format(ID))
    db.commit()
    print("record is deleted")

def Update(ID,Age):
    db.row_factory = sqlite3.Row
    db.execute("Update admins set Age=? where ID=?",(Age,ID))
    db.commit()
    print("record is updated")

def main():
    CreateTable()
    while 1:
        IndexOp=int(input("Select operation:\n1-Add\n2-List admins\n3-Delete record\n4-Update Record\n0-Break"))
        if(IndexOp==1):
            Name=input("Enter the Name")
            Age=int(input("Enter the Age"))
            Add(Name,Age)
        elif(IndexOp==2):
            ListAdmins()
        elif(IndexOp==3):
            ID=input("Enter the ID of the record to be deleted:")
            Delete(ID)
        elif(IndexOp==4):
            ID=input("Enter the ID of the record to be updated:")
            Age=int(input("Enter the new Age:"))
            Update(ID,Age)
        elif(IndexOp==0):
            break;
if __name__ == '__main__':main()
