import json
import os

class Phonebook:
    def __init__(self):
        self.phonebook_file = 'phonebook.json'
        if not os.path.exists(self.phonebook_file):
            with open(self.phonebook_file, 'w') as f:
                json.dump([], f)

        while True:
            user_input = input("Enter 1 to add contact, 2 to search contact, 3 to update contact, 4 to delete contact, 5 to close the program: ")

            if user_input == '1':
                self.add_contact()
            elif user_input == '2':
                self.search_contact()
            elif user_input == '3':
                self.update_contact()
            elif user_input == '4':
                self.delete_contact()
            elif user_input == '5':
                print("Program has been closed")
                break
            else:
                print("Invalid input")

    def add_contact(self):
        name_input = input("Enter name: ")
        phone_input = input("Enter phone number: ")

        with open(self.phonebook_file, 'r') as f:
            data = json.load(f)

        # Kontrollon nqs ka 2 numra njesoj
        for entry in data:
            if entry['phone'] == phone_input:
                print("Phone number already exists")
                return

        data.append({"name": name_input, "phone": phone_input})

        with open(self.phonebook_file, 'w') as f:
            json.dump(data, f)
        print("Contact added successfully.")

    def search_contact(self):
        search_input = input("Enter name or phone number to search: ")

        with open(self.phonebook_file, 'r') as f:
            data = json.load(f)

        found = False
        for entry in data:
            if entry['name'] == search_input or entry['phone'] == search_input:
                print(f"Name: {entry['name']}, Phone: {entry['phone']}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self):
        name_input = input("Enter name to update: ")

        with open(self.phonebook_file, 'r') as f:
            data = json.load(f)

        found = False
        for entry in data:
            if entry['name'] == name_input:
                new_phone = input("Enter new phone number: ")
                entry['phone'] = new_phone
                found = True
        if not found:
            print("Contact not found.")
        else:
            with open(self.phonebook_file, 'w') as f:
                json.dump(data, f)
            print("Contact updated successfully.")

    def delete_contact(self):
        name_input = input("Enter name to delete: ")

        with open(self.phonebook_file, 'r') as f:
            data = json.load(f)

        # Kerkon te gjitha kontatet qe e kan emrin e njejt
        contacts_to_delete = [entry for entry in data if entry['name'] == name_input]

        if not contacts_to_delete:
            print("Contact not found.")
        else:
            if len(contacts_to_delete) > 1:
                print("Contacts with the same name found:")
                for i, entry in enumerate(contacts_to_delete):
                    print(f"{i+1}. Name: {entry['name']}, Phone: {entry['phone']}")

                choice = input("Enter the number of the contact to delete: ")
                try:
                    choice_index = int(choice) - 1
                    if choice_index < 0 or choice_index >= len(contacts_to_delete):
                        print("Invalid choice.")
                        return
                    del contacts_to_delete[choice_index]
                except ValueError:
                    print("Invalid input.")
                    return

            updated_data = [entry for entry in data if entry not in contacts_to_delete]

            with open(self.phonebook_file, 'w') as f:
                json.dump(updated_data, f)
            print("Contact deleted successfully.")

Phonebook()