import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="descritores",
  passwd="12345678",
  database="referencias"
)

# print(mydb)
mycursor = mydb.cursor()

sql = "INSERT INTO fast_brief(Nome, Matches, Correto, ImgReferente) VALUES (%s, %s, %s, %s)"
# sql = "TRUNCATE orb"
val = ("este", 20, 10, "teste.jpg")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")