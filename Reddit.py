import praw
import csv
import auth_token

def reddit_obj():
    reddit = praw.Reddit(client_id=auth_token.REDDIT_CLIENT, client_secret=auth_token.REDDIT_SECRET, user_agent=auth_token.REDDIT_AGENT, username=auth_token.REDDIT_USERNAME, password=auth_token.REDDIT_PASSWORD)
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
