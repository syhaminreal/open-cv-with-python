import random
user_database = {
    "Raja": "ram",
    "user2": "securepass",
   }
def generate_otp():
    otp = ""
    for _ in range(6):  # 6-digit OTP
        otp += str(random.randint(0, 9))
    return otp
def authenticate_with_2fa(username, password, otp):
    if username in user_database and user_database[username] == password:
        if otp == generated_otp:
            return True
    return False
username = input("Enter your username: ")
password = input("Enter your password: ")
generated_otp = generate_otp()
print("Generated OTP:", generated_otp)
entered_otp = input("Enter the OTP: ")
if authenticate_with_2fa(username, password, entered_otp):
    print("Authentication successful!")
else:
    print("Authentication failed.")