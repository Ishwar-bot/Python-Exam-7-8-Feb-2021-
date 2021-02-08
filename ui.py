import itertools as it
from os import name,system
def menu(menuList):
    "Display a indexed Menu of all the elments in iterable menuList"
    counter = it.count(1)
    for i in menuList:
        print(str(next(counter)) + ". " + i )
def clear(): 
    "clears the console/terminal."
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')
def loginMenu():
    "Displays a login menu and records username and password entered by an user. Returns username and password in tuple format"
    print("Enter account details \nEmail:")
    email = input()
    print("Password:")
    password = input()
    return (email,password)
def checkInt(n = float("inf")):
    "Checks whether a input given by a user is numerical and less than n. Makes user input again if constraints are not met."
    print("Enter a choice:")
    while True:
        temp = input()
        if temp.isnumeric():
            temp = int(temp)
            if temp <= n and temp > 0:
                clear()
                return temp
            else:
                print("Oops! Wrong input. Try again.")
        else:
            print("Oops! Wrong input. Try again.")
def dict_menu(dic):
    if dic:
        for key, value in dic.items():
            print(key, ". ", value, sep = "")
        while True:
            choice = int(input("Enter Choice:\n"))
            if choice in dic.keys():
                return choice
            else:
                print("Enter Valid choice.\n")
def go_back_menu():
    print("1.Go Back.")
    checkInt(1)
def quiz_menu(quiz_dict):
    for quiz_id, (quiz_name, topic, difficulty) in quiz_dict.items():
        print(quiz_id, quiz_name, "Topic:",topic, "Difficulty:", difficulty)
    while True:
        choice = int(input("Enter Choice:\n"))
        if choice in quiz_dict.keys():
            return choice
        else:
            print("Enter Valid choice.\n")