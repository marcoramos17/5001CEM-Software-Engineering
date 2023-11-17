import time
from CaptchaFunction import *
from guizero import *
from SupportTickets import *
from SARForm import *
from information import *
import accounts as usr

# Takes the input from usernameTB and returns the username
def submitUsername():
    username = usernameTB.value
    return username
# Takes the input from PasswordTB and returns the password
def submitPassword():
    password = passwordTB.value
    return password

def submitCaptcha():
    captchaVal = captchaTB.value
    return captchaVal

# gets the variables username and password and calls the userLogin function
def userLogin_username_password_dbUsername_dbPassword(captchaCorrect):
    username = submitUsername()
    password = submitPassword()
    captchaVal = submitCaptcha()

    userLogin(username, password, captchaCorrect, captchaVal, "Liam", "Password")

#check the username is the same as the one in the database
#check the password is the same as the one in the database
#If they are, display a correct username/password message and continue to website
#Else, Print details incorrect and retry details.
def userLogin(username, password, captchaCorrect, captchaVal,  dbUsername, dbPassword):
    check1 = False
    check2 = False
    check3 = False
    print(f"usr: {username}")
    print(f"pwd: {password}")
    if captchaVal == captchaCorrect:
        if acCCombo.value == "student":
            user = usr.StudentAccount(False,
                                    password=password,
                                    username=username)
        elif acCCombo.value == "teacher":
            user = usr.ProfessorAccount(False,
                                    password=password,
                                    username=username)
        elif acCCombo.value == "business":
            user = usr.BusinessAccount(False,
                                    password=password,
                                    username=username)
        elif acCCombo.value == "personal":
            user = usr.PersonalAccount(False,
                                    password=password,
                                    username=username)
        elif acCCombo.value == "school":
            user = usr.SchoolAccount(False,
                                    password=password,
                                    username=username)
        homepage()
    else:
        print("Invalid Username or Password")
        

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
    loginPg.hide()
    def closeCreateAcc():
        accWindow.hide()
        loginPg.show()
        
    def saveDetails():
        print("")

    def guestLogin():
        accWindow.hide()
        def ctnuAsGuest():
            homepage()
            
        def goBack():
            guestWindow.hide()
            accWindow.show()
            
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
    
    # first name
    firstName = Text(accWindow, text="Enter your First name")
    firstNameTB = TextBox(accWindow, width=40)

    # last name
    lastName = Text(accWindow, text="Enter your Last name")
    lastNameTB = TextBox(accWindow, width=40)

    #password textbox
    password = Text(accWindow, text="Enter your Password")
    passwordTB = TextBox(accWindow, width=40)

    # location
    location = Text(accWindow, text="Enter your Location")
    locationTB = TextBox(accWindow, width=40)   

    # dob
    dob = Text(accWindow, text="Enter your date of birth")
    dobTB = TextBox(accWindow, width=40)

    # access code
    accessCode = Text(accWindow, text="Enter your Access Code")
    accessCodeTB = TextBox(accWindow, width=40)


#################################################################################
    def  accTypeCreation():
        user = None
        if accCombo.value == "student":
            user = usr.StudentAccount(True,
                                      password=passwordTB.value,
                                      fst_name=firstNameTB.value,
                                      lst_name=lastNameTB.value,
                                      location=locationTB.value,
                                      date_birth=dobTB.value,
                                      access_code=accessCodeTB.value)
        elif accCombo.value == "teacher":
            user = usr.ProfessorAccount(True,
                                      password=passwordTB.value,
                                      fst_name=firstNameTB.value,
                                      lst_name=lastNameTB.value,
                                      location=locationTB.value,
                                      date_birth=dobTB.value,
                                      access_code=accessCodeTB.value)
        elif accCombo.value == "business":
            user = usr.BusinessAccount(True,
                                      password=passwordTB.value,
                                      fst_name=firstNameTB.value,
                                      lst_name=lastNameTB.value,
                                      location=locationTB.value,
                                      date_birth=dobTB.value,
                                      access_code=accessCodeTB.value)
        elif accCombo.value == "personal":
            user = usr.PersonalAccount(True,
                                      password=passwordTB.value,
                                      fst_name=firstNameTB.value,
                                      lst_name=lastNameTB.value,
                                      location=locationTB.value,
                                      date_birth=dobTB.value,
                                      access_code=accessCodeTB.value)
        elif accCombo.value == "school":
            user = usr.SchoolAccount(True,
                                      password=passwordTB.value,
                                      fst_name=firstNameTB.value,
                                      lst_name=lastNameTB.value,
                                      location=locationTB.value,
                                      date_birth=dobTB.value,
                                      access_code=accessCodeTB.value)
        return user
    # select a background colour
    accoutnTypeMessage = Text(accWindow, text = "select your account type", align = "top")
    accountTypes = ["student", "teacher", "business", "personal", "school"]
    accCombo = Combo(accWindow, options = accountTypes, selected = accWindow)

    

