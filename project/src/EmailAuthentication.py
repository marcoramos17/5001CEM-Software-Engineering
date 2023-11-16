import smtplib
import ssl 
import random

# https://realpython.com/python-send-email/
# Documention above is key

def emailAuthentication(userEmail):
    x = str(random.getrandbits(128))
    code = x[0:6]
    message = """Subject: Verification Code\n
    Please use the following code to verify your login:\n
    {}""".format(code)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls(context=ssl.create_default_context())
        server.login("KomodoHub@outlook.com", "Hub@Komodo!")
        server.sendmail("KomodoHub@outlook.com", userEmail, message)
    
    checkLoop = True
    while (checkLoop == True):
        inputCode = input("Please enter the code sent to your email, if you are unable to find the code. Please check the spam folder\n")
        if inputCode == code:
            print("Code is acceptable, your account has been verified\n")
            checkLoop = False
        else:
            print("Code is not accepted, please try again\n")

emailAuthentication("jack.mcgr0@gmail.com")

