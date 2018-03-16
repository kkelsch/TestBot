import praw
import pdb
import re
import os

# Create the Reddit Instance
reddit = praw.Reddit('bot1')

# List of posts replied to, create empty array if not exists
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to)) #delete any empty ids in the array

# Create the subreddit object
subreddit = reddit.subreddit("LadyTesla")

# Get the top 5 values from our subreddit
for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")