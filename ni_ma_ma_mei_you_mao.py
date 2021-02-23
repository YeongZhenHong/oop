import re
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# removes all punctuations, special symbols, urls and converts to lowercase
def clean(file):
    text = open(file).read()
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
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]

    # convert filtered_words into string(VADER cannot take in a List)
    return " ".join(filtered_words)


def sentiment_analyse(text):
    value = SentimentIntensityAnalyzer().polarity_scores(text)
    neg = value['neg']
    pos = value['pos']
    if neg > pos:
        print("Negative  Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")
    print(value)
    return value


def plot_bar(score):
    data = [score['pos'], score['neg'], score['neu']]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    sentiment = ['Positive', 'Negative', 'Neutral']
    ax.bar(sentiment, data)
    plt.show()


if __name__ == "__main__":
    score = sentiment_analyse(clean('tweets.json'))
    plot_bar(score)
