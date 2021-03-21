"""! 
@file InstagramCrawler.py
@author Kendrick Ang 2609737A
@brief This file contains the Instagram Crawler sub class
@version 1.0
@section DESCRIPTION
Runs instagram crawler to crawl data
@section usage_main Usage
e.g instagram = InstagramCrawler('foodpandasg')
    instagram.crawl()
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
from pandas import DataFrame
import re
from Crawler import Crawler


class InstagramCrawler(Crawler):
    """! The instagram crawler sub class.
    @brief Defines a instagram Crawler subclass to crawl instagram dataset.
    @brief Inherits from Crawler based class.
    """

    # user & post list to store their respective data
    users_list = []
    posts_list = []
    date_list = []
    time_list = []

    def __init__(self, hashtag, post=10):
        """! The Instragram Crawler class initializer.
        @param hashtag The search tag we want to crawl
        @param post the amount of posts to be crawled
        @return An instance of Instagram Crawler class initialized with specified hashtag and post
        """
        super().__init__()
        super().set_Settings(hashtag, post)
        self.setup()
        self.login(['insert username'], ['insert password'])
        self.navigateViaHashTag()
        # self.scroll_down()

    def setup(self):
        """! Setup the selenium webdriver with certain options and navigates to instagram page.
        """
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://instagram.com")
        time.sleep(2)

    def login(self, _username, _password):
        """! Logins into instagram using username and password.
        """
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username_input.clear()
        username_input.send_keys(_username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password_input.clear()
        password_input.send_keys(_password)

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(4)

    def scroll_down(self, timer=5):
        """! Scrolls instagram page down indefinitely as it loads dynamically, 
        not used in here as we use the arrow keys to navigate through the posts.
        """
        prev_height = self.driver.execute_script(
            "return document.body.scrollHeight")
        html = self.driver.find_element_by_tag_name('html')

        while True:
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html.send_keys(Keys.END)
            time.sleep(timer)
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == prev_height:
                break
            prev_height = new_height

    def loadAllComments(self):
        """! Load entire comments from a single post by clicking the (+) button continuously
        till all comments are loaded.
        """
        loadMore = True
        while loadMore:
            time.sleep(2)
            try:
                if self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button"):
                    self.driver.find_element_by_xpath(
                        "/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button").click()
            except:
                loadMore = False

    def loadAllReplies(self):
        """! Load entire replies from a single post by expanding all the 'view replies'.
        """
        viewReplies = self.driver.find_elements_by_class_name("EizgU")
        try:
            for reply in viewReplies:
                reply.click()
                time.sleep(2)
        except:
            pass

    def navigateViaHashTag(self):
        """! Navigate to pages via the url + tags 
        """
        self.driver.get('https://www.instagram.com/explore/tags/' +
                        super().get_searchString() + '/')
        time.sleep(4)

    def crawl(self):
        """! Main function to start crawling data and export it to .csv file.
        @brief Clicks the first post, then loops through the posts by selecting the right arrow key
        to extract data and then output the data to a .csv file.
        """

        # click first initial post in the page
        profile = self.driver.find_element_by_class_name("v1Nh3").click()
        time.sleep(5)

        # keep repeating the steps loadComment->loadReplies->ExtractData till the limit
        for i in range(super().get_searchLimit()):
            try:
                self.loadAllComments()
                time.sleep(3)
                self.loadAllReplies()
                time.sleep(3)
                self.extractData()
                nextpage = self.driver.find_element_by_class_name(
                    "coreSpriteRightPaginationArrow").click()
                time.sleep(3)

            except:
                break

        self.outputToFile()

    def extractData(self):
        """! Extract data from the posts (e.g username, comments, date & time)
        """
        # find the list of users and post
        users = self.driver.find_elements_by_class_name('_6lAjh')
        post = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/span")
        datetime = self.driver.find_elements_by_xpath(
            "//div[@class='C4VMK']/div/div//time[@class='FH9sR Nzb55']")

        # loop through the user list and extract the text
        for user in users:
            self.users_list.append(user.text)

        # loop through the date and time list and extract the text
        for dt in datetime:
            date = dt.get_attribute("datetime").split("T")[0]
            time = dt.get_attribute("datetime").split("T")[1].split(".")[0]
            self.date_list.append(date)
            self.time_list.append(time)

        # loop through the post list and extract the text
        for p in post:
            self.posts_list.append(p.text.replace('\r', '').replace('\n', ''))

    def outputToFile(self, filename="Instagram"):
        """! Export data to .csv file.
        @param filename Amend the export filename (optional)
        """
        data = {
            "user": self.users_list,
            "posts": self.posts_list,
            "date": self.date_list,
            "time": self.time_list
        }

        df = pd.DataFrame(data=data)
        df.to_csv("./CSV/"+self.get_searchString() + '_' + filename + ".csv")
        #df.to_json('insta.json', orient='records', indent=1)
