import sys
import time
import re

def get_valid_time_input(prompt):
    basic_pattern = r"^\d{2}:\d{2}:\d{2}$"
    strict_pattern = r"^\d{2}:(?:[01]\d|2[0-3]):[0-5]\d$"

    while True:
        user_input = input(prompt)

        if not re.match(basic_pattern, user_input):
            print(f"'{user_input}': Format Error (Must be strict DD:HH:MM e.g. 01:12:30)")
            continue 
        
        elif not re.match(strict_pattern, user_input):
            print(f"'{user_input}': Logical Error (Hours must be 00-23, Minutes 00-59)")
            continue 
        
        else:
            return user_input

def add_times():
    print(">> Executing: Add 2 Times")
    time.sleep(0.5)
    
    date1 = get_valid_time_input(f"Please enter a date to add (DD:HH:MM): ")
    date2 = get_valid_time_input(f"Please another date to add to {date1} (DD:HH:MM): ")
    
    date1_day = int(date1.split(":")[0])
    date1_hours = int(date1.split(":")[1])
    date1_mins = int(date1.split(":")[-1])
    
    date2_day = int(date2.split(":")[0])
    date2_hours = int(date2.split(":")[1])
    date2_mins = int(date2.split(":")[-1])
    
    calculated_date = f"{date1_day + date2_day}:{date1_hours + date2_hours}:{date1_mins + date2_mins}\n"
    
    return calculated_date

    
def diff_times():
    print(">> Executing: Difference Of 2 Times")
    time.sleep(0.5)
    date1 = get_valid_time_input(f"Please enter a date (DD:HH:MM): ")
    date2 = get_valid_time_input(f"Please another date (DD:HH:MM): ")
    
    date1_day = int(date1.split(":")[0])
    date1_hours = int(date1.split(":")[1])
    date1_mins = int(date1.split(":")[-1])
    
    date2_day = int(date2.split(":")[0])
    date2_hours = int(date2.split(":")[1])
    date2_mins = int(date2.split(":")[-1])
    
    calculated_date = f"{date1_day - date2_day}:{date1_hours - date2_hours}:{date1_mins - date2_mins}\n"
    
    return calculated_date

def convert_to_hours():
    print(">> Executing: Convert To Hours")
    time.sleep(0.5)
    date = get_valid_time_input(f"Please enter a date to convert to hours (DD:HH:MM): ")
    
    date_day = int(date.split(":")[0])
    date_hours = int(date.split(":")[1])
    date_mins = int(date.split(":")[-1])
    
    calculated_date = f"{((date_day * 24) + date_hours + (date_mins / 60)):.2f} hours"
    return calculated_date

def convert_to_minutes():
    print(">> Executing: Convert To Minutes")
    time.sleep(0.5)

    date = get_valid_time_input(f"Please enter a date to add (DD:HH:MM): ")
    
    date_day = int(date.split(":")[0])
    date_hours = int(date.split(":")[1])
    date_mins = int(date.split(":")[-1])
    
    calculated_date = f"{((date_day * 1440) + (date_hours * 60) + (date_mins)):.2f} minutes"
    return calculated_date

def convert_minutes_to_time():
    print(">> Executing: Convert Minutes To Time")
    time.sleep(0.5)

def convert_hours_to_time():
    print(">> Executing: Convert Hours To Time")
    time.sleep(0.5)

def convert_days_to_time():
    print(">> Executing: Convert Days To Time")
    time.sleep(0.5)

def exit_script():
    print("Exiting program...")
    time.sleep(2)
    sys.exit()

def menu():
    options = [
        "Add 2 Times",
        "Difference Of 2 Times",
        "Convert To Hours",
        "Convert To Minutes",
        "Convert Minutes To Time",
        "Convert Hours To Time",
        "Convert Days To Time",
        "Exit"
    ]
    
    print(f"\n----- Time Calculator -----")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
        
    try:
        selection = int(input(f"Please select an option (1 - {len(options)}): "))
        return selection
    except ValueError as e:
        print("\nSelection must be an integer")
        print(f"[ERROR]: {e}")
        return False

def main():
    menu_actions = [
        add_times,
        diff_times,
        convert_to_hours,
        convert_to_minutes,
        convert_minutes_to_time,
        convert_hours_to_time,
        convert_days_to_time,
        exit_script
    ]

    while True:
        choice = menu()

        if choice is False:
            continue

        if 1 <= choice <= len(menu_actions):
            selected_function = menu_actions[choice - 1] 
            print(selected_function())
            input("Please press enter to CONTINUE")
        else:
            print(f"\n[ERROR]: Please enter a number between 1 and {len(menu_actions)}.")

if __name__ == "__main__":
    main()