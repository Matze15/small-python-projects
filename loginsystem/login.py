import json
import os
import time

def clear_console():
    os.system('clear')

def write_down():
    json.dump(userdata, open('userdata.json', 'w'), indent = 4)

userdata = json.load(open('userdata.json'))

def username_taken(name):
    taken = False
    for i in range(len(userdata)):
        if userdata[i]['username'] == name:
            taken = True
            break
    return taken

def correct(name, passwd):
    correct = False
    for i in range(len(userdata)):
        if userdata[i]['username'] == name and userdata[i]['password'] == passwd:
            correct = True
            break
    return correct

def register_or_login():
    rol = input('Do you want to register (r) or login (l)? ')
    if rol == 'r' or rol == 'l':
        return rol
    else:
        print('Invalid input. Type r to register or l to login. Then hit return.')
        register_or_login()

def register():
    clear_console()
    user_information = {'username': '', 'password': ''}
    print('Register\nCreate an account by setting a username and a password.')
    def ask_for_username():
        username = input('Username: ')
        if username_taken(username):
            print('This username is already taken!')
            ask_for_username()
        else:
            user_information['username'] = username

    def ask_for_password():
        password = input('Password: ')
        if len(password) < 8:
            print('This password is too insecure. Please choose a password that has at least 8 characters.')
            ask_for_password()
        else: user_information['password'] = password

    ask_for_username()
    ask_for_password()

    global userdata
    userdata.append(user_information)
    write_down()
    userdata = json.load(open('userdata.json'))
    print('Successfully registered')
    time.sleep(2)
    clear_console()
    login()

def login():
    clear_console()
    print('Login')
    given_username = input('Username: ')
    given_password = input('Password: ')

    if not correct(given_username, given_password):
        choice = input('Invalid username or password provided. Do you want to try again (l) or register (r)? ')
        if not(choice == 'r' or choice == 'l'):
            register_or_login()
        elif choice == 'r':
            register()
        else:
            login()
    else:
        clear_console()
        print('Logged in as', given_username)

r_o_l = register_or_login()
if r_o_l == 'r':
    register()
else:
    login()