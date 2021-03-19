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


class Sentimental_Analysis:

    def __init__(self):
        self.twitter = np.array([len(pd.read_csv('foodpanda_tweets.csv').index), len(
            pd.read_csv('deliveroo_tweets.csv').index)])
        self.reddit = np.array([len(pd.read_csv(
            'foodpanda_reddit.csv').index), len(pd.read_csv(
                'deliveroo_reddit.csv').index)])
        # self.grabfood = [len(pd.read_csv('grabfood_tweets.csv').index), len(pd.read_csv(
        # 'grabfood_reddit.csv').index), len(pd.read_csv('grabfood_yahoo.csv').index)]

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

    def plot_pie(score):
        """! plot_pie(score)
        @brief plots a pir chart with a given set of scores
        @param score of float type
        """
        highlight = (0.1, 0, 0)
        data = [score['pos'], score['neg'], score['neu']]
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        sentiment = ['Positive', 'Negative', 'Neutral']
        ax.pie(data, explode=highlight, labels=sentiment, autopct='%1.1f%%',
               shadow=True, startangle=90)
        plt.savefig('./sent_anal.png')
        # plt.show()

    def plot_radar(self):
        df = pd.DataFrame({
            'Food': ['Foodpanda', 'Deliveroo'],
            'Twitter': self.twitter,
            'Reddit': self.reddit,
        })
        # get number of food delivery
        delivery_services = list(df)[:1]
        count = len(delivery_services)

        # get ange of axis
        angle = [n / float(count) * 2 * pi for n in range(count)]
        angle += angle[:1]

        # initialise plot
        ax = plt.subplot(111, polar=True)

        # Draw one axe per variable + add labels
        plt.xticks(angle[:-1], delivery_services)

        # get xlabels
        ax.set_rlabel_position(0)
        plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
        plt.ylim(0, 40)

        values = df.loc[0].drop('Food').values.flatten().tolist()
        values += values[:1]
        ax.plot(angle, values, linewidth=1,
                linestyle='solid', label="Foodpanda")
        ax.fill(angle, values, 'b', alpha=0.1)

        values = df.loc[1].drop('Food').values.flatten().tolist()
        values += values[:1]
        ax.plot(angle, values, linewidth=1,
                linestyle='solid', label="Deliveroo")
        ax.fill(angle, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # Show the graph
        plt.show()


if __name__ == "__main__":
    hello = Sentimental_Analysis()
    hello.plot_radar()
