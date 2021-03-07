'''
Coded by Liani Aslam 2609807A
'''

import mysql.connector
import auth_token


class BotAPI:


    '''
    Connections to mysql service
    '''

    cnx = mysql.connector.connect(user=auth_token.MYSQL_DBUSER,
                                  host=auth_token.MYSQL_HOST,
                                  database=auth_token.MYSQL_DBNAME)
    cursor = cnx.cursor()
    '''
    @insertData(first_name,last_name,course)
    dummy insert statement into local database for student object
    the following insert statemetn would need to cater to data that
    is fetched from the twitter bot
    '''

    def insertData(self, first_name, last_name, course):

        # first_name = input("Please input first name ")
        # last_name = input("Please input last name ")
        # course = input("Please input course ")
        try:
            add_student = ("INSERT INTO test.student " +
                           "(first_name, last_name, course) " +
                           "VALUES ('"+first_name+"', '"+last_name+"','"+course+"')")

            self.cursor.execute(add_student)
            cnx.commit()
            return True
        except:
            pass
    '''
    @selectAll() function to be changed to select all the data from within the database
    under the query table '''

    def selectAll(self):
        query = ("SELECT * FROM test.student")
        self.cursor.execute(query)
        astr = ''
        for i in self.cursor:
            astr += str(i)
        return astr
    
    #cursor.close()
    #cnx.close()

       
    
