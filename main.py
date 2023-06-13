import random
from art import logo, vs
from game_data import data
from replit import clear

def game_picks():
    """randomly chooses A and/or B from the game data"""
    return random.choice(data)

def compare(first_pick, next_pick):
    """determines whether A or B is the correct choice"""
    high_follower = ""
    pick_a = first_pick['follower_count']
    pick_b = next_pick['follower_count']
    if pick_a > pick_b:
        high_follower += "a"
        return high_follower
    elif pick_a < pick_b:
        high_follower += "b"
        return high_follower

def game_play():
    first_pick = game_picks()
    score = 0
    print(logo)
    game_over = False
    while not game_over:
        print(f"Compare A: {first_pick['name']}, a {first_pick['description']}, from {first_pick['country']}.")
        print (vs)
        next_pick = game_picks()
        if first_pick == next_pick:
            next_pick = game_picks()
        print(f"Against B: {next_pick['name']}, a {next_pick['description']}, from {next_pick['country']}.")
        choice = input("Who has more followers?  Choose 'A' or 'B'. ").lower()
        high_follower = compare(first_pick, next_pick)
        if choice == high_follower:
            clear()
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}.")
            if choice and high_follower == 'b':
                first_pick = next_pick
        else:
            game_over = True
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Your final score is {score}.")
    
game_play()



