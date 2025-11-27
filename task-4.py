# TASK:
# loop to get 5 names as inputs + prints with "is awesome" added to it. 

# while loop
# for loop
# list comp
# STRETCH GOAL: list comp one line only! 

# WHILE 
count = 0

while count < 5:
    name = input("Please enter a name: ")
    print(f"{name} is awesome!")
    count += 1
    
# FOR
for i in range(5):
    name = input("Please enter a name: ")
    print(f"{name} is awesome!")
    

# LIST COMP
awesome_names = [f"{input('Enter a name: ')} is awesome" for _ in range(5)]

for sentence in awesome_names:
    print(sentence)
    
# ONE LINE LIST COMP

[print(f"{input('Enter a name: ')} is awesome") for _ in range(5)]