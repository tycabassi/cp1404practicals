# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()



# c
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end='')




# d
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    i += 1
    print("*" * i)