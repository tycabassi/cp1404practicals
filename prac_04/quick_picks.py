import random

NUMBER_OF_COLUMNS = 6

number_of_quick_picks = int(input("Enter the number of quick picks you would like to generate"))
for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(NUMBER_OF_COLUMNS):
        quick_pick = random.randint(1, 45)
        while quick_pick in quick_picks:
            quick_pick = random.randint(1, 45)
        quick_picks.append(quick_pick)
    print(" ".join(f"{quick_pick:2}" for quick_pick in quick_picks))

