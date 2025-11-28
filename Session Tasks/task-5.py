ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

def ageLength(ages):
    age_length = len(ages)

    print(f"Ages length: {age_length}\n")

def printAges(ages):
    for index, age in enumerate(ages, start=1):
        print(f"{index}. {age}")
        print(f"{index}. {age + 1}\n")
        
def removeAges(ages):
    for age in ages[:]:
        if age not in range(15, 66):
            ages.remove(age)
            
    print(f"{ages}\n")
    print(f"New ages length: {len(ages)}\n")
    
def countAges(ages):
    count = 0
    range_start = int(input("Enter a starting age to count from: "))
    range_end = int(input("Enter a finishing age to count to: "))

    for age in ages:
        if age in range(range_start-1, range_end+1):
            count += 1
            
    print(f"There are {count} people in the age range of {range_start} - { range_end }\n")
    
def sortAges(ages):
    print(f"Ascending:  {sorted(ages)}\n")
    print(f"Descending:  {sorted(ages, reverse=True)}\n")
    
def proportionAge(ages):
    range_start = int(input("Enter a starting age to count from: "))
    range_end = int(input("Enter a finishing age to count to: "))
    
    new_ages = []
    
    for age in ages:
        if age in range(range_start-1, range_end+1):
            new_ages.append(age)
    
    proportion = len(new_ages)/len(ages)
    
    print(f"{(proportion*100):.2f}% of people in the age range of {range_start} - {range_end}")
        
def main(ages):
    ageLength(ages)
    
    printAges(ages)
    
    removeAges(ages)
    
    countAges(ages)
    
    sortAges(ages)
    
    proportionAge(ages)
    
main(ages)