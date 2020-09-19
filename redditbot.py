import praw
import time
import pickle

reddit = praw.Reddit(client_id="ezKvopEp5BEwJw", 
client_secret="c-MsoJWEP3m12OGk9DVpiHXnPwo", 
username="desktopworm85bot", 
password="3FJ7+Jjt:eD8fj&", 
user_agent="Simple bot by /u/desktopworm85")

with open("replied.dat", "rb") as fp:
    replied_to = pickle.load(fp)
    print("Loaded")

while True:
    for mention in reddit.inbox.mentions(limit=25):
        if mention.id not in replied_to:
            mention.reply("hello")
            replied_to.append(mention.id)
            print("Message sent")
    
    with open("replied.dat", "wb") as fp:
        pickle.dump(replied_to, fp)
        print("Saved")
    
    time.sleep(10)