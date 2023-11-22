import os
from twilio.rest import Client
import random
# https://www.twilio.com/docs/usage/api
# Documentation above is key

def textAuthentication(clientNumber):
    account_sid = os.environ["Twilio_Account_SID"]
    auth_token = os.environ["Twilio_Auth_Token"]
    client = Client(account_sid, auth_token)
    x = str(random.getrandbits(128))
    code = x[0:6]
    message = client.messages \
        .create(
            body=code,
            from_="+447360494327",
            to=clientNumber
        )
    checkLoop = True
    while (checkLoop == True):
        inputCode = input("Please enter the code sent to your phone\n")
        if inputCode == code:
            print("Code is acceptable, your account has been verified\n")
            checkLoop = False
        else:
            print("Code is not accepted, please try again\n")

number = "+447395622465" # Just for testing, remove this since personal phone number
textAuthentication(number)