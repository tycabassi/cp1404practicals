def main():
    password = get_password()
    print_password(password)


def print_password(password):
    """Print stars based on the length of the password"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """Get password ensuring its valid"""
    password = input("Enter a password: ")
    while len(password) < 10:
        print("Invalid enter password again!")
        password = input("Enter a password: ")
    return password


main()
