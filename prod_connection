# This is for connection to and updating PROD DB

import mysql.connector

# Define variables
host = "blank"
user = "blank"
password = "blank"
database = "blank"

# Establishing a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Creating a cursor object
cursor = connection.cursor()

# Test query
query = "SELECT * FROM your_table"

# Execute the query
cursor.execute(query)

# Fetching the results
results = cursor.fetchall()

# Printing the results
for row in results:
    print(row)

# Closing the cursor and connection
cursor.close()
connection.close()
