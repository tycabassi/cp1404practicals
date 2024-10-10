# 1. Basic List Operations
numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    i += 1
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")


#2.Woefully inadeuqate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input('Enter a username:')
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied!")