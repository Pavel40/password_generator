#!/usr/bin/python3
import string
import random

class Generator():
    #Password generator class
    def __init__(self):
        self.characters = { #Characters dictionary
            'normal_characters': string.ascii_letters,
            'numbers': [i for i in range(10)],
            'special_characters': string.punctuation
        }

    def generate_password(self, password_type, password_length):
        #Returns password generated according to the arguments
        password = ''
        for _ in range(password_length):
            usable_characters = []
            for i in password_type:
                usable_characters.extend(self.characters[i])
            password += str(random.choice(usable_characters))
        return password

class UserInterface():

    def get_number(self, message):
        #Asks user for number until the user writes it down
        while True:
            try:
                number = input(message)
                number = int(number)
                return number
            except ValueError:
                print("Please write down number.")

    def user_agree(self, message):
        #Asks user if he/she agrees with something
        while True:
            answer = input(message)
            if answer in ['y', 'Y', 'Yes', 'yes', 'YES']:
                return True
            elif answer in ['n', 'N', 'No', 'no', 'NO']:
                return False
            else:
                print("Please write down yes or no.")

    def greet_user(self):
        print("Dear user, welcome to my password generator!")

    def say_goodbye(self):
        print("See you next time!")

generator = Generator()
ui = UserInterface()
program_running = True

ui.greet_user()

while program_running:
    #The main loop, runs until user quits

    password_quantity = ui.get_number('How many passwords to generate: ')
    password_length = ui.get_number('How long passwords to generate: ')

    #Password details
    password_type = []
    if ui.user_agree('Can the password include normal letters?\ny/n: '):
        password_type.append('normal_characters')
    if ui.user_agree('Can the password include numbers?\ny/n: '):
        password_type.append('numbers')
    if ui.user_agree('Can the password include special characters?\ny/n: '):
        password_type.append('special_characters')

    #Generating each password
    for _ in range(password_quantity):
        password = generator.generate_password(password_type, password_length)
        print(password)

    program_running = ui.user_agree("Do you want to generate another password(s)?\ny/n: ")    

ui.say_goodbye()