import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='admin', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
conn.autocommit = True
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

sql = '''CREATE database mydb''';

#Preparing query to create a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()


