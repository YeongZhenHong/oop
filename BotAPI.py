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
    @insertData(author, content, date, likes, retweets, url)
    dummy insert statement into local database for student object
    the following insert statemetn would need to cater to data that
    is fetched from the twitter bot
    '''

    def insertData(self, author, content, date, likes, retweets, url):

        # self.author = author
        # self.content = content
        # self.date = date
        # self.likes = likes
        # self.retweets = retweets
        # self.url = url

        # author = input("Please input Author name: ")
        # content = input("Please input tweet content: ")
        # date = input("Please input date: ")
        # likes = input("Please input no. of likes: ")
        # retweets = input("Please input no. of retweets: ")
        # url = input("Please input URL: ")

        try:
            add_tweets = ("INSERT INTO crawler.tweets " +
               "(author, content, date, likes, retweets, url)" +
               "VALUES ('"+author+"', '"+content+"', '"+date+"', '"+likes+"', '"+retweets+"', '"+url+"')")

            self.cursor.execute(add_tweets)
            print("insert successfully")
            self.cnx.commit()
        except:
            print("insert fail")

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

