# Password Generator
# Task 3 - CodSoft Python Internship

import random
import string

class PasswordGenerator:

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for _ in range(length):
            password += random.choice(characters)

        return password

    def menu(self):
        print("\n*****Password Generator*****")
        print("\n1. Generate Password")
        print("\n2. Exit")


generator = PasswordGenerator()

while True:
    generator.menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        length = int(input("Enter the length of password: "))

        if length < 8:
            print("Password length should be at least 8 characters.")
        else:
            password = generator.generate_password(length)
            print("Generated Password:", password)
    elif choice == '2':
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice! Try again.")
