import wikipedia

wiki_title = input("Insert a wikipedia title to search up: ")
while wiki_title != "":
    try:
        wiki_page = wikipedia.page(wiki_title)
        print("{}:".format(wiki_page.title))
        print(wikipedia.summary(wiki_title))
        print("Retrieved from: {}".format(wiki_page.url))
        wiki_title = input("Insert a wikipedia title to search up: ")
    except wikipedia.exceptions.DisambiguationError:
        print("Error: Multiple pages have this title, enter a more specific title")
        wiki_title = input("Insert a wikipedia title to search up: ")