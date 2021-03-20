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


if __name__ == "__main__":
    reddit = len(pd.read_csv('foodpanda_reddit.csv').index)
    print(reddit)
