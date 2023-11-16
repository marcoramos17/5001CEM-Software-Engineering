from captcha.image import ImageCaptcha
import random
# Captcha documentation in below link
# https://pypi.org/project/captcha/
def captcha():
    image = ImageCaptcha(width = 400, height = 200)
    x = str(random.getrandbits(128)) # Random number generation for captcha image
    captchaString = x[0:6]
    image.write(captchaString, 'CAPTCHA.png') # Captcha image generation with value from captchaString variable
    captchaInput = input("What is the string above?\nPlease be capital specific\n") # If statement only to simulate user input on the front end
    if captchaInput == captchaString: 
        print("Captcha successful")
    else:
        print("Captcha unsuccessful")

captcha()

