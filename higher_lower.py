from data import data
from art import *
import random
from os import system
system('clear')
print(logo)

def choose_random(rand_data):
    return random.choice(rand_data)

score = 0

def compare(player_choise, first_data, second_data):
    
    if player_choise == "a" or player_choise == "A":
        if int(first_data['follower_count']) > int(second_data['follower_count']):
            return True
        else:
            return False

    elif player_choise == "b" or player_choise == "B":
        if int(second_data['follower_count']) > int(first_data['follower_count']):
            return True
        else:
            return False
    else:
        return False


def choose_player(score):
    end_game = False

    while not end_game:
        random1 = choose_random(data)
        random2 = choose_random(data)

        if random1 == random2:
            choose_player(score)

        print(f"Compare A: {random1['name']}, {random1['description']}, from  {random1['country']}.")
        print(vs)
        print(f"Compare B: {random2['name']}, {random2['description']}, from  {random2['country']}.")
        
        player_choise = input("Who has more followers? Type 'A' or 'B': ")
        result = compare(player_choise=player_choise, first_data=random1, second_data = random2)

        if result == True:
            score += 1
            system('clear')
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            system('clear')
            print(logo)
            print(f"You're wrong! Your final score is {score}")
            end_game = True

choose_player(score)


