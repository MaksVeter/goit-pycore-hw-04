def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if (name and phone and not exists(name, contacts)):
        contacts[name] = phone
        return "Contact added."
    return "Invalid params or contact is already exist."


def change_contact(args, contacts):
    name, phone = args
    if (name and phone and exists(name, contacts)):
        contacts[name] = phone
        return "Contact updated."
    return "Invalid params or contact doesn't exist."


def get_contact_phone(args, contacts):
    name = args[0]
    if (name and exists(name, contacts)):
        return contacts[name]
    return "Invalid params or contact doesn't exist."


def get_all(contacts):
    res = ''
    for name, phone in contacts.items():
        res += f"{name} {phone}\n"
    return res


def exists(name, contacts):
    return name in contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
