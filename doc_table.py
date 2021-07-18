import sqlite3

con = sqlite3.connect('hospital.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE docter
               (Doc_id text, doc_name text, dept text, fee real, days text, time text)''')

# Insert a row of data
cur.execute("INSERT INTO docter VALUES ('D001','Dr. Prakash','Cardio',1000,'T/T/S', '4-5 pm')")
cur.execute("INSERT INTO docter VALUES ('D002','Dr. Krishnamani','Neuro',2000,'M/S', '11-4 pm')")
cur.execute("INSERT INTO docter VALUES ('D003','Dr. Jonh','ENT',800,'T/T/S', '4-6 pm')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
