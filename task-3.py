# Exercise:
#     - weight converter
#     - user to input weight
#     - user to select either Kgs or Lbs
#     - logic: check the unit entered
#     - logic: calculate the conversion
#     - print out the result nicely!!
#     - Stretch: Error handling for incorrect unit type (upper/lower, else/while loop) 
#     - Optional: Error handling for non-numeric inputs for weight. 

def weightconverter():
    units = ["Kgs", "Lbs"]

    print(f"--- Weight Converter ---")
    for index, unit in enumerate(units, start=1):
        print(f"{index}. {unit}")
        
    try:
        selection = int(input("Please select a unit by number to convert to: "))
        
        if 1 <= selection <= len(units):
            selected_unit = units[selection - 1]
            
            if selected_unit == "Kgs":
                weight = float(input(f"\nPlease enter a weight in Lbs: "))
                
                calculated_pounds = weight * 2.20462

                return f"\n{weight}Lbs in {selected_unit} is:\n\t{weight} * 2.20462 = {calculated_pounds:.3f} Kgs"
            elif selected_unit == "Lbs":
                weight = float(input(f"\nPlease enter a weight in Kgs: "))
                
                calculated_kilos = weight / 2.20462

                return f"\n{weight}Kgs in {selected_unit} is:\n\t{weight} / 2.20462 = {calculated_kilos:.3f} Lbs"
        else:
            return f"\nError: Please select a valid number from the menu."
            

    except ValueError:
        return f"\nError: Invalid input. Please enter a number."

print(weightconverter())