contacts = {}
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
    print(f"Contact {full_name} added sucessfully.")

def view_contact():
    if not contacts:
        print("Contact does not exist.")
    else: 
        print("\n --- CONTACT LIST ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print("-----------------------")

def search_contact():
    search = input("Enter the name to search: ").strip().title()
    for full_name, phone in contacts.items():
        if search in name:
            print(f"{full_name}: {phone}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name to update: ").strip().title()
    if name in contacts:
        new_number = input("Enter new phone number: ").strip()
        contacts[name] = new_number
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")


        

        

    


while True:
    record = input("Name: ")
    num = input("Number: ")
    print(record, num)
