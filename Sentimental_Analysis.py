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
        """! __init__(self)
        @brief setup default data; inculding dataframes, read location
        @brief allows passing custom dataframes for analysis/ tesing purposes else the default scraped ones are used
        @brief sentimental analysis done this way for easier unit testing development   
        """
        self.fp_tweets = pd.read_csv('./CSV/FoodPanda_Twitter.csv')
        self.d_tweets = pd.read_csv('./CSV/Deliveroo_Twitter.csv')
        self.g_tweets = pd.read_csv('./CSV/GrabFood_Twitter.csv')

        self.fp_reddit = pd.read_csv('./CSV/FoodPanda_Reddit.csv')
        self.d_reddit = pd.read_csv('./CSV/Deliveroo_Reddit.csv')
        self.g_reddit = pd.read_csv('./CSV/GrabFood_Reddit.csv')

        self.fp_insta = pd.read_csv('./CSV/FoodPanda_Instagram.csv')
        self.d_insta = pd.read_csv('./CSV/Deliveroo_Instagram.csv')
        self.g_insta = pd.read_csv('./CSV/GrabFood_Instagram.csv')

        self.fp_yahoo = pd.read_csv('./CSV/FoodPanda_Yahoo.csv')
        self.d_yahoo = pd.read_csv('./CSV/Deliveroo_Yahoo.csv')
        self.g_yahoo = pd.read_csv('./CSV/GrabFood_Yahoo.csv')

        # foodpanda freq date df
        fp_timestamp = [self.fp_tweets,
                        self.fp_reddit]
        # combine csv
        self.fp_combined = pd.concat(fp_timestamp)
        # extract dates and count freq of date occurance
        fp_df = self.fp_combined['date' or 'Date'].str.split(
        ).str[0].value_counts().sort_index().reset_index()
        # formatting
        fp_df.columns = ['Date', 'Freq']
        # make 'Date' column an object
        fp_df['Date'] = pd.to_datetime(fp_df['Date'])
        self.fp_freq_time = fp_df

        # deliveroo freq date df
        d_timestamp = [self.d_tweets,
                       self.d_reddit]
        self.d_combined = pd.concat(d_timestamp)
        d_df = self.d_combined['date' or 'Date'].str.split(
        ).str[0].value_counts().sort_index().reset_index()
        d_df.columns = ['Date', 'Freq']
        d_df['Date'] = pd.to_datetime(d_df['Date'])
        self.d_freq_time = d_df

        # grab freq date df
        g_timestamp = [self.g_tweets,
                       self.g_reddit]
        self.g_combined = pd.concat(g_timestamp)
        g_df = self.g_combined['date' or 'Date'].str.split(
        ).str[0].value_counts().sort_index().reset_index()
        g_df.columns = ['Date', 'Freq']
        g_df['Date'] = pd.to_datetime(g_df['Date'])
        self.g_freq_time = g_df

        self.dt = pd.DataFrame({'Food': ['foodpanda', 'deliveroo', 'grabfood'],
                                'Twitter': [len(self.fp_tweets.index), len(self.d_tweets.index), len(self.g_tweets.index)],
                                'Reddit': [len(self.fp_reddit.index), len(self.d_reddit.index), len(self.g_reddit.index)],
                                'Instagram': [len(self.fp_insta.index), len(self.d_insta.index), len(self.g_insta.index)],
                                "Yahoo": [len(self.fp_yahoo.index), len(self.d_yahoo.index), len(self.g_yahoo.index)]
                                })

    # removes all punctuations, special symbols, urls and converts to lowercase
    def clean(self, file):
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

    def Analyse(self, text):
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
        return pos

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
        ax.get_xaxis().majorTicks[1].label1.set_horizontalalignment('left')
        ax.get_xaxis().majorTicks[3].label1.set_horizontalalignment('right')
        # ax.get_xaxis().majorTicks[1].label1.set_horizontalalignment('left')

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
        plt.savefig("./docs/"+name, dpi=100)

    def plot_line(self, name="sent_anal_line", fp_df=None, d_df=None, g_df=None):
        """! plot_line(score)
        @brief plots a line chart; frequency over datetime 
        @param optional name
        """
        if fp_df is None:
            fp_df = self.fp_freq_time

        if d_df is None:
            d_df = self.d_freq_time

        if g_df is None:
            g_df = self.g_freq_time

        fig, ax = plt.subplots()

        # foodpanda
        ax.plot(fp_df['Date'], fp_df['Freq'],
                color='#D80765', label='FoodPanda')

        # deliveroo
        ax.plot(d_df['Date'], d_df['Freq'], color='#02CCC0', label='Deliveroo')

        # GrabFood
        ax.plot(g_df['Date'], g_df['Freq'], color='#029837', label='GrabFood')

        fig.autofmt_xdate()

        plt.legend(loc='upper left')
        plt.savefig("./docs/"+name)
        # plt.show()

    def get_positive(self):
        """! get_positive(self)
        @brief generates positive score based on scraped content
        """
        score = []
        fp = Sentimental_Analysis()
        fp_positive = fp.clean('./CSV/FoodPanda_Instagram.csv') + fp.clean(
            './CSV/FoodPanda_Reddit.csv') + fp.clean('./CSV/Foodpanda_Twitter.csv') + fp.clean('./CSV/FoodPanda_Yahoo.csv')
        score.append(fp.Analyse(fp_positive))
        g_positive = fp.clean('./CSV/GrabFood_Instagram.csv') + fp.clean('./CSV/GrabFood_Reddit.csv') + \
            fp.clean('./CSV/GrabFood_Twitter.csv') + \
            fp.clean('./CSV/GrabFood_Yahoo.csv')
        score.append(fp.Analyse(g_positive))
        d_positive = fp.clean('./CSV/Deliveroo_Instagram.csv') + fp.clean('./CSV/Deliveroo_Reddit.csv') + \
            fp.clean('./CSV/Deliveroo_Twitter.csv') + \
            fp.clean('./CSV/Deliveroo_Yahoo.csv')
        score.append(fp.Analyse(d_positive))
        return score


if __name__ == "__main__":
    fp = Sentimental_Analysis()
    fp.plot_line()
    fp.plot_radar()
