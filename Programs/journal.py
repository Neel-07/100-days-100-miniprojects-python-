import os
import json
from datetime import datetime

def create_journal_entry():
    try:
        # Input journal entry
        entry_text = input("Write your journal entry: ")

        # Get current date and time
        entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create an entry dictionary
        entry = {
            "date": entry_date,
            "text": entry_text
        }

        # Save the entry to a JSON file
        journal_file = "journal.json"
        if not os.path.exists(journal_file):
            with open(journal_file, 'w') as file:
                json.dump([], file)

        with open(journal_file, 'r') as file:
            journal_data = json.load(file)
            journal_data.append(entry)

        with open(journal_file, 'w') as file:
            json.dump(journal_data, file, indent=4)

        return "Journal entry saved successfully."

    except Exception as e:
        return f"An error occurred: {str(e)}"

def view_journal_entries():
    try:
        journal_file = "journal.json"
        if os.path.exists(journal_file):
            with open(journal_file, 'r') as file:
                journal_data = json.load(file)
                if journal_data:
                    print("\nJournal Entries:")
                    for entry in journal_data:
                        print(f"Date: {entry['date']}")
                        print(f"Entry: {entry['text']}\n")
                else:
                    print("No journal entries available.")
        else:
            print("No journal entries available.")

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main menu
while True:
    print("Main Menu:")
    print("1. Create Journal Entry")
    print("2. View Journal Entries")
    print("3. Quit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        create_journal_entry()
    elif choice == '2':
        view_journal_entries()
    elif choice == '3':
        print("Thanks for using the Journal App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

