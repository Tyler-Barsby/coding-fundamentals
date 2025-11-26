library = {
    "J. R. R. Tolkein" : [
        "The Hobbit",
        "The Lord Of The Rings",
        "The Fellowship Of The Ring"
        ], 
    "Michael Morpurgo": [
        "War Horse" ,
        "Private Peaceful",
        "Born To Run"
        ], 
    "J. K. Rowling": [
        "Harry Potter: The Philosophers Stone",
        "Harry Potter: The Chanber Of Secrets",
        "Harry Potter: The Prisoner Of Azkaban"
        ]
    }

author = str(input(f"Select an Author from this list {list(library.keys())}: "))

if author in library:
    print(f" These are {author} books:\n{str(library[author])}")
else:
    print(f"{author} is not in the list")


