"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    grade = determine_score(score)
    print(f"The user's score is {score} which is {grade}")
    random_score = random.randint(1, 100)
    random_grade = determine_score(random_score)
    print(f"The random's score is {random_score} which is {random_grade}")


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
