'''
Coded by Brendan Tan Wen Yi 2609720T
'''
import re
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from math import pi
import numpy as np
import datetime


class Sentimental_Analysis:

    def __init__(self):
        self.fp_tweets = pd.read_csv('./CSV/foodpanda_tweets.csv')
        self.d_tweets = pd.read_csv('./CSV/deliveroo_tweets.csv')
        self.g_tweets = pd.read_csv('./CSV/grabfood_tweets.csv')

        self.fp_reddit = pd.read_csv('./CSV/foodpanda_reddit.csv')
        self.d_reddit = pd.read_csv('./CSV/deliveroo_reddit.csv')
        self.g_reddit = pd.read_csv('./CSV/grabfood_reddit.csv')

        self.fp_insta = pd.read_csv('./CSV/foodpanda_instagram.csv')
        self.d_insta = pd.read_csv('./CSV/deliveroo_instagram.csv')
        self.g_insta = pd.read_csv('./CSV/grabfood_instagram.csv')

        self.dt = pd.DataFrame({'Food': ['foodpanda', 'deliveroo', 'grabfood'],
                                'Twitter': [len(self.fp_tweets.index), len(self.d_tweets.index), len(self.g_tweets.index)],
                                'Reddit': [len(self.fp_reddit.index), len(self.d_reddit.index), len(self.g_reddit.index)],
                                'Instagram': [len(self.fp_insta.index), len(self.d_insta.index), len(self.g_insta.index)]
                                })

    # removes all punctuations, special symbols, urls and converts to lowercase

    def clean(file):
        """! clean(file)
        @brief cleans text for accurate analysis
        @param name of the file
        @return a string without: /n, special characters/symbols, digits, and stop words
        """
        try:
            # open file and read content
            with open(file, encoding="utf8") as f:
                text = f.read()
        except:
            raise FileNotFoundError('File cannot be opened!')
        # lowercase
        text = text.lower()

        # remove \n
        text = text.replace('\n', "")

        # remove special chars
        cleaned_text = re.sub('<.*?>', '', text)

        # remove urls
        remove_url = re.sub(r'http\S+', '', cleaned_text)

        # remove digits
        remove_num = re.sub('[0-9]+', '', remove_url)

        # split(AKA tokonize) text into words
        tokens = RegexpTokenizer(r'\w+').tokenize(remove_num)

        # remove stop words(I, a, of, for)
        # iterate through tokens, check if word is a stop word, else append to filtered words
        filtered_words = [
            w for w in tokens if not w in stopwords.words('english')]

        # convert filtered_words into string(VADER cannot take in a List)
        return " ".join(filtered_words)

    def Analyse(text):
        """! sentiment analyse(text)
        @brief takes in string and passes it through nltk VADER analyser
        @param string
        @return a list indicating overall positive, negative and neutral score of the given string
        """
        value = SentimentIntensityAnalyzer().polarity_scores(text)
        neg = value['neg']
        pos = value['pos']
        if neg > pos:
            sentiment = 'Negative Sentiment'
        elif pos > neg:
            sentiment = 'Positive Sentiment'
        else:
            sentiment = 'Neutral Sentiment'
        return value, sentiment

    def plot_pie(score, name='sent_anal'):
        """! plot_pie(score)
        @brief plots a pie chart with a given set of scores
        @param score of float type
        """
        highlight = (0.1, 0, 0)
        data = [score['pos'], score['neg'], score['neu']]
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        sentiment = ['Positive', 'Negative', 'Neutral']
        ax.pie(data, explode=highlight, labels=sentiment, autopct='%1.1f%%',
               shadow=True, startangle=90)
        plt.savefig(name)
        # plt.show()

    def plot_radar(self, dat=None, name="sent_anal_spider"):
        """! plot_radar(score)
        @brief plots a radar chart with a given set of scores
        @param score of float type
        """
        if dat is None:
            dat = self.dt

        # number social media crawled
        social = list(dat)[1:]
        N = len(social)

        # find angles of axis
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # initialise spider plot
        ax = plt.subplot(111, polar=True)

        # set axis vertical
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # draw axis for each social media
        plt.xticks(angles[:-1], social)
        ax.get_xaxis().majorTicks[2].label1.set_horizontalalignment('right')
        ax.get_xaxis().majorTicks[1].label1.set_horizontalalignment('left')

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks(color="grey", size=7)

        # foodpanda
        values = dat.loc[0].drop('Food').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, color='#D80765', linewidth=1,
                linestyle='solid', label="Foodpanda")
        ax.fill(angles, values, '#D80765', alpha=0.1)

        # deliveroo
        values = dat.loc[1].drop('Food').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, color='#02CCC0', linewidth=1,
                linestyle='solid', label="Deliveroo")
        ax.fill(angles, values, '#02CCC0', alpha=0.1)

        # grabfood
        values = dat.loc[2].drop('Food').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, color='#029837', linewidth=1,
                linestyle='solid', label="GrabFood")
        ax.fill(angles, values, '#029837', alpha=0.1)

        # legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # show graph
        # plt.show()
        plt.savefig('name')

    def plot_line(self):

        for date in self.fp_tweets['date']:

            # if __name__ == "__main__":
            #     fp = Sentimental_Analysis()
            #     fp.plot_radar(dat=pd.DataFrame({'Food': ['encapsulation', 'inheritence', 'polymorphism'],
            #                                     'var1': [5000, 1000, 2000],
            #                                     'var2': [3500, 1500, 500],
            #                                     'var3': [90, 9000, 6900]
            #                                     }))
