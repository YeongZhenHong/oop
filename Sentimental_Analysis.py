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
        df = pd.DataFrame({'Social media': ['Reddit', 'Instagram', 'Twitter'],
                           'Col F': [len(pd.read_csv('./foodpanda_reddit.csv').index), len(pd.read_csv('./foodpandasg_instagram.csv').index), len(pd.read_csv('./foodpanda_tweets.csv').index)],
                           'Col D': [len(pd.read_csv('./deliveroo_reddit.csv').index), len(pd.read_csv('./deliveroo_instagram.csv').index), len(pd.read_csv('./deliveroo_tweets.csv').index)],
                           'Col G': [len(pd.read_csv('./grabfood_reddit.csv').index), len(pd.read_csv('./grabfood_instagram.csv').index), len(pd.read_csv('./grabfood_tweets.csv').index)]})
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="polar")

        # theta has 5 different angles, and the first one repeated
        theta = np.arange(len(df) + 1) / float(len(df)) * 2 * np.pi
        # values has the 5 values from 'Col B', with the first element repeated
        values = df['Col B'].values
        values = np.append(values, values[0])

        # draw the polygon and the mark the points for each angle/value combination
        ax.plot(theta, values, color="#D70465",
                marker="o", label="Name of Col F")
        plt.xticks(theta[:-1], df['Social media'], color='grey', size=12)
        # to increase the distance of the labels to the plot
        ax.tick_params(pad=10)
        # fill the area of the polygon with green and some transparency
        ax.fill(theta, values, '#D70465', alpha=0.1)

        # plt.legend() # shows the legend, using the label of the line plot (useful when there is more than 1 polygon)
        plt.title("Post count for each social media of each delivery service")
        plt.savefig('./spider_sent_anal.png')
        # plt.show()


if __name__ == "__main__":
    fp = Sentimental_Analysis()
    fp.plot_radar()
