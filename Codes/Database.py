import MySQLdb

c = MySQLdb.connect(host='localhost', database='Python', user='root', password='root')

cursor = c.cursor()

try:
    cursor.execute("create table if not exists Student(Rollno varchar(10), Name varchar(50), Department varchar(50), CGPI float)")
    print("\nTable Created Successfully!\n")
    
    cursor.execute("insert into Student values(1011, 'ABC', 'INFT', 9.9)")
    print("Records Inserted Successfully!\n")

    cursor.execute("insert into Student values(1021, 'LMN', 'CMPN', 8.6)")
    print("Records Inserted Successfully!\n")

    cursor.execute("insert into Student values(1031, 'RST', 'EXTC', 6.4)")
    print("Records Inserted Successfully!\n")

    cursor.execute("insert into Student values(1041, 'XYZ', 'BIOM', 6.4)")
    print("Records Inserted Successfully!\n")

    cursor.execute("update Student set CGPI = 8.1 where Rollno = '1031'")
    print("Records Updated Successfully!\n")

    cursor.execute("delete from Student where Department = 'BIOM'")
    print("Records Deleted Successfully!\n")

    print("Contents of the table Student :")
    cursor.execute("select * from Student")
    
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    c.commit()

except:
    c.rollback()

cursor.close()
c.close()
