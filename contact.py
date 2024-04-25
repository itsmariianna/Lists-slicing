def add_contact(contact_list):
    def add(name, phone):
        contact_list[name] = phone
        print(f"Contact {name} added successfully.")
    return add

def delete_contact(contact_list):
    def delete(name):
        if name in contact_list:
            del contact_list[name]
            print(f"Contact deleted successfully.")
        else:
            print(f"Contact not found.")
    return delete

def search_contact(contact_list):
    def search(name):
        if name in contact_list:
            print(f"Name: {name}, Phone: {contact_list[name]}")
        else:
            print(f"Contact {name} not found.")
    return search

def view_contacts(contact_list):
    def view():
        if contact_list:
            print("Contacts:")
            for name, phone in contact_list.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")
    return view

def main():
    contacts = {}

    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = input("Choose number: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts)(name, phone)
        elif choice == '2':
            name = input("Enter contact name to delete: ")
            delete_contact(contacts)(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(contacts)(name)
        elif choice == '4':
            view_contacts(contacts)()
        elif choice == '5':
            print("EXIT")
            break
        else:
            print("Enter a number between 1 and 4.")


if __name__ == "__main__":
    main()