import praw
from prawoauth2 import PrawOAuth2Server
from prawoauth2 import PrawOAuth2Mini
from tkinter import *



def oAuth():
    global MESSAGE
    global TOKENS 
    global USER
    global ENTRY
    user_agent = 'Cleannit by u/rlnaveenrm'
    reddit_client = praw.Reddit(user_agent=user_agent)
    scopes = ['identity', 'read', 'submit', 'history', 'edit']
    oauthserver = PrawOAuth2Server(reddit_client, app_key="gqNezasru70jDg",
                                    app_secret = "None",
                                   state=user_agent, scopes=scopes)
    oauthserver.start()
    TOKENS = oauthserver.get_access_codes()
    oauth_helper = PrawOAuth2Mini(reddit_client, app_key="gqNezasru70jDg",
                                  app_secret="None", access_token=TOKENS["access_token"],
                                  scopes=TOKENS["scope"], refresh_token=TOKENS["refresh_token"])
    USER = reddit_client.get_redditor(reddit_client.get_me())
    MESSAGE = ENTRY.get('1.0',END)

def editMessage():
    oAuth()
    for comment in USER.get_comments(limit=None):
        comment.edit(MESSAGE)

def deleteMessage():
    oAuth()
    editMessage()
    for comment in USER.get_comments(limit=None):
        comment.delete()

top = Tk()
top.wm_title("CLEANNIT by /u/rlnaveenrm")
label = Label(top, text="Enter message to replace your comments with")
label.pack( side = TOP, pady = 10)
ENTRY = Text(top, height= 10, width=40)
ENTRY.config(wrap = WORD)
ENTRY.pack(side = TOP, padx =10, pady = 10)
ENTRY.insert(END, """This comment has been overwritten by a bot for privacy reasons. Check out http://github.com for the windows executable or the python script""")
button0 = Button(top, text ="Instructions", command = editMessage)
button0.config(width = 12)
button0.pack(side = LEFT, padx = 10, pady = 10)
button1 = Button(top, text ="Edit", command = editMessage)
button1.config(width = 12)
button1.pack(side = LEFT, padx = 10, pady = 10)
button2 = Button(top, text ="Delete", command = deleteMessage)
button2.config(width = 12)
button2.pack(side = RIGHT,padx = 10, pady = 10)
top.mainloop()