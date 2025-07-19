import json

username = input("What is your name? ")
password = input("What is your password? ")
print('\n\n')

filename = 'username.json'
with open(filename) as f_obj:
    username_and_password = json.load(f_obj)
    
if username_and_password['username'] == username and username_and_password['password'] == password:
    print(f"Welcome back, {username}!")
else:
    print("Username or password is incorrect. Please try again.")