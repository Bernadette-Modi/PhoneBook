import json
CONTACTS_FILE = "contact.json"
def load_contact():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contact()

def display_menu(): 
    print("Welcome to the Phone Book system.")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("First Name: ").strip().title()
    lname = input("Last Name: ").strip().title()
    full_name = name + " " + lname
    if full_name in contacts:
        print("Contact already exists!")
        return
    phone = input("Phone Number: ")
    contacts[full_name] = phone
    save_contacts()
    print(f"Contact {full_name} added sucessfully.")

def view_contact():
    if not contacts:
        print("Contact is empty.")
    else: 
        print("\n --- CONTACT LIST ---")
        for name in sorted(contacts):
            print(f"{name}: {contacts[name]}")
        print("-----------------------")

def search_contact():
    search = input("Enter the name to search: ").strip().title()
    for full_name, phone in contacts.items():
        if search in full_name:
            print(f"{full_name}: {phone}")
            return
    print("Contact not found.")

def update_contact():
    search = input("Enter the name to update: ").strip().title()
    matches = [name for name in contacts if search in name]

    if not matches:
        print("Contact not found.")
        return

    if len(matches) > 1:
        print("\nMultiple contacts found: ")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match}: {contacts[match]}")
        choice = input("Select the number of the contact to update: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, len(matches) + 1):
            print("Invalid Selection.")
            return
        selected_contact = matches[int(choice) - 1]
    else:
        selected_contact = matches[0]
    
    new_number = input(f"Enter new phone number for {selected_contact}: ").strip()
    contacts[selected_contact] = new_number
    save_contacts()
    print(f"Contact {selected_contact} updated successfully.")

def delete_contact():
    search = input("Enter the contact to delete: ").strip().title()
    matches = [name for name in contacts if search in name]

    if not matches:
        print("Contact not found.")
        return

    if len(matches) > 1:
        print("\nMultiple contacts found: ")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match}: {contacts[match]}")
        choice = input("Select the number of the contact to delete: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, len(matches) + 1):
            print("Invalid Selection.")
        selected_contact = matches[int(choice) - 1]
    else:
        selected_contact = matches[0]

    confirm = input(f"Are you sure you want to delete {selected_contact}? (yes/no): ").strip().lower()
    if confirm == "yes":
        del contacts[selected_contact]
        save_contacts()
        print(f"Contact {selected_contact} deleted successfully.")
    else:
        print("Deletion Canceled.")


        
while True:
    display_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Phone Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1-6.")

    
