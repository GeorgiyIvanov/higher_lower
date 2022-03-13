#import art, data, and random module for choosing the data
from art import logo, vs
from game_data import data
from random import choice
import os

#creating a function for clearing the console
clear = lambda: os.system('cls')
clear()

#store the randomed data into two variables, check they are note equal
person_a = choice(data)
person_b = choice(data)


#create a variable for the score
score = 0

#print the logo, ask the player to compare the first person vs second one
print(logo)
while True:
    followers_a = person_a["follower_count"]
    followers_b = person_b["follower_count"]

    while person_a == person_b:
        person_b = choice(data)
        followers_b = person_b["follower_count"]
        
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
    
    if followers_a > followers_b:
        right_answer = "A"
    else:
        right_answer = "B"
        
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    while user_answer not in ['A', 'B']:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if user_answer == right_answer:
        clear()
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        person_a = person_b
        person_b = choice(data)
        continue
    else:
        clear()
        print(logo)
        print(f"Sorry that's wrong. Final score: {score}.")
        break
