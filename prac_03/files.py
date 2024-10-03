#1.
name = input("Enter your name: ")
out_file = open(f"{name}.txt", "w")
out_file.write(name)
out_file.close()