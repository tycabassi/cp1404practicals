"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
        result = int(input("Enter a valid integer: "))
print("Valid result is:", result)

# A ValueError would occur if i was to type in say "w" or a symbol instead of an integer
# A ZeroDivisionError wouldn't occur unless we try to divide a number by result variable when the result = 0
# To avoid a ZeroDivisionError an error checking of the result value will be needed the same as for the ValueError
