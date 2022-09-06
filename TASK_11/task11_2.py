import json

PHONEBOOK_FILE_NAME = "pb.json"
global phonebook


def trying_or_creating(PHONEBOOK_FILE_NAME):
    try:
        with open(PHONEBOOK_FILE_NAME, "r") as file:
            phonebook = json.load(file)
            print(f"Phonebook was loaded from file '{PHONEBOOK_FILE_NAME}'.")
            return phonebook
    except:
        print(
            f"File '{PHONEBOOK_FILE_NAME}' was not found."
            f" Sample phonebook was created"
        )
        phonebook = [
            {
                "Name": "Mary",
                "Surname": "Hodges",
                "Full Name": "",
                "Country": "Ukraine",
                "City": "Odessa",
                "Phone": "+380930423834",
                "Contact_No": "",
            },
            {
                "Name": "Robert",
                "Surname": "Jones",
                "Full Name": "",
                "Country": "Ukraine",
                "City": "Kyiv",
                "Phone": "+380501013233",
                "Contact_No": "",
            },
        ]
        return phonebook



def printing_single_contact(contact):
    for i, j in contact.items():
        if i != "Contact_No":
            print(f"{i} : {j}")


def printing_phonebook():
    for contact in phonebook:
        print(f"--Contact #{contact['Contact_No']}--")
        printing_single_contact(contact)
    input("Press [Enter] to continue.")



def adding_contact():
    phonebook.append(
        {
            "Name": input("Insert First Name: "),
            "Surname": input("Insert Last Name: "),
            "Full Name": "",
            "Country": input("Insert Country: "),
            "City": input("Insert City: "),
            "Phone": input("Insert Phone: "),
            "Contact_No": "",
        }
    )
    print("New contact was added")
    input("Press [Enter] to continue.")



def finding_contact(action):
    contact_to_choose = ""
    while not quit_or_menu(contact_to_choose):
        contact_to_choose = input(
            f"Which Contact would you like to {action}?\n\
        Enter full name(Surname name: "
        )
        for contact in phonebook:
            if contact["Full name"] == contact_to_choose.replace(" ", ""):
                print(f"We found contact '{contact['Full Name']}'")
                printing_single_contact(contact)
                input("Press [Enter] to continue")
                return contact
            else:
                print(f"Sorry your contact was not found or print it correctly")



def editing_contact(contact):
    editing_data = ""
    while not quit_or_menu(editing_data):
        editing_data = input(
            '\nWhat would you like to Edit? \n"1" for Name,'
            ' \n"2" for Surname, \n"3" for Country, \n"4" for City'
            ',\n"5" for Phone"\nPlease Enter Number to choose (or [M/m] for '
            "Menu): "
        )
        if editing_data == "1":
            contact["Name"] = input("Enter new Name: ")
            print(f"Name was successfully changed to '{contact['Name']}'.")
        elif editing_data == "2":
            contact["Surname"] = input("Enter new Surname: ")
            print(f"Surname was successfully changed to '{contact['Surname']}'.")
        elif editing_data == "3":
            contact["Country"] = input("Enter new Country: ")
            print(f"Country was successfully changed to '{contact['Country']}'.")
        elif editing_data == "4":
            contact["City"] = input("Enter new City: ")
            print(f"City was successfully changed to '{contact['City']}'.")
        elif editing_data == "5":
            contact["Phone"] = input("Enter new Phone Number: ")
            print(f"Phone was successfully changed to '{contact['Phone']}'.")



def removing_contact(contact):
    for i in range(len(phonebook)):
        if phonebook[i]["Full Name"] == contact["Full Name"]:
            del phonebook[i]
            break



def searching_contact():
    searching_input = ""
    found_contacts = []
    while not quit_or_menu(searching_input):
        searching_input = input(f"Please enter any data like Name, City etc..")
        print(f"We'll try to find '{searching_input}'")
        for contact in phonebook:
            for value in contact.values():
                if searching_input in str(value):
                    found_contacts.append(value)
                else:
                    print("Try to print data correctly")



def store_phonebook():
    with open(PHONEBOOK_FILE_NAME, "w") as file:
        json.dump(phonebook, file)



def quit_or_menu(user_input):
    if user_input == "q":
        print(f"All changes are saved to '{PHONEBOOK_FILE_NAME}'")
        print(f"See you soon")
        store_phonebook()
        quit()
    elif user_input in ("m", "n"):
        print("Back to menu")
        main_menu()
    else:
        pass


def main_menu():
    menu_choice = ""
    while not quit_or_menu(menu_choice):
        counter = 0
        for contact in phonebook:
            counter += 1
            contact["Contact_No"] = counter
            contact["Full Name"] = f"{contact['Surname']} {contact['Name']}"
        menu_choice = input(
            """\n1. Show Contacts List
2. Add New Contact
3. Edit Contact
4. Remove Contact
5. Search
Also, anywhere in the Program you can use: 
m - Main Menu
q - Quit
Your action: """
        )
        if menu_choice == "1":
            printing_phonebook()
        elif menu_choice == "2":
            adding_contact()
        elif menu_choice == "3":
            contact = finding_contact("Edit")
            editing_contact(contact)
        elif menu_choice == "4":
            contact = finding_contact("Remove")
            removing_contact(contact)
        elif menu_choice == "5":
            search_result = searching_contact()


phonebook = trying_or_creating(PHONEBOOK_FILE_NAME)
main_menu()
