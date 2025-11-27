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

# author = str(input(f"Select an Author from this list {list(library.keys())}:"))

# if author in library:
#     print(f" These are {author} books:\n{str(library[author])}")
# else:
#     print(f"{author} is not in the list")

authors = list(library.keys())

print("--- Library Menu ---")
for index, author in enumerate(authors, start=1):
    print(f"{index}. {author}")
    
try:
    selection = int(input("Please select an author by number: "))
    
    if 1 <= selection <= len(authors):
        selected_author = authors[selection - 1]
        
        print(f"\n--- Books by {selected_author} ---")
        for book in library[selected_author]:
            print(f"- {book}")
    else:
            print("Error: Please select a valid number from the menu.")

except ValueError:
    print("Error: Invalid input. Please enter a number.")
