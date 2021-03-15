import praw
import csv

def reddit_obj():
    reddit = praw.Reddit(client_id='SO--Wv0Ey3tvKA', client_secret='NswvAZW_UE_UxBjLtQj4FTdiSJ5gaw', user_agent='redditcrawl', username='orhstin', password='redditcrawl123')
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
