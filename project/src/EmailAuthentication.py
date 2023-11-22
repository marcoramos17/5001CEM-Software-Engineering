import smtplib
import ssl 
import random

# https://realpython.com/python-send-email/
# Documention above is key

def emailAuthentication(userEmail):

    x = str(random.getrandbits(128))
    codeGlo = x[0:6]
    messageGlo = """Subject: Verification Code\n
    Please use the following code to verify your login:\n
    {}""".format(codeGlo)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls(context=ssl.create_default_context())
        server.login("KomodoHub@outlook.com", "Hub@Komodo!")
        server.sendmail("KomodoHub@outlook.com", userEmail, messageGlo)


    
    
    

def checkCode(codePass):
    if codeGlo == codePass:
        print("TRUE")
    else:
        print("FaLse")


