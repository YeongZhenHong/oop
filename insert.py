import mysql.connector

cnx = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()

first_name = input("Please input first name ")
last_name = input("Please input last name ")
course = input("Please input course ")
add_student = ("INSERT INTO trash_test.student " +
               "(first_name, last_name, course) " +
               "VALUES ('"+first_name+"', '"+last_name+"','"+course+"')")

# query = ("SELECT * FROM trash_test.student")
cursor.execute(add_student)

cnx.commit()
cursor.close()
cnx.close()
