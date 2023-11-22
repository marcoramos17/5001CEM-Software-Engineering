import pyotp
import qrcode
import qrcode.image.svg
import database as db
import os
rootDir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
os.environ['path'] += ";" + rootDir + r"\src\dlls"
import cairosvg





# https://pyauth.github.io/pyotp/#module-pyotp
# Documentation above is key

def userAccountGeneration(accountName):
    try: # Tries this section to see if error occurs which means there is no secret for the account
        if db.db_get_user_secret(accountName) == None:
            pass
    except TypeError: # If there is no secret, this code generates it while excepting the occured error
        RNGSecretGeneration = pyotp.random_base32()
        RNGSecretTOTP = pyotp.TOTP(RNGSecretGeneration) 
        db.db_update_user_secret(accountName, RNGSecretTOTP)
        qrCodeImage = qrcode.make(pyotp.totp.TOTP(RNGSecretGeneration).provisioning_uri(name=accountName, issuer_name="Komodo Hub"), image_factory=qrcode.image.svg.SvgImage)
        with open('qrcode.svg', 'wb') as qr:
            qrCodeImage.save(qr)
        cairosvg.svg2png(url="qrcode.svg", write_to="output.png")
    else:
        print("Secret is already generated")
def userAccountCheck(accountName):
    RNGSecretTOTP = db.db_get_user_secret(accountName)
    checkLoop = True
    while (checkLoop == True):
        check = input("Enter code\n")
        if check.replace(" ", "") == RNGSecretTOTP.now():
            print("Code is acceptable, your account has been verified\n")
            checkLoop = False
        else:
            print("Code is not accepted, please try again\n")

userAccountGeneration("EricProf582874") # Test value
#userAccountCheck("JimmCric582874") # Test value
