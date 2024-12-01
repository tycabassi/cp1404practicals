import wikipedia

user_search = input("Enter a Search phrase or Page title: ")
while user_search != "":
    try:
        page_details = wikipedia.summary(user_search)
        print(page_details)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print(e)
    user_search = input("Enter a Search phrase or Page title: ")
print("Thanks for using our cool Wikipedia search")
