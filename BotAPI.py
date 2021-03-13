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
        query = ("SELECT * FROM crawler.tweets")
        self.cursor.execute(query)
        astr = ''
        for i in self.cursor:
            astr += str(i)
        return astr
    
a = BotAPI()
a.insertData("hong", "aaaaaaa", "2021-02-03", "666", "4753", "www.pochai.com")
    #cursor.close()
    #cnx.close()

       
    
