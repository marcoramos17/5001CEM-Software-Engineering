### FORUM ###
import database as db
#Import to get time#
import time
#Import to get date#
from datetime import date

def INSERTINTO(username, title, body):
    db.db_send_to_forum(username, title, body)
    return

def INSERTINTOREPLY(postID, username, title, body):
    db.db_reply_to_forum(postID, username, title, body)
    return

def GETALLMESSAGES():
    return db.db_get_forum_items()

def GETALLREPLIES(messageID):
    return db.db_get_forum_replies(messageID)





