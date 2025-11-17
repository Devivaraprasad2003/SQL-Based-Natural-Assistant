# pip install db-sqlite3
# pip install sqlite3
import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("ipl_rcb_players2.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ipl_rcb_players2")

#create the table
#Our table name student
#Columns names are: name, course
table_inf="""
CREATE TABLE ipl_rcb_players2(players_name varchar(30),
                    players_role varchar(30),
                    players_age int,
                    players_salary float);
"""
cursor.execute(table_inf)

#Insert the records

cursor.execute('''Insert Into ipl_rcb_players2 values('Virat Kohli','Batsmen',38,1500000)''')
cursor.execute('''Insert Into ipl_rcb_players2 values('Phil Salt','Batsmen',27,1100000)''')
cursor.execute('''Insert Into ipl_rcb_players2 values('Devdut padikal','Batsmen',27,200000)''')
cursor.execute('''Insert Into ipl_rcb_players2 values('Krunal Pandya','Allrounder',33,500000)''')
cursor.execute('''Insert Into ipl_rcb_players2 values('Jacob Bethell','Allrounder',22,200000)''')
cursor.execute('''Insert Into ipl_rcb_players2 values('Bhuvneshwar Kumar','Bowler',33,1100000)''')
cursor.execute('''Insert into ipl_rcb_players2 values('Josh Hazelwood','Bowler','29',1200000)''')
cursor.execute('''Insert into ipl_rcb_players2 values('Romario Shepherd','Allrounder','31',250000)''')
cursor.execute('''Insert into ipl_rcb_players2 values('Jitesh Sharma','WK-Batsmen','26',1150000)''')
cursor.execute('''Insert into ipl_rcb_players2 values('Suyash Sharma','Bowler','24',400000)''')
cursor.execute('''Insert into ipl_rcb_players2 values('Liam Livingstone','Allrounder','33',800000)''')

#Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from ipl_rcb_players2''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()