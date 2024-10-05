MAX_COLUMNS = 10
MIN_COLUMNS = 2
LOWER = 33
UPPER = 127

character = input("Enter a Character: ")
ascii_value = ord(character)
print(f"The ASCII code for {character} is {ascii_value}")
number = int(input("Enter a Number: "))
while number < LOWER or number > UPPER:
    print(f"Please enter a number between {LOWER} and {UPPER}")
    number = int(input("Enter a Number: "))
character_value = chr(number)
print(f"The character for {number} is {character_value}")

# Single Column
# for value in range(LOWER, UPPER + 1):
#     print(f"{value:3} {chr(value):.4}")

number_of_columns = int(input("Enter number of columns: "))
while number_of_columns < MIN_COLUMNS or number_of_columns > MAX_COLUMNS:
    print(f"Please use a value between {MIN_COLUMNS} and {MAX_COLUMNS}")
    number_of_columns = int(input("Enter number of columns: "))
# calculate the range of values and the number of full rows
number_of_values = UPPER - LOWER + 1
number_of_rows = number_of_values // number_of_columns

print("Version 1: Horizontal then vertical ordering")
# iterate through the full rows first, incrementing by 1
value = LOWER
for row_number in range(number_of_rows):
    for column_number in range(number_of_columns):
        print(f"{value:6} {chr(value):>2}", end="")
        value += 1
    print()
