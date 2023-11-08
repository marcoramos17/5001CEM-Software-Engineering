###Animal Profiles###

from guizero import *
from main import *

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


