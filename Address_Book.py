address_book = {}

while True: 
    print("---------------------")
    action = input("Are you sending or retrieving data? Type 'S' or 'R': ")

    if action.lower() == "s":
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")

        address_book[name] = {"address": address, "phone": phone}
        print(f"Data added for {name}.")

    elif action.lower() == "r":
        if not address_book:
            print("Address book empty. Data not retrievable.")
        name = input("Enter name: ")
        if name in address_book:
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Phone number: {phone}")
        else:
            print("No data found.")
    elif action == "done": 
        print("Exited address book.")
        break
    else: 
        print("Invalid input. Please type 'S' or 'R'")
