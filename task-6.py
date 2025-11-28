def catchWord():
    try:
        word = str(input("Please enter a word: "))
        return word
    except ValueError as e:
        print(f"[ERROR]: {e}")
        

def countVowels(word):
    vowels = ["a","e","i","o","u"]
    count = 0
    
    vowels_in_word = []
    
    for letter in word:
        if letter in vowels:
            count +=1
            vowels_in_word.append(letter)
    
    print(f"There are {count} vowels in your word: {word}\n")
    print(f"The vowels in your word are {vowels_in_word}")

def main():
    countVowels(catchWord())
    
main()