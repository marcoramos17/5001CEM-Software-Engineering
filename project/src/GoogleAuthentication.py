import pyotp
import qrcode
import qrcode.image.svg

# https://pyauth.github.io/pyotp/#module-pyotp
# Documentation above is key
# There will need to be database implementation to save the account name and their related RNGSecretTOTP to check later on during log in


def userAccountCheck(accountName):
    RNGSecretGeneration = pyotp.random_base32()
    RNGSecretTOTP = pyotp.TOTP(RNGSecretGeneration) 
    # Database code needed to store the RNGSecretTOTP and related account name/user - WORK NEEDED
    # If statement for if the account name is in the database, then overwrite the RNGSecretTOTP variable
    qrCodeImage = qrcode.make(pyotp.totp.TOTP(RNGSecretGeneration).provisioning_uri(name=accountName, issuer_name="Komodo Hub"), image_factory=qrcode.image.svg.SvgImage)
    with open('qrcode.svg', 'wb') as qr:
        qrCodeImage.save(qr)
    checkLoop = True
    while (checkLoop == True):
        check = input("Enter code\n")
        if check.replace(" ", "") == RNGSecretTOTP.now():
            print("Code is acceptable, your account has been verified\n")
            checkLoop = False
        else:
            print("Code is not accepted, please try again\n")

userAccountCheck("Jack")
