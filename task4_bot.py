"""
Це простий бот-помічник, який дозволяє користувачеві додавати, змінювати та переглядати контакти.
"""

def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та аргументи.
    Повертає кортеж (command, *args).
    """

    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає контакт до списку контактів.
    """

    if len(args) != 2:
        return "Invalid input. Please provide a name and phone number."
    
    name = args[0].lower()
    phone = args[1]
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added."

def change_contact(args, contacts):
    """
    Змінює телефон контакту.
    """

    if len(args) != 2:
        return "Invalid input. Please provide a name and new phone number."
    
    name = args[0].lower()
    new_phone = args[1]
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name}'s phone number changed to {new_phone}."
    else:
        return f"Contact {name} not found."

def show_phone(args, contacts):
    """
    Показує телефон контакту.
    """

    if len(args) != 1:
        return "Invalid input. Please provide a name."
    name = args[0].lower()
    if name in contacts:
        return f"Contact {name}'s phone number is {contacts[name]}."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    """
    Показує всі контакти.
    """

    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    """
    Головна функція, яка запускає бота-помічника.
    """

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()