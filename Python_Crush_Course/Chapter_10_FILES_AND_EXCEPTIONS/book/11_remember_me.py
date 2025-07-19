import json

username = input("What is your name? ")
password = input("What is your password? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump({"username": username, "password": password}, f_obj)
    print(f"We'll remember you when you come back, {username}!")