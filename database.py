import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="books"
)


#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE books")


'''mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE ketabkhane (name VARCHAR (120), ISBN VARCHAR (120), author VARCHAR  (120), translator VARCHAR (120), publisher VARCHAR (120), type VARCHAR (120) )")
mycursor = mydb.cursor()

sql = "INSERT INTO books (name, isbn,author,translator,publisher,type) VALUES (%s, %s,%s,%s,%s,%s)"
val = ("nabarde man","129356-672","Adolf Hitler","Fereshte","Negah press","Historical")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")'''



#mycursor = mydb.cursor()
#ql ="INSERT INTO ketabkhane (name,isbn,author,translator,publisher,type) VALUES (%s, %s, %s, %s, %s, %s)"
#val = ("nabardeman","129356-672","Adolf Hitler","Fereshte","Negah press","Historical")
#mycursor.execute(sql,val)
#mydb.commit()
#print(mycursor.rowcount,"record inserted.")