'''
Coded by Liani Aslam 2609807A
'''

import mysql.connector
import auth_token
import datetime
import pandas as pd

class BotAPI:

    '''
    Connections to mysql service
    '''

    cnx = mysql.connector.connect(user=auth_token.MYSQL_DBUSER,
                                  host=auth_token.MYSQL_HOST,
                                  database=auth_token.MYSQL_DBNAME,
                                  password=auth_token.MYSQL_PASSWD)
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
            self.cnx.commit()
            return True
        except:
            pass
    '''
    @selectAll() function to be changed to select all the data from within the database
    under the query table '''

    def selectAll(self):
        query = ("SELECT * FROM crawler.testing")
        self.cursor.execute(query)
        aList = []
        for i in self.cursor:
            aList.append(i)
        return aList

    # cursor.close()
    # cnx.close()

    def insertFromTwitter(self, author, content, date, likes, retweets, url):

        try:
            # add_tweets = ("INSERT INTO crawler.tweets " +
            #               "(author, content, date, likes, retweets, url)" +
            #               "VALUES ('"+author+"', '"+content+"', '"+date+"', '"+likes+"', '"+retweets+"', '"+url+"')")
            add_tweets = ("INSERT INTO crawler.testing " +
                          "(author, content, date, likes, retweets, url)" +
                          "VALUES ('"+author+"', '"+content+"', '"+date+"', '"+likes+"', '"+retweets+"', '"+url+"')")
            self.cursor.execute(add_tweets)
            self.cnx.commit()
            print("Insert successful!")
        except:
            print("Fail to insert into database!")
    def close(self):
        self.cnx.close()
        self.cursor.close()
    
    def readCsv(self):
        # a = open("tweets.csv","rb")
        df = pd.read_csv("tweets.csv",usecols=['content','author','date','retweets','likes','url'])
        # print(df)
        for index,row in df.iterrows():
            # print(type(str(row['url'])))
            self.insertFromTwitter(str(row['author']),str(row['content']),str(row['date']),str(row['likes']),str(row['retweets']),str(row['url']))
        

# a = BotAPI()
# a.readCsv()
# a.insertFromTwitter("hong","what","who")

