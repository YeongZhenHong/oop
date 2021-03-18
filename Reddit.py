import praw
import csv
import Auth_Token

def reddit_obj():
    reddit = praw.Reddit(client_id=Auth_Token.REDDIT_CLIENT, client_secret=Auth_Token.REDDIT_SECRET, user_agent=Auth_Token.REDDIT_AGENT, username=Auth_Token.REDDIT_USERNAME, password=Auth_Token.REDDIT_PASSWORD)
    return reddit


def crawl():
    redditCrawl = reddit_obj()
    singapore = redditCrawl.subreddit("singapore").search('foodpanda')
    posts = []
    for i in singapore:
        title = i.title
        url = i.url
        commentCount = i.num_comments
        date = i.created
        post = (title, url, commentCount, date)
        posts.append(post)


    with open('reddit.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Link', 'Comment Count', 'Date'])
        writer.writerows(posts)


if __name__ == '__main__':
    crawl()
