# coding-fundamentals

## task-1.py
- Introduction to Dictionaries and lists. 
- I have used a menu type selection to print out the authors in the library
- Users select an author via number and a list or their known books is printed

- ### Potential Improvements:
    - Use contains rather than in to create a character search
    - Paginate the menu (max 10 per page)
    - Alphabetize the list
    - Allow searching on starting character
        - reduce list length to names starting with character

-----

## task-2.py
- Introduction to creating data structures
- Using a dictionary I have created a JSON style data structure which stores details about the books of an author

- ### Potential Improvements
    - Use Unique IDs fpr author positions
    - Use strings consistently and use casting when grabbing the item if a calculation is needed

-----

## task-3.py
- Weight Conversion
- Users select either Kgs or Lbs from a numbered list to convert to
- And a conversion algorithm calculates the weight from Kgs to Lbs for example
    - 10Kg * 2.20462 = 22.046Lbs

- ### Potential Improvements:
    - Allow users to select starting unit
    - Allow other units to be selected e.g. grams, tonnes, etc 

-----

## task-4.py
- Introduction to Loop structures and List Comprehensions.
- Solves a specific input/output problem using four distinct methods: While Loop, For Loop, Standard List Comprehension, and a One-line List Comprehension.
- Iterates 5 times to collect user input and prints a concatenated f-string response.

- ### Potential Improvements:
    - Allow the user to specify the loop count (n iterations) rather than hardcoding to 5
    - Add input validation to prevent empty string entries
    - Format the input names (e.g. use .title()) to ensure proper capitalization
    - Store the resulting strings in a list or file for later use rather than just printing immediately

-----

## task-5.py
- Comprehensive exercises on List manipulation and built-in methods.
- Performs operations such as calculating length, looping through items, modifying values, filtering data (removing outliers), and sorting.
- Counts specific occurrences within a defined age range.

- ### Potential Improvements:
    - Use list comprehensions for more concise filtering and modification
    - Use in-place sorting (ages.sort()) to modify the original list directly

-----

## task-6.py
- Introduction to string traversal and logical operators.
- Iterates through a user-inputted string character by character.
- Uses a defined list of vowels and the in operator to identify, count, and collect vowels found in the word.
- Includes a try/except block to handle potential input errors and ensure the value is iterable.

- ### Potential Improvements:
    - Convert the input to lowercase to ensure capitalized vowels are also counted (case-insensitivity)
    - Use a dictionary to track the frequency of each specific vowel found (e.g., 2 'a's, 1 'e')
    - Add specific validation (like .isalpha()) to reject strings containing numbers or symbols