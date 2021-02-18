import mysql.connector

cnx = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()
print(cursor)
# query = ("SELECT * FROM trash_test.student")
# cursor.execute(query)
# for i in cursor:
#     print(i)

cursor.close()
cnx.close()