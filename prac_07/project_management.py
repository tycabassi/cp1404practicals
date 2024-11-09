"""Estimated time: 1hr 45
Actual time: 15 mins"""
from prac_07.project import Project
import datetime

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project"
        "\n(U)pdate project\n(Q)uit")


def main():
    print(MENU)
    choice = input("Enter a choice: ").lower()
    while choice != "q":
        if choice == "l":
            pass
        elif choice == "s":
            pass
        elif choice == "d":
            display_projects()
        elif choice == "f":
            pass
        elif choice == "a":
            print(add_new_project)
        elif choice == "u":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter a choice: ").lower()


# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
#
# project = Project("Dishes", date_string, 7, 340, 9)
# print(project)


#



def display_projects():
    in_file = open("projects.txt", "r")
    for line in in_file:
        parts = line.split()
        print(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))


# Add new project function
def add_new_project():
    name = input("Name: ")
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = float(input("Priority: "))
    estimate = input("Estimate: $")
    completion = int(input("Completion:"))
    new_project = Project(name, date, priority, estimate, completion)
    return new_project


main()
# Update project completion

# Sort projects by date using lt method, shows all projects after x date
