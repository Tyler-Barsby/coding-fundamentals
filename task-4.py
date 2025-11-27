# TASK:
# loop to get 5 names as inputs + prints with "is awesome" added to it. 

# while loop
# for loop
# list comp
# STRETCH GOAL: list comp one line only! 

# WHILE 
print("\n\n WHILE \n")


count = 0

while count < 5:
    name = input("Please enter a name: ")
    print(f"{count + 1} - {name} is awesome!")
    count += 1
    
# FOR
print("\n\n FOR \n")

for i in range(5):
    name = input("Please enter a name: ")
    print(f"{i + 1} - {name} is awesome!")
    

# LIST COMP
print("\n\n LIST COMP \n")

awesome_names = [f"{input('Enter a name: ')} is awesome" for _ in range(5)]

for sentence in awesome_names:
    print(sentence)
    
# ONE LINE LIST COMP
print("\n\n ONE LINE LIST COMP \n")

[print(f"{input('Enter a name: ')} is awesome") for _ in range(5)]
