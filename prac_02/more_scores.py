import random


def main():
    number_of_scores = int(input("How many scores do you want to generate: "))
    in_file = open("results.txt", "w")
    for i in range(number_of_scores):
        random_score = random.randint(1, 100)
        score = determine_score(random_score)
        in_file.write(f"{random_score} is {score}\n")
    in_file.close()


def determine_score(random_score):
    if random_score < 0 or random_score > 100:
        return "Invalid"
    elif random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
