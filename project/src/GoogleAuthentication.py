import pyotp
import qrcode
import qrcode.image.svg
import database as db

# https://pyauth.github.io/pyotp/#module-pyotp
# Documentation above is key

def userAccountGeneration(accountName):
    if db.db_get_user_secret(accountName) == None:
        RNGSecretGeneration = pyotp.random_base32()
        RNGSecretTOTP = pyotp.TOTP(RNGSecretGeneration) 
        db.db_update_user_secret(accountName, RNGSecretTOTP)
        qrCodeImage = qrcode.make(pyotp.totp.TOTP(RNGSecretGeneration).provisioning_uri(name=accountName, issuer_name="Komodo Hub"), image_factory=qrcode.image.svg.SvgImage)
        with open('qrcode.svg', 'wb') as qr:
            qrCodeImage.save(qr)
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

userAccountGeneration("JimmCric582874")
userAccountCheck("JimmCric582874")
