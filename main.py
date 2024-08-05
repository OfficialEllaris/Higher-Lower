from random import choice

from replit import clear

from art import logo, vs
from game_data import data


def format_question(question):
    return f"{question['name']}, a {question['description']}, from {question['country']}."

def correct_answer(question_a, question_b):
    if question_a['follower_count'] > question_b['follower_count']:
        return "a"
    else:
        return "b"

print(logo)
user_score = 0
game_switch = True
question_b = choice(data)

while game_switch:
    question_a = question_b
    question_b = choice(data)

    while question_a == question_b:
        question_b = choice(data)

    print(f"Compare A: {format_question(question_a)}\n{vs}\nAgainst B: {format_question(question_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(logo)

    if user_guess == correct_answer(question_a, question_b):
        user_score += 1
        print(f"You're right! Current score: {user_score}.")
    else:
        game_switch = False
        print(f"Sorry, that's wrong. Final score: {user_score}")