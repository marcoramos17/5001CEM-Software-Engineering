import time
from guizero import *
from information import *

################### AIDENS WORK ##############################

def writeArticleLinkHome(articleDir):
    
    articleDir = "articles/" + articleDir
    
    file = open(articleDir, "r")
    extractHeader = file.readline()
    file.close()

    articleLink = Box(homePg, width="fill", align="top")
    articleHeader = Text(articleLink, text=extractHeader, align="left")
    articleOpenButton = PushButton(articleLink, align="right", text="Open", command=openArticles)
    articlePlaceholder = Text(articleLink, align="top")


###################################################################

        
# Takes the input from usernameTB and returns the username
def submitUsername():
    username = usernameTB.value
    return username
# Takes the input from PasswordTB and returns the password
def submitPassword():
    password = passwordTB.value
    return password

# gets the variables username and password and calls the userLogin function
def userLogin_username_password_dbUsername_dbPassword():
    username = submitUsername()
    password = submitPassword()
    userLogin(username, password, "Liam", "Password")

#check the username is the same as the one in the database
#check the password is the same as the one in the database
#If they are, display a correct username/password message and continue to website
#Else, Print details incorrect and retry details.
def userLogin(username, password, dbUsername, dbPassword):
    check1 = False
    check2 = False
    while check1 == False or check2 == False:
        if username == dbUsername:
            check1 = True
            print("check 1")
        if password == dbPassword:
            check2 = True
            print("check 2")
        if check1 == True and check2 == True:
            print("Username and password are correct")
            homepage()
        else:
            print("Invalid Username or Password")
            break
        

#continue later to make a mini animation of logging in 
def waitingToLogin():
    loggedIn = False
    while loggedIn == False:
        loggingIn = Text(loginPg, text = "Logging In .")
        loggingIn.hide()
        loggingIn = Text(loginPg, text = "Logging In ..")
        loggingIn.hide()
        loggingIn = Text(loginPg, text = "Logging In ...")
        loggingIn.hide()
    
def createAccount():
    def closeCreateAcc():
        accWindow.hide()
    def saveDetails():
        print("")

    def guestLogin():
        def ctnuAsGuest():
            print("go To main Website")
            
        def goBack():
            guestWindow.hide()
            
        def closeAll():
            loginPg.hide()
            accWindow.hide()
            guestWindow.hide()

        #####################################################################################
        ############################## Guest Login ##########################################
        #####################################################################################
            
        #creates the guest page
        guestWindow = Window(loginPg, title = "Guest Login")

        #title for guest page
        guestTitle = Text(guestWindow, text = "Guest Page")

        # creates a blank gap 
        placeHolder1 = Text(guestWindow)

        ###############################################################
        # empty box to create a space to the left of the buttons 
        guestWindowBtn = Box(guestWindow, width = "fill", align = "top")

        # creates a blank gap 
        pH1 = Box(guestWindowBtn, width = "fill", align = "left")
        
        #continue as guest 
        guestCtnuBtn = PushButton(guestWindowBtn, text = "Push to Continue as a Guest", command = ctnuAsGuest, align = "left", width = "fill")

        #go back a window
        goBackBtn = PushButton(guestWindowBtn, text = "Return", command = goBack, align = "left", width = "fill")
        
        #close Window
        closeBtn = PushButton(guestWindowBtn, text = "Exit", command = closeAll, align = "left", width = "fill" )

        # creates a blank gap 
        pH2 = Box(guestWindowBtn, width = "fill", align = "left")
        ################################################################

    ########################################################################################    
    ############################## Create Account ##########################################
    ########################################################################################
        
    # creates the create account page
    accWindow = Window(loginPg, title = "Create Account")
    
    # Main title of window
    createTitle = Text(accWindow, text="Create Account")

    # creates a blank gap 
    placeHolder1 = Text(accWindow)
    
    #email textbox
    email = Text(accWindow, text="Enter your Email")
    textbox = TextBox(accWindow, width=40)

    #password textbox
    password = Text(accWindow, text="Enter your Password")
    textbox = TextBox(accWindow, width=40)
    
    #password Confirmation
    password = Text(accWindow, text="Re-enter your Password")
    textbox = TextBox(accWindow, width=40)

    # creates a blank gap 
    placeHolder2 = Text(accWindow)

    ######################################################################
    # A box to hold all the buttons 
    accWindowBtn = Box(accWindow, width = "fill", align = "top")
    
    # empty box to create a space to the left of the buttons 
    pH1 = Box(accWindowBtn, width = "fill", align = "left")
    #close Window
    closeBtn = PushButton(accWindowBtn, text = "Return to previous Page", command =  closeCreateAcc, align = "left", width = "fill")
    #Confirm details
    confirm = PushButton(accWindowBtn, text = "Enter", command =  saveDetails, align = "left",  width = "fill")
    # empty box to create a space to the left of the buttons 
    pH2 = Box(accWindowBtn, width = "fill", align = "left")
    ######################################################################

    # creates a blank gap 
    placeHolder2 = Text(accWindow)

    #Guest Login
    guestText = Text(accWindow, text="Do you wish to log in as guest instead ?")
    # creates a blank gap 
    placeHolder2 = Text(accWindow)
    guestAccBtn = PushButton(accWindow, text = "Guest login", command = guestLogin )
    
