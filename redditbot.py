import praw
import time
import pickle

reddit = praw.Reddit(client_id="ID", 
client_secret="secret", 
username="desktopworm85bot", 
password="pass", 
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
