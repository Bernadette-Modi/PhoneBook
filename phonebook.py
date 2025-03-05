contacts = {}
def display_menu: 
    print("Welcome to the Phone Book system.")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    

while True:
    record = input("Name: ")
    num = input("Number: ")
    print(record, num)
