"""! 
@file InstagramCrawler.py
@author Kendrick Ang
@brief This file contains the Instagram Crawler sub class
@version 1.0
@section DESCRIPTION
Runs instagram crawler to crawl data
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
from pandas import DataFrame
import re #for replace and split
from Crawler import Crawler


class InstagramCrawler(Crawler):
    """! The instagram crawler sub class
    Defines a instgram Crawler subclass to crawl instagram dataset.
    
    Inherits from Crawler based class
    """

    users_list = []
    posts_list = []
    
    def __init__(self, hashtag):
        """! The Instragram Crawler class initializer
        @param 
        @return An instance of Instagram Crawler class initialized with specified
        """
        self.post = 3
        super().set_searchString(hashtag)
        self.setup()
        self.login("CSC10071007@gmail.com", "P@ssw0rd1007")
        self.navigateViaHashTag()
        #self.scroll_down()

    def setup(self):
        """! 
        
        """
        self.chrome_options = webdriver.ChromeOptions()
        #self.chrome_options.add_argument("--incognito")
        #self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://instagram.com")
        time.sleep(2)

    def login(self, _username, _password):
        """! 
        """
        print('\nlogin...\n')
        username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username_input.clear()
        username_input.send_keys(_username)

        password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password_input.clear()
        password_input.send_keys(_password)
       
        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(4)

    def scroll_down(self, timer=5):
        #dont have to scroll because we are using arrow keys
        prev_height = self.driver.execute_script("return document.body.scrollHeight")
        html = self.driver.find_element_by_tag_name('html')
        
        while True:
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html.send_keys(Keys.END)
            time.sleep(timer)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == prev_height:
                break
            prev_height = new_height

    def loadAllComments(self):
        """!
        """
        loadMore = True
        while loadMore:
            time.sleep(2)
            try:
                if self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button"):
                    self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button").click()
            except:
                loadMore = False

    def loadAllReplies(self):
        """! 
        """
        viewReplies = self.driver.find_elements_by_class_name("EizgU")
        try:
            for reply in viewReplies:
                reply.click()
                time.sleep(2)
        except:
            pass

    def navigateViaHashTag(self):
        self.driver.get('https://www.instagram.com/explore/tags/' + super().get_searchString() + '/')
        time.sleep(4)

    def crawl(self):
        """! main function to start crawling data and export it to .csv file
        """
        profile = self.driver.find_element_by_class_name("v1Nh3").click() #click first post
        time.sleep(5)

        for i in range(self.post):
            try:
                self.loadAllComments()
                time.sleep(3)
                self.loadAllReplies()
                time.sleep(3)
                self.extractData()
                nextpage = self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
                time.sleep(3)
               
            except:
                break
        
        self.outputToFile()

    def extractData(self):
        """! 
        """
        users = self.driver.find_elements_by_class_name('_6lAjh')
        post = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/span")

        for user in users: 
            self.users_list.append(user.text)

        for p in post:
             self.posts_list.append(p.text.replace('\r', '').replace('\n',''))

    def outputToFile(self):
        """! 
        """

        data = {
            "user" : self.users_list,
            "posts": self.posts_list 
        }

        df = pd.DataFrame(data=data)
        df.to_csv("instagram.csv")
        #df.to_json('insta.json', orient='records', indent=1)

insta = InstagramCrawler('foodpandasg')
insta.crawl()
