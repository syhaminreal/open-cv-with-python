import random
def generate_captcha():
    captcha = ""
    for _ in range(6):  # 6-character CAPTCHA
        captcha += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return captcha
def verify_captcha(input_captcha, generated_captcha):
    return input_captcha == generated_captcha
generated_captcha = generate_captcha()
print("Generated CAPTCHA:", generated_captcha)
input_captcha = input("Enter the CAPTCHA: ")
if verify_captcha(input_captcha, generated_captcha):
    print("CAPTCHA verification successful!")
else:
    print("CAPTCHA verification failed.")