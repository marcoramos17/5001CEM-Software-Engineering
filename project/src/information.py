from guizero import *
from forum import *

userName = "JimmCric582874"

def exitFunc():

    home.hide()
    animalProfiles.hide()
    articles.hide()
    forum.hide()

    

def writeProfile(textDir, imageDir):

    def destroyProfile():

        animalProfile.hide()

        animalProfileHeader.destroy()
        animalProfilePlaceholder.destroy()
        animalProfileText.destroy()
        animalProfileCloseButton.destroy()
        animalProfileImage.destroy()

        animalProfiles.show()
    
    animalProfiles.hide()
    articles.hide()
    forum.hide()
    home.hide()
    
    file = open(textDir, "r")
    headerText = file.readline()
    textList = file.readlines()
    textContent = ""
    
    for i in range(len(textList)):

        textContent = textContent + textList[i]

        
       
    
    animalProfile = Window(home, title="Information Hub - " + headerText)
    animalProfileHeader = Text(animalProfile, text=headerText, align="top")
    animalProfilePlaceholder = Text(animalProfile, text="", align="top")
    

    animalProfileImage = Picture(animalProfile, image=imageDir, align="top")
    animalProfileText = Text(animalProfile, text=textContent, width="fill", align="top")
    animalProfileCloseButton = PushButton(animalProfile, command=destroyProfile, text="Close Profile", align="right")

    
def writeProfileLink(textDir, imageDir):
    
    textDir = "text/" + textDir
    imageDir = "images/" + imageDir
    
    file = open(textDir, "r")
    extractText = file.readline()
    file.close()


    article = Box(animalProfiles, width="fill", align="top")
    articleImage = Picture(article, image=imageDir, align="left")
    articleText = Text(article, text=extractText, align="left")
    articleOpen = PushButton(article, command=writeProfile, args=[textDir,imageDir], text="Open", align="right")

#Function writes Forum Items#
def writeForum():
    #Imbedded function is used when the user clicks send to a forum message#
    def sendForumMsgs():
        #Grabs text from the textbox#
        message = fTextBox.value
        #Calls function from forum.py#
        INSERTINTO(userName, " ",message)

        #reloads messages#
        destroyForumMsgs()
        writeForum()
        
    def replyMessage(x):
        allForumMsgs = GETALLMESSAGES()
        msgID = allForumMsgs[x][0]
        message = fTextBox.value
        INSERTINTOREPLY(msgID, userName, "", message)

        destroyForumMsgs()
        writeForum()

        
    #destroys forum items#
    def destroyForumMsgs():

        allForumMsgsBox.destroy()


    #calls forum.py to display all messages#
    allForumMsgs = GETALLMESSAGES()
    
    allForumMsgsBox = Box(forum, width="fill", align="top")
    
    #Runs for loop to display all messages#
    for x in range(len(allForumMsgs)):
        nameText = allForumMsgs[x][1] + ":    "
        messageText = allForumMsgs[x][3]
        dateTimeText = allForumMsgs[x][4]
        messageBox = Box(allForumMsgsBox, width="fill", align="top")
        name = Text(messageBox, text=nameText, align = "left")
        message = Text(messageBox, text=messageText, align = "left")
        dateTime = Text(messageBox, text=dateTimeText, align="right")

        ###Week 4###
        reply = PushButton(messageBox, text="reply", command=replyMessage, args=[x], align="right")
        currMessage = allForumMsgs[x][0]
        
        allReplies = GETALLREPLIES(currMessage)
        if len(allReplies) > 0:
            for y in range(len(allReplies)):
                rNameText = allReplies[y][2] + ":   "
                rMessageText = allReplies[y][4]
                rDateTimeText = allReplies[y][5]
                replyBox = Box(allForumMsgsBox, width="fill", align="top")
                reply = Text(replyBox, text="Reply: ", align="left")
                rName = Text(replyBox, text=rNameText, align="left")
                rMessage = Text(replyBox, text=rMessageText, align="left")
                rDateTime = Text(replyBox, text=rDateTimeText, align="right")
            

            
    #User input section
    fEnterMsg = Box(allForumMsgsBox, width="fill", align="bottom")

    fPlaceholder3 = Text(fEnterMsg, width="fill", align="left")
    fTextBox = TextBox(fEnterMsg, text="Enter your message", align="left")
    fSendMsgBtn = PushButton(fEnterMsg, command=sendForumMsgs, width="fill", align="left")
    fPlaceHolder4 = Text(fEnterMsg, width="fill", align="left")

    
    
def writeArticleLink(articleDir):
    
    articleDir = "articles/" + articleDir
    
    file = open(articleDir, "r")
    extractHeader = file.readline()
    file.close()

    articleLink = Box(articles, width="fill", align="top")
    articleHeader = Text(articleLink, text=extractHeader, align="left")
    articleOpenButton = PushButton(articleLink, align="right", text="Open", command=writeArticles, args=[articleDir])
    articlePlaceholder = Text(articleLink, align="top")


