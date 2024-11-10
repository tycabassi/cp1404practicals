"""Estimated time: 1hr 45
Actual time: 15 mins"""

from prac_07.project import Project
import datetime

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project"
        "\n(U)pdate project\n(Q)uit")

DEFAULT_FILENAME = "projects.txt"


def main():
    print(MENU)
    choice = input("Enter a choice: ").lower()
    while choice != "q":
        if choice == "l":
            file_name = input("Enter the file name we want to load the project from: ")
            while file_name != "projects.txt":
                file_name = input("Enter the file name we want to load the project from: ")
            display_projects()
        elif choice == "s":
            pass
        elif choice == "d":
            display_projects()
        elif choice == "f":
            pass
        elif choice == "a":
            new_project = add_new_project()
            print(new_project)
            with open("projects.txt", "a") as out_file:
                out_file.write(str(new_project))
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
    projects = []
    with open(DEFAULT_FILENAME) as in_file:
        in_file.readline()
        for i, line in enumerate(in_file):
            projects.append(line)
            print((projects[i]).strip("\n"))


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


# def save_projects():

main()
# Update project completion

# Sort projects by date using lt method, shows all projects after x date
