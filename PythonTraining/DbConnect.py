import sqlite3

def main():
    db=sqlite3.connect("Information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists admin(name text,age int)")
    db.commit()

if __name__ == '__main__':main()
