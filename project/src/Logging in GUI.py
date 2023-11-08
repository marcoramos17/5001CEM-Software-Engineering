import time
from guizero import *

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

    homePg = Window(loginPg, title = "Authentication Page")
    
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

# Submits the username and password in the textboxes 
continueButton = PushButton(loginPgBtn, text = "Continue", command = userLogin_username_password_dbUsername_dbPassword, align = "left", width = "fill")

# create account button
CreateAccBtn = PushButton(loginPgBtn, text = "Create Account", command =  createAccount, align = "left", width = "fill")

# account authentication
authenticateBtn = PushButton(loginPgBtn, text = "Authenticate Account", command =  createAccount, align = "left", width = "fill")

# empty box to create a space to the right of the buttons
pH2 = Box(loginPgBtn, width = "fill", align = "left")
###########################################################################

loginPg.display()
