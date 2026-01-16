# Rock Paper Scissors Game
# Task 2 - CodSoft Python Internship

import random
class RockPaperScissors:

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computerchoice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def decide_winner(self, user, computer):
        if user == computer:
            return "Tie"
        elif (
            (user == 'rock' and computer == 'scissors') or
            (user == 'scissors' and computer == 'paper') or
            (user == 'paper' and computer == 'rock')
        ):
            self.user_score += 1
            return "You Win!"
        else:
            self.computer_score += 1
            return "Computer Wins!"

    def menu(self):
        print("\n*****Rock Paper Scissors*****")
        print("\n1. Rock")
        print("\n2. Paper")
        print("\n3. Scissors")
        print("\n4. Exit")

game = RockPaperScissors()

while True:
    game.menu()
    choice = input("Enter your choice: ")

    if choice == '4':
        print("Final Score:")
        print("You:", game.user_score)
        print("Computer:", game.computer_score)
        print("Game Over!")
        break

    options = {'1': 'rock', '2': 'paper', '3': 'scissors'}

    if choice in options:
        user_choice = options[choice]
        computer_choice = game.get_computerchoice()

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = game.decide_winner(user_choice, computer_choice)
        print("Result:", result)
    else:
        print("Invalid choice!! Try again...")
