import sqlite3
import pandas as pd
connection = sqlite3.connect("INSTRUCTOR.db")   #make connection to database
cursorObj = connection.cursor()      #create cursor object
cursorObj.execute("DROP TABLE IF EXISTS INSTRUCTOR")   #drop a table if it exist

# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursorObj.execute(table)
print("Table is Ready")

#inserting into table
cursorObj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
cursorObj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

#fetch data
statement = '''SELECT * FROM INSTRUCTOR'''
cursorObj.execute(statement)
output_all = cursorObj.fetchall()

#print data
print("All the data")
for row_all in output_all:
  print(row_all)

#to fetch limited rows
statement = '''SELECT * FROM INSTRUCTOR'''
cursorObj.execute(statement)
output_many = cursorObj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

  # Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursorObj.execute(statement)
  
print("All the data")
output_column = cursorObj.fetchall()
for fetch in output_column:
  print(fetch)

  #updating
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursorObj.execute(query_update)
statement = '''SELECT * FROM INSTRUCTOR WHERE FNAME="Rav"'''
cursorObj.execute(statement)
output1 = cursorObj.fetchmany(1)
for row in output1:
  print(row)

#store data into dataframe
df = pd.read_sql_query("select * from instructor;", connection)
print(df.to_string(index=False))
#u can now do basic panda operation like finding no of row/column
print(df.shape)

# Close the connection
connection.close()