### FORUM ###
#Import for mySQL connection#
import mysql.connector
#Import to get time#
import time
#Import to get date#
from datetime import date

#Connnecting to database and table#
forumDB = mysql.connector.connect(
    host="localhost",
    user="AidenL",
    password="Lico2004*",
    database="Forum"
)

#Function runs SQL for inserting items to DB#
def INSERTINTO(dispName, message):

    forumCursor = forumDB.cursor()
    #SQL Query#
    SQL = "INSERT INTO messages (disp_name, message, day, month, year, hour, minute) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    #Getting Date#
    dateStamp = str(date.today())
    dateList = dateStamp.split("-")
    day = int(dateList[2])
    month = int(dateList[1])
    year = int(dateList[0])

    #Getting Time#
    timeStamp = time.localtime()
    timeStampShort = str(time.strftime("%H:%M", timeStamp))
    timeList = timeStampShort.split(":")
    hour = int(timeList[0])
    minute = int(timeList[1])

    #Values to be inserted#
    values = (dispName, message, day, month, year, hour, minute)

    #Adding values to DB and commiting changes#
    forumCursor.execute(SQL, values)
    forumDB.commit()

    #System displays records inserted#
    print(forumCursor.rowcount, "record inserted")


def INSERTINTOREPLY(messageID, dispName, message):

    forumCursor = forumDB.cursor()
    #SQL Query#
    SQL = "INSERT INTO replies (message_ID, disp_name, message, day, month, year, hour, minute) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    #Getting Date#
    dateStamp = str(date.today())
    dateList = dateStamp.split("-")
    day = int(dateList[2])
    month = int(dateList[1])
    year = int(dateList[0])

    #Getting Time#
    timeStamp = time.localtime()
    timeStampShort = str(time.strftime("%H:%M", timeStamp))
    timeList = timeStampShort.split(":")
    hour = int(timeList[0])
    minute = int(timeList[1])

    #Values to be inserted#
    values = (messageID, dispName, message, day, month, year, hour, minute)

    #Adding values to DB and commiting changes#
    forumCursor.execute(SQL, values)
    forumDB.commit()

    #System displays records inserted#
    print(forumCursor.rowcount, "record inserted")



#Function runs SQL query to return all DB messages#
def GETALLMESSAGES():

    forumCursor = forumDB.cursor()
    #SQL Query#
    SQL = "SELECT * FROM messages ORDER BY message_ID DESC"
    #Runs SQL Query#
    forumCursor.execute(SQL)

    #Variable holds all messages#
    allMessages = forumCursor.fetchall()
    #returns messages#
    return allMessages




def GETALLREPLIES(messageID):

    forumCursor = forumDB.cursor()
    SQL = "SELECT * FROM replies WHERE message_ID = " + str(messageID)

    forumCursor.execute(SQL)
    allReplies = forumCursor.fetchall()
    return allReplies



    
    

#TEST FUNCTION#
def DISPLAYALLMESSAGES():

    forumCursor = forumDB.cursor()
    SQL = "SELECT * FROM messages ORDER BY message_ID DESC"
    forumCursor.execute(SQL)

    allMessages = forumCursor.fetchall()
    
    for x in range(len(allMessages)):

            
        print(allMessages[x][1] + ": " + allMessages[x][2] + "     " + str(allMessages[x][3]) + "/" + str(allMessages[x][4]) + "/" + str(allMessages[x][5]) + " " + str(allMessages[x][6]) + ":" + str(allMessages[x][7]))
        




