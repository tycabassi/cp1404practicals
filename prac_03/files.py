# 1.
name = input("Enter your name: ")
out_file = open(f"{name}.txt", "w")
out_file.write(name)
out_file.close()


# 2.
name = input("Enter your name: ")
in_file = open(f"{name}.txt", "r")
print(f"Hello, {name}!")
in_file.close()

# 3.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(f"Sum of the first two lines is {number1 + number2}")
in_file.close()

sum_of_numbers = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    sum_of_numbers += number
print(f"Sum of the numbers is {sum_of_numbers}")
in_file.close()
