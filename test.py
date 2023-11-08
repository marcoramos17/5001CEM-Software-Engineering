import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="AidenL",
    password="Lico2004*",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM test")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
