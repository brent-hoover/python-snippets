import MySQLdb
# Create a connection object, then use it to create a cursor
con = MySQLdb.connect(host="127.0.0.1", port=3306, 
    user="joe", passwd="egf42", db="tst")
cursor = con.cursor()
# Execute an SQL string
sql = "SELECT * FROM Users"
cursor.execute(sql)
# Fetch all results from the cursor into a sequence and close the connection
results = cursor.fetchall()
con.close()
