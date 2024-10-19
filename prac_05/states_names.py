"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# state_code = input("Enter short state: ")
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ")

state_code = input("Enter short state: ").upper()
while state_code not in CODE_TO_NAME:
    try:
        state_code = input("Enter short state: ").upper()
        print(state_code, "is", CODE_TO_NAME[state_code])
    except ValueError:
        print("Invalid try again")
    except KeyError:
        print("Invalid short state")


for state_code, state in CODE_TO_NAME.items():
    print(f"{state_code} is {state}")