def writeArticles(articleDir):

    
    file = open(articleDir, "r")
    extractHeader = file.readline()
    extractArticle = file.readlines()
    file.close()

    def destroyArticle():

        articleContainer.destroy()
        articleWindow.hide()
        articles.show()
        
        

    articleWindow = Window(home, title="Information Hub - " + extractHeader, visible=False)
    
    articleContainer = Box(articleWindow, width="fill", align="top")
    articlePlaceholder = Text(articleContainer)
    articleHeader = Text(articleContainer, text=extractHeader, align="top")
    articlePlaceholder2 = Text(articleContainer)


    for x in range(len(extractArticle)):

        articleContent = Text(articleContainer, text=extractArticle[x], align="top")
        

    articleClose = PushButton(articleContainer, text="Close", command=destroyArticle, align="bottom")
    
    
    animalProfiles.hide()
    articles.hide()
    forum.hide()
    home.hide()
    articleWindow.show()


  
def openHome():

    animalProfiles.hide()
    articles.hide()
    forum.hide()
    home.show()
    
    
def openAnimalProf():
    global aPOpened

    #Checks if page already visited#
    if aPOpened == 0:

        #Generates Profile Links#
        writeProfileLink("tiger.txt", "tiger.png")
        writeProfileLink("zebra.txt", "zebra.png")
        writeProfileLink("lion.txt", "lion.png")

        aPOpened = 1

    #Opens animal Profiles window#
    home.hide()
    articles.hide()
    forum.hide()
    animalProfiles.show()



def openArticles():
    global articlesOpened

    if articlesOpened == 0:

        writeArticleLink("article1.txt")
        writeArticleLink("article2.txt")
        writeArticleLink("article3.txt")

        articlesOpened = 1

    
    home.hide() 
    animalProfiles.hide()
    forum.hide()
    articles.show()

def openForum():
    global forumOpened
    
    if forumOpened == 0:
        writeForum()
        forumOpened = 1
        
    
    home.hide()
    animalProfiles.hide()
    articles.hide()
    forum.show()




#Creation of windows, with respective titles#

home = App(title="Information Hub - Home")
animalProfiles = Window(home, title="Information Hub - Animal Profiles")
articles = Window(home, title="Information Hub - Articles")
forum = Window(home, title="Information Hub - Forum")

home.hide()
animalProfiles.hide()
articles.hide()
forum.hide()


#header content#

header = Text(home, text="Information Hub", align="top")
placeholder = Text(home, text="", align="top")

menu = Box(home, width="fill", align="top")
menuButton1 = PushButton(menu, command=openAnimalProf, text="Animal Profiles", align="left", width="fill")
menuButton2 = PushButton(menu, command=openArticles, text="   Articles    ", align="left", width="fill")
menuButton3 = PushButton(menu, command=openForum, text="     Forum     ", align="left", width="fill") 
menuButton4 = PushButton(menu, command=exitFunc, text="     Exit      ", align="left", width="fill")


#Animal Profiles Page Content#

apHeader = Text(animalProfiles, text="Animal Profiles", align="top")
apPlaceholder = Text(animalProfiles, text="", align="top")

apMenu = Box(animalProfiles, width="fill", align="top")
apMenuButton1 = PushButton(apMenu, command=openHome, text="     Home      ", align="left", width="fill")
apMenuButton2 = PushButton(apMenu, command=openArticles, text="   Articles    ", align="left", width="fill")
apMenuButton3 = PushButton(apMenu, command=openForum, text="     Forum     ", align="left", width="fill") 
apMenuButton4 = PushButton(apMenu, command=exitFunc, text="     Exit      ", align="left", width="fill")

    
    
#Articles Page Content#

aHeader = Text(articles, text="Articles", align="top")
aPlaceholder = Text(articles, text="", align="top")
aMenu = Box(articles, width="fill", align="top")
aMenuButton1 = PushButton(aMenu, command=openHome, text="     Home      ", align="left", width="fill")
aMenuButton2 = PushButton(aMenu, command=openAnimalProf, text="Animal Profiles", align="left", width="fill")
aMenuButton3 = PushButton(aMenu, command=openForum, text="     Forum     ", align="left", width="fill") 
aMenuButton4 = PushButton(aMenu, command=exitFunc, text="     Exit      ", align="left", width="fill")
aPlaceholder2 = Text(articles, text="", align="top")

#Forum Page Content#

fHeader = Text(forum, text="Forum", align="top")
fPlaceholder = Text(forum, text="", align="top")

fMenu = Box(forum, width="fill", align="top")
fMenuButton1 = PushButton(fMenu, command=openHome, text="     Home      ", align="left", width="fill")
fMenuButton2 = PushButton(fMenu, command=openAnimalProf, text="Animal Profiles", align="left", width="fill")
fMenuButton3 = PushButton(fMenu, command=openArticles, text="   Articles    ", align="left", width="fill") 
fMenuButton4 = PushButton(fMenu, command=exitFunc, text="     Exit      ", align="left", width="fill")

fPlaceholder2 = Text(forum, align="top")

#Variables check if pages have been opened previously, relevant for#D
#duplication glitch#
global forumOpened, aPOpened, articlesOpened
forumOpened = 0
aPOpened = 0
articlesOpened = 0

#Displays home (main window)

    











