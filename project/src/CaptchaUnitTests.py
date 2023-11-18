import unittest
from CaptchaFunction import captchaGeneration

class CaptchaTests(unittest.TestCase):
    def test_captcha_generation_returns_numeric(self):
        captchaResult = captchaGeneration()
        self.assertTrue(captchaResult.isnumeric, "Captcha is not numeric")

    def test_captcha_generation_contains_6_numbers(self):
        captchaResult = captchaGeneration()
        self.assertEqual(len(captchaResult), 6, "Captcha does not contain 6 numbers")
