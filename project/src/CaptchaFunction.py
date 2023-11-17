from captcha.image import ImageCaptcha
import random
# Captcha documentation in below link
# https://pypi.org/project/captcha/
def captchaGeneration():
    image = ImageCaptcha(width = 400, height = 200)
    x = str(random.getrandbits(128)) # Random number generation for captcha image
    captchaString = x[0:6]
    image.write(captchaString, 'CAPTCHA.png') # Captcha image generation with value from captchaString variable
    return captchaString

def captchaCheck(userValue, captchaString):
    if userValue == captchaString: 
        return True
    else:
        print("Wrong captcha")
#