################################################################################
################################# Home Page ####################################
################################################################################
    
def homepage():


    # call info hub
    def callHub():

        openHome()
        

    def callArticles():
        openArticles()
        
    def callProfile():
        profilesPage()

    def callMessages():
        print("Messages")

    def callMinigames():
        print("Minigames")

    
    loginPg.hide()
    homePg.show()
    
    
    
    ##########################################################################

    # creates a blank gap 
    placeHolder0 = Text(homePg)
    
    # infoBox to hold buttons 
    infoBox = Box(homePg, width = "fill", align = "top")
    
    # empty box to create a space to the left of the buttons 
    pH1 = Box(infoBox, width = "fill", align = "left")

    # Opens Info Hub
    infoHubBtn = PushButton(infoBox, text = "Info Hub", command = callHub, align = "left", width = "25")

    # opens articles
    articlesBtn = PushButton(infoBox, text = "Articles", command =  callArticles, align = "left", width = "25")

    # empty box to create a space to the right of the buttons
    pH2 = Box(infoBox, width = "fill", align = "left")

    # creates a blank gap 
    placeHolder1 = Text(homePg)


    #Communication Box
    communicationBox = Box(homePg, width = "fill", align = "top")

    # empty box to create a space to the left of the buttons 
    pH3 = Box(communicationBox, width = "fill", align = "left")

    # Opens profiles page
    profileBtn = PushButton(communicationBox, text = "Profiles Page", command =  callProfile, align = "left", width = "25")

    # Opens private messages
    messagesBtn = PushButton(communicationBox, text = "Private Messages", command =  callMessages, align = "left", width = "25")

    # empty box to create a space to the right of the buttons
    pH4 = Box(communicationBox, width = "fill", align = "left")

    # creates a blank gap 
    placeHolder2 = Text(homePg)
    

    # Opens private messages
    minigamesBtn = PushButton(homePg, text = "Mini games", command =  callMinigames, align = "top", width = "50")





    writeArticleLinkHome("article1.txt")
    writeArticleLinkHome("article2.txt")
    #





    
    ###########################################################################