#################################################################################


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
    user = PushButton(accWindowBtn, text = "Enter", command =  accTypeCreation, align = "left",  width = "fill")
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
    return user
################################################################################
################################# Home Page ####################################
################################################################################
    
def homepage():
    loginPg.hide()
    # call info hub 
    def callHub():
        openHome()

    def callArticles():
        openArticles()
        
    def callProfile():
        profilesPage(homePg)

    def callMessages():
        print("Messages")

    def callMinigames():
        Minigames()
        
    homePg = Window(loginPg, title = f"Home Page")
    
    ##########################################################################

    # creates a blank gap 
    placeHolder0 = Text(homePg)
    
    headerBox = Box(homePg, width = "fill", align = "top")
    header = Text(headerBox, text="Home", width = "fill", align="left")
    supportTickBtn = PushButton(headerBox, text="Support", align="right", command=supportTicketsForm, args=["LiarnesIphone"])
    SARBtn = PushButton(headerBox, text="Subject Access Request", align="right", command=SARForm, args=["LiarnesIphone"])
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


    ###########################################################################

####################################################################################
############################# Profiles Page ########################################
####################################################################################
def profilesPage(homePg):
    homePg.hide()
    def callCustomisation():
        customisation()

    def callDetails():
        details()

    def callNotifications():
        notifications()

    def returnHome():
        profilesPg.hide()
        homePg.show()
            
    # come back to this (missing profile pic and background) 
    def customisation():
        profilesPg.hide()
        # creates page
        customisationPg = Window(loginPg, title = "Customisation Page")
        
        # view profile
        profileWin = Window(loginPg, title = "Profile")
        profileWin.hide()

        def  changeBg():
            profileWin.bg = bgCombo.value

        def returnCust():
            customisationPg.hide()
            profilesPg.show()
        ########################################################################
        ########################## profile #####################################
        #######################################################################
        def profile():
            profileWin.show()
            customisationPg.hide()
            def deleteProf():
                    message1.destroy()
                    message2.destroy()
                    message3.destroy()
                    message4.destroy()
                    placeHolder0.destroy()
                    profilePic.destroy()
                    placeHolder1.destroy()
                    returnBtn.destroy()

                    returnProf()
                    
            def displayNameVal():
                    displayName = displayNameTB.value
                    return displayName

            #def NewDisplayName():
                    #print message and new display name
                    
                    
            def bioVal():
                    bio = bioTB.value
                    return bio            

            #def newBio():
                    # add new bio and display
                    

            def returnProf():
                    profileWin.hide()
                    customisationPg.show()
                    
            message1 = Text(profileWin, text = "Your display name is:")
            newDisplayName = displayNameVal()
            message2 = Text(profileWin, text = newDisplayName)

            
            message3 = Text(profileWin, text = "Your new bio is")
            newBio = bioVal()
            message4 = Text(profileWin, text = newBio)

            # creates a blank gap 
            placeHolder0 = Text(profileWin)
            
            #picture
            profilePic = Picture(profileWin, image = "profilePic.png")
            
            # creates a blank gap 
            placeHolder1 = Text(profileWin)
            
            # return to customisation
            returnBtn = PushButton(profileWin, text = "return", command = deleteProf, align = "top", width = "fill")
            
        #########################################################################

        # creates a blank gap 
        placeHolder0 = Text(customisationPg)
            
        #box to contain it all
        chngeDetBox = Box(customisationPg, width = "fill", align = "top")
            
        # display name text box 
        displayName = Text(chngeDetBox, text = "Enter your display name", align = "top")
        displayNameTB = TextBox(chngeDetBox, width = "40", align = "top")

        # bio text box
        bio = Text(chngeDetBox, text = "Enter your bio", align = "top")
        bioTB = TextBox(chngeDetBox, width = "40", align = "top")        

        # creates a blank gap 
        placeHolder1 = Text(chngeDetBox)
            
        # view profile btn
        viewProfileBtn = PushButton(chngeDetBox, text = "View Profile", command =  profile, align = "left", width = "fill")

        # select a background colour
        colourMessage = Text(chngeDetBox, text = "select your background colour", align = "top")
        colors = ["grey", "white", "red", "green", "blue"]
        bgCombo = Combo(chngeDetBox, options = colors, selected = profileWin.bg, command = changeBg)

        ###################################################################################
        
        # creates a blank gap 
        placeHolder2 = Text(customisationPg)

        returnBtn = PushButton(customisationPg, text = "return", command = returnCust, align = "top", width = "fill")
        
    def details():
        profilesPg.hide()
        ###################################################################################
        def newDetails():
            newDetWin.show()

            def deleteDet():
                message1.destroy()
                message2.destroy()
                message3.destroy()
                message4.destroy()
                returnBtn.destroy()
                
                newDetWin.hide()

            def emailVal():
                emailAdd = emailTB.value
                return emailAdd

            #def NewEmail():
                

            def passwordVal():
                newPass = passwordTB.value
                return newPass

            #def NewPassword():
                

            message1 = Text(newDetWin, text = "Your new email is:")
            emailAdd = emailVal()
            message2 = Text(newDetWin, text = emailAdd)

            message3 = Text(newDetWin, text = "Your new password is:")
            newPass = passwordVal()
            message4 = Text(newDetWin, text = newPass)

            returnBtn = PushButton(newDetWin, text="Return", align="top", command=deleteDet)

        def returnDet():
            detailsPg.hide()
            profilesPg.show()
        ###################################################################################
        
        detailsPg = Window(loginPg, title = "Details Page")

        # view new details
        newDetWin = Window(loginPg, title = "New details Page")
        newDetWin.hide()
       
        # load current details

        # change email
        emailTxt = Text(detailsPg, text = "Type your new email address here", align = "top")
        emailTB = TextBox(detailsPg, width = "40", align = "top")

        # change Password
        passwordTxt = Text(detailsPg, text = "Enter your password here", align = "top")
        passwordTB = TextBox(detailsPg, width = "40", align = "top")

        # view new details
        viewDetailsBtn = PushButton(detailsPg, text = "View your new details", command = newDetails , align = "left", width = "fill")

        # return button
        returnBtn = PushButton(detailsPg, text = "return", command = returnDet, align = "left", width = "fill")
        
        
    def notifications():
        def returnNot():
            notificationsPg.hide()
            profilesPg.show()
    
        notificationsPg = Window(loginPg, title = "Notifications Page")
        
        # creates a blank gap 
        placeHolder0 = Text(profilesPg)

        # notifications tick box
        notificationsOn = CheckBox(notificationsPg, text = "notifications On?")

        #picture
        # reference this
        notificationsPic = Picture(notificationsPg, image = "notifications.png")

        # return button
        returnBtn = PushButton(notificationsPg, text = "return", command = returnNot, align = "left", width = "fill")


    profilesPg = Window(loginPg, title = "Profiles Page")

    ################################################################################
    # creates a blank gap
    placeHolder0 = Text(profilesPg)

    # title of page
    profilePgTxt = Text(profilesPg, text = "Edit Your Profile")

    # Box to hold buttons 
    Box1 = Box(profilesPg, width = "fill", align = "left")

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
    ############################################################################################################

    ############################################################################################################
    # Box2
    Box2 = Box(profilesPg, width = "fill", align = "top")
    
    # empty box to create a space to the left of the buttons 
    pH3 = Box(Box2, width = "fill", align = "left")
    
    # return button
    returnBtn = PushButton(Box2, text = "return", command = returnHome, align = "left", width = "fill")

    # empty box to create a space to the left of the buttons 
    pH4 = Box(Box2, width = "fill", align = "left")
    
    ################################################################################

