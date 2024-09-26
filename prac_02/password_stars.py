password = input("Enter a password: ")
while len(password) < 10:
    print("Invalid enter password again!")
    password = input("Enter a password: ")
for i in range(len(password)):
    print("*", end="")