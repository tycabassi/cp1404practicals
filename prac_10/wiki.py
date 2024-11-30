import wikipedia

user_search = input("Enter a Search phrase or Page title: ")
while user_search != "":
    page_details = wikipedia.search(user_search)
    print(page_details)
    user_search = input("Enter a Search phrase or Page title: ")
print("Thanks for using our cool Python search")
