COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Aqua": "#00ffff", "Ash Grey": "#b2beb5", "Baby Blue": "#89cff0",
                  "Brick Red": "#cb4154", "Bright Green": "#66ff00", "Bronze": "#cd7f32", "Bulgarian Rose": "#480607",
                  "Caribbean Green": "#00cc99", "Electric Blue": "#7df9ff"}

colour = input("Enter a colour: ")
while colour != "":
    if colour in COLOUR_TO_CODE:
        print(COLOUR_TO_CODE[colour])
    else:
        print("Invalid")
    colour = input("Enter a colour: ")
print("Thank you for picking a colour")

