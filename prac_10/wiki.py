import wikipedia

page_title = input("Enter page title: ")
while page_title != "":
    try:
        page_summary = wikipedia.summary(page_title)
        wikipedia_page = wikipedia.page(page_title)
        print(f"{page_title}\n{page_summary}\n{wikipedia_page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print(e)
    page_title = input("Enter a Search phrase or Page title: ")
print("Thanks for using our cool Wikipedia search")
