import sys

milkshakes = {
    "vanilla": 2.99,
    "chocolate": 3.50,
    "strawberry": 3.75,
    "mint": 3.25
        }

budget = float(20.00)

while budget >= min(milkshakes.values()):
    print("--- Milkshake Menu ---")
    for index, milkshake in enumerate(milkshakes, start=1):
        print(f"{index}. {milkshake}:\t£{milkshakes[milkshake]:.2f}")
        
    print(f"{len(milkshakes) + 1}.\t\tQuit")
    choice = int(input(f"Please select a milkshake by number:\t"))

    if choice >= 1 or choice <= len(milkshakes):
        selected_milkshake = list(milkshakes.keys())[choice - 1]
        price = milkshakes[selected_milkshake]
        
        print(f"You selected a {selected_milkshake} milkshake for £{price:.2f}")
        
        budget -= price
        print(f"Your remaining budget is £{budget:.2f}")
    
    elif choice == 5:
        sys.exit("Thank You for visiting the Milk Bar")
        
    else:
        print("Sorry We Dont Serve That, Pick Another!")
        

sys.exit("Get Out Broke Boy")