import csv
import zipfile
from datetime import datetime
from pathlib import Path

class Colours:
    """
    Defines ANSI escape codes for terminal styling.
    Used to add visual emphasis to the CLI output.
    """
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

PERFORMANCE_DESCRIPTORS = {
    'performance': {
        1: "found the module content quite challenging",
        2: "maintained a steady, satisfactory standard",
        3: "consistently produced high-quality work",
        4: "delivered exceptional results across the board"
    },
    'understanding': {
        1: "had difficulty connecting with some of the core ideas",
        2: "grasped the essential fundamentals reasonably well",
        3: "developed a strong command of the topics covered",
        4: "demonstrated a deep, intuitive mastery of the subject"
    },
    'contribution': {
        1: "tended to be an observer during discussions",
        2: "offered thoughts occasionally during group chats",
        3: "was a valuable voice in our discussions",
        4: "actively drove the conversation and helped clarify things for peers"
    },
    'lab_completion': {
        1: "needed significant support to navigate the practical tasks",
        2: "managed the labs, though often needed a nudge in the right direction",
        3: "executed the lab exercises to a high standard",
        4: "breezed through the labs and even experimented with advanced scenarios"
    },
    'punctuality': {
        1: "struggled a bit with keeping to the schedule",
        2: "was generally prompt for sessions",
        3: "was reliable and consistently on time",
        4: "maintained a flawless attendance and punctuality record"
    },
    'engagement': {
        1: "seemed a little disconnected at times",
        2: "stayed tuned in and participated when asked",
        3: "interacted really well via Webex and the classroom",
        4: "brought great energy and enthusiasm to the sessions"
    },
    'further_study': {
        1: "spend some extra time revisiting the syntax foundations.",
        2: "tackle a few more coding challenges to boost self-belief.",
        3: "keep sharpening those containerisation and pipeline skills.",
        4: "aim high—start looking into cloud architecture certifications."
    }
}

base_path = Path(__file__).parent
csv_path = base_path / "students.csv"
out_dir = base_path / "feedback"
zip_dir = base_path / "feedback_archive"

"""Ensure output directories exist before processing."""
out_dir.mkdir(exist_ok=True)
zip_dir.mkdir(exist_ok=True)

def build_text(name, scores):
    """
    Constructs the feedback letter by mapping numeric scores to descriptors.
    
    Args:
        name (str): The student's name.
        scores (dict): Dictionary of category keys and integer scores (1-4).
        
    Returns:
        str: The formatted feedback text.
    """
    p = {k: PERFORMANCE_DESCRIPTORS[k].get(v, "N/A") for k, v in scores.items()}
    
    return (
        f"General comments\n"
        f"{name} {p['performance']} in this module. "
        f"{name} {p['understanding']} and showed they have a solid knowledge base.\n"
        f"They {p['contribution']}. Regarding the practical work, {name} {p['lab_completion']}.\n\n"
        f"Learner Punctuality and engagement\n"
        f"{name} {p['punctuality']} and {p['engagement']}.\n\n"
        f"Recommendations on further learning\n"
        f"{p['further_study']}\n"
    )

"""
---------------------------------------------------------
Main Script Execution
---------------------------------------------------------
"""

students = []

"""
Load data from CSV.
Assumes the file exists and the format is correct.
Parses rows into a list of dictionaries with integer scores.
"""
print(f"{Colours.HEADER}--- Loading Data ---{Colours.END}")
try:
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            s_scores = {k.lower(): int(v) for k, v in row.items() if k != 'Name'}
            students.append({'name': row['Name'], 'scores': s_scores})
    print(f"{Colours.GREEN}Successfully loaded {len(students)} students from CSV.{Colours.END}")
except FileNotFoundError:
    print(f"{Colours.FAIL}Error: Could not find students.csv{Colours.END}")
    exit()

"""Display the student roster to the console."""
print(f"\n{Colours.HEADER}--- Student List ---{Colours.END}")
for idx, s in enumerate(students):
    print(f"{Colours.CYAN}[{idx}]{Colours.END} {s['name']}")

"""
Quick and dirty input selection.
Captures user input to select a specific student by index.
"""
try:
    target_idx = int(input(f"\n{Colours.BOLD}Enter ID to edit/generate:{Colours.END} "))
    student = students[target_idx]
except (ValueError, IndexError):
    print(f"{Colours.FAIL}Invalid selection.{Colours.END}")
    exit()

print(f"\n{Colours.HEADER}Editing: {Colours.BOLD}{student['name']}{Colours.END}")
print(f"{Colours.WARNING}Press Enter to keep current score, or type new number (1-4).{Colours.END}")

"""
Iterate through performance metrics.
Allows the user to input new scores line-by-line.
Validation ensures only integers 1-4 are accepted.
"""
for key in PERFORMANCE_DESCRIPTORS.keys():
    curr = student['scores'].get(key, 0)
    nice_key = key.replace('_', ' ').title()
    
    val = input(f"  {nice_key} [{Colours.BLUE}Current: {curr}{Colours.END}]: ")
    
    if val.strip():
        if val.isdigit() and 1 <= int(val) <= 4:
            student['scores'][key] = int(val)
        else:
            print(f"  {Colours.FAIL}Invalid input, keeping old score.{Colours.END}")

"""
Update the original CSV file.
Flattens the student dictionary back into CSV row format and overwrites the file.
"""
print(f"\n{Colours.HEADER}--- Updating CSV ---{Colours.END}")
try:
    fieldnames = ['Name'] + list(PERFORMANCE_DESCRIPTORS.keys())
    
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for s in students:
            row = {'Name': s['name']}
            row.update(s['scores'])
            writer.writerow(row)
            
    print(f"{Colours.GREEN}Updated {csv_path.name} with new scores.{Colours.END}")
except Exception as e:
    print(f"{Colours.FAIL}Failed to save CSV: {e}{Colours.END}")

"""Generate and save the feedback text file."""
print(f"\n{Colours.HEADER}--- Generating Feedback ---{Colours.END}")
content = build_text(student['name'], student['scores'])
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{student['name']}_{timestamp}.txt"
file_path = out_dir / filename

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
    print(f"{Colours.GREEN}Saved to:{Colours.END} {file_path}")

"""
Update the ZIP archive.
Compresses all text files in the output directory into a timestamped zip.
"""
print(f"\n{Colours.HEADER}--- Archiving ---{Colours.END}")
zip_name = f"archive_{timestamp}.zip"
zip_full_path = zip_dir / zip_name

with zipfile.ZipFile(zip_full_path, 'w') as zf:
    for txt in out_dir.glob("*.txt"):
        zf.write(txt, arcname=txt.name)

print(f"{Colours.GREEN}Archive created at:{Colours.END} {zip_full_path}")
print(f"{Colours.BOLD}Done.{Colours.END}")