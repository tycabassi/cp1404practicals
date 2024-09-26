MENU = """(G)et a valid score(must be 0-100 inclusive)
(P)rint result
(S)how stars (This should print as many stars as the score)
(Q)uit"""



def main():
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>: ").upper()


main()