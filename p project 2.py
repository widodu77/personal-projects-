#programme that makes you play rock paper scissors agaisnt the computer 

import random

Win = 3
user_points = 0
comp_points = 0

def u_hand():
    return input("What hand do you want to play? ")

def computer_hand():
    possible_hands = ["rock", "paper", "scissor"]
    return random.choice(possible_hands)

def determine_winner(comp_hand, user_hand):
    global comp_points, user_points
    if user_hand == comp_hand:
        print("It's a draw")
    elif (
        (user_hand == "rock" and comp_hand == "scissor") or
        (user_hand == "paper" and comp_hand == "rock") or
        (user_hand == "scissor" and comp_hand == "paper")
    ):
        user_points += 1
        print(f"You won! The score is now {comp_points} for the computer and {user_points} for you.")
    else:
        comp_points += 1
        print(f"The computer won. The score is now {comp_points} for the computer and {user_points} for you.")

def main():
    global comp_points, user_points

    while user_points < Win and comp_points < Win:
        user_hand = u_hand()
        comp_hand = computer_hand()
        determine_winner(comp_hand, user_hand)

    if user_points == Win:
        print("You won!")
    else:
        print("You lost :(")


main()




         
    
        











#rock>scissor scissor>paper paper>rock 
# if the two are the same it gives draw anf the points stay the same 