####################################################################################
############################ minigames #############################################
####################################################################################
def Minigames():
    minigamePg = Window(loginPg, title = "Minigames")

    minigamesTxt = Text(minigamePg, text = "Minigames")
####################################################################################

####################################################################################
############################## User Login ##########################################
####################################################################################
    
#titles the page and colour
loginPg = App(title="KomodoHub")

# Main title of app
message = Text(loginPg, text="Komodo Hub")

# creates a blank gap 
placeHolder1 = Text(loginPg)

#username textbox
email = Text(loginPg, text="Enter your Username")
usernameTB = TextBox(loginPg, width = "40")

#password textbox
password = Text(loginPg, text="Enter your Password")
passwordTB = TextBox(loginPg, width = "40")

# creates a blank gap 
placeHolder2 = Text(loginPg)

##########################################################################
# A box to hold all the buttons 
loginPgBtn = Box(loginPg, width = "fill", align = "top")

# empty box to create a space to the left of the buttons 
pH1 = Box(loginPgBtn, width = "fill", align = "left")

captchaCorrect = captchaGeneration()
captchaPic = Picture(loginPgBtn, image = "CAPTCHA.png", align = "top")

captchaTB = TextBox(loginPgBtn, width = "40", align = "top")

# select a background colour
accoutTypeMsg = Text(loginPg, text = "select your account type", align = "top")
accountTyp = ["student", "teacher", "business", "personal", "school"]
acCCombo = Combo(loginPgBtn, options = accountTyp, selected = loginPgBtn)

# Submits the username and password in the textboxes 
continueButton = PushButton(loginPgBtn, text = "Continue", command = userLogin_username_password_dbUsername_dbPassword, args=[captchaCorrect], align = "left", width = "fill")

# create account button
CreateAccBtn = PushButton(loginPgBtn, text = "Create Account", command =  createAccount, align = "left", width = "fill")

homeBtn = PushButton(loginPgBtn, text = "home", command =  homepage, align = "left", width = "fill")
# empty box to create a space to the right of the buttons
pH2 = Box(loginPgBtn, width = "fill", align = "left")
###########################################################################



loginPg.display()