####################################################################################
############################# Profiles Page ########################################
####################################################################################
def profilesPage():
    def callCustomisation():
        customisation()

    def callDetails():
        details()

    def callNotifications():
        notifications()
            
    # come back to this (missing profile pic and background) 
    def customisation():
        # creates page
        customisationPg = Window(loginPg, title = "Customisation Page")
        
        # view profile
        profileWin = Window(loginPg, title = "Profile")
        profileWin.hide()

        def  changeBg():
            profileWin.bg = bgCombo.value
            
        ########################################################################
        ########################## profile #####################################
        #######################################################################
        def profile():
            profileWin.show()
            def displayNameVal():
                    displayName = displayNameTB.value
                    return displayName

            def NewDisplayName():
                    #print message and new display name
                    message1 = Text(profileWin, text = "Your display name is:")
                    newDisplayName = displayNameVal()
                    message2 = Text(profileWin, text = newDisplayName)
                    
            def bioVal():
                    bio = bioTB.value
                    return bio            

            def newBio():
                    # add new bio and display
                    message1 = Text(profileWin, text = "Your new bio is")
                    newBio = bioVal()
                    message2 = Text(profileWin, text = newBio)
                    
            NewDisplayName()
            newBio()
        #########################################################################

        # creates a blank gap 
        placeHolder0 = Text(customisationPg)
            
        #box to contain it all
        chngeDetBox = Box(customisationPg, width = "fill", align = "top")
            
        # display name text box 
        displayName = Text(chngeDetBox, text = "Enter your display name", align = "top")
        displayNameTB = TextBox(chngeDetBox, width = 40, align = "top")

        # bio text box
        bio = Text(chngeDetBox, text = "Enter your bio", align = "top")
        bioTB = TextBox(chngeDetBox, width = 40, align = "top")        

        # creates a blank gap 
        placeHolder1 = Text(chngeDetBox)
            
        # view profile btn
        viewProfileBtn = PushButton(chngeDetBox, text = "View Profile", command =  profile, align = "left", width = "fill")

        # select a background colour
        colourMessage = Text(chngeDetBox, text = "select your background colour", align = "top")
        colors = ["grey", "white", "red", "green", "blue"]
        bgCombo = Combo(chngeDetBox, options = colors, selected = profileWin.bg, command = changeBg)

        # creates a blank gap 
        placeHolder2 = Text(customisationPg)
        ###################################################################################
        

    def details():
        detailsPg = Window(loginPg, title = "Details Page")

        
        
        
    def notifications():
        notificationsPg = Window(loginPg, title = "Notifications Page")
        
        # creates a blank gap 
        placeHolder0 = Text(profilesPg)

        # notifications tick box
        notificationsOn = CheckBox(notificationsPg, text = "notifications On?")

        #picture
        # reference this
        notificationsPic = Picture(notificationsPg, image = "notifications.png")

    profilesPg = Window(loginPg, title = "Profiles Page")
    
    ################################################################################
    
    # creates a blank gap 
    placeHolder0 = Text(profilesPg)

    # infoBox to hold buttons 
    Box1 = Box(profilesPg, width = "fill", align = "top")

    # empty box to create a space to the left of the buttons 
    pH1 = Box(Box1, width = "fill", align = "left")
    
    # Opens account customisations
    customisationBtn = PushButton(Box1, text = "Customise Profiles", command =  callCustomisation, align = "left", width = "fill")

    # Opens Account Details
    detailsBtn = PushButton(Box1, text = "Change Details", command =  callDetails, align = "left", width = "fill")

    # Opens Notification Settings
    notificationsBtn = PushButton(Box1, text = "Notification Settings", command =  callNotifications, align = "left", width = "fill")

    # empty box to create a space to the left of the buttons 
    pH2 = Box(Box1, width = "fill", align = "left")

    ################################################################################
    
####################################################################################
############################## User Login ##########################################
####################################################################################
    
#titles the page and colour
loginPg = App(title="KomodoHub")
homePg = Window(loginPg, title = "Home Page")
homePg.hide()

# Main title of app
message = Text(loginPg, text="Komodo Hub")

# creates a blank gap 
placeHolder1 = Text(loginPg)

#username textbox
email = Text(loginPg, text="Enter your Username")
usernameTB = TextBox(loginPg, width = 40)

#password textbox
password = Text(loginPg, text="Enter your Password")
passwordTB = TextBox(loginPg, width = 40)

# creates a blank gap 
placeHolder2 = Text(loginPg)

##########################################################################
# A box to hold all the buttons 
loginPgBtn = Box(loginPg, width = "fill", align = "top")

# empty box to create a space to the left of the buttons 
pH1 = Box(loginPgBtn, width = "fill", align = "left")

# Submits the username and password in the textboxes 
continueButton = PushButton(loginPgBtn, text = "Continue", command = userLogin_username_password_dbUsername_dbPassword, align = "left", width = "fill")

# create account button
CreateAccBtn = PushButton(loginPgBtn, text = "Create Account", command =  createAccount, align = "left", width = "fill")

homeBtn = PushButton(loginPgBtn, text = "home", command =  homepage, align = "left", width = "fill")
# empty box to create a space to the right of the buttons
pH2 = Box(loginPgBtn, width = "fill", align = "left")
###########################################################################

loginPg.display()
