import praw
import pandas as pd
reddit = praw.Reddit(client_id='EsajlvC8jp3hng', client_secret=	'Q-Z71dXqCVqJCraCY_wqxgagZyw', user_agent='Reddit WebScraping')

# get 10 hot posts from MachineLearning subreddit
posts = []
hot_posts = reddit.subreddit('CompTIA').new(limit=1000)
for post in hot_posts:
    postTitle = post.title.lower()
    if postTitle.find('a+') != -1 and postTitle.find('passed') != -1:
        posts.append([post.title, post.score])
posts = pd.DataFrame(posts, columns=['title', 'score'])
print(posts)
