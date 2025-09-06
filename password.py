user_database = {
    "sabin": "bhurtel",
    "rajaram": "everest",
    # Add more user entries here
}
def authenticate(username, password):
    if username in user_database and user_database[username] == password:
        return True
    return False
username = input("Enter your username: ")
password = input("Enter your password: ")
if authenticate(username, password):
    print("Authentication successful!")
else:
    print("Authentication failed.")