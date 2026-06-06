"""def validation_name_and_contact(func):
    def wrapper(name, contact_number):
        if not name or not isinstance(name, str):
            return "Name must be a non-empty string."

        if len(contact_number) != 10 or not contact_number.isdigit():
            return "Contact number must be a 10-digit number."

        return func(name, contact_number)
    return wrapper

@validation_name_and_contact
def register_user(name, contact_number):
    return f"User {name} with contact number {contact_number} has been successfully registered."

print(register_user("Alice", "1234567890")) # valid input
print(register_user("", "1234567890")) # Invalid name
print(register_user("bob", "12345")) # Invalid contact number
print(register_user("Alice", "1234@ab890")) # Invalid contact number (contact letters)"""


def validation_name_and_contact(func):
    def wrapper(fname,lname, contact_number):
        if not fname or not isinstance(fname, str):
            return "Name must be a non-empty string."
        if not lname or not isinstance(lname, str):
            return "Name must be a non-empty string."

        if len(contact_number) != 10 or not contact_number.isdigit():
            return "Contact number must be a 10-digit number."
    
        return func(fname,lname contact_number)
    return wrapper

@validation_name_and_contact
def register_user(fname,lname, contact_number):
    return f"User {fname}, {lname} with contact number {contact_number} has been successfully registered."

print(register_user("Alice", "1234567890")) # valid input
print(register_user("", "1234567890")) # Invalid name
print(register_user("bob", "12345")) # Invalid contact number
print(register_user("Alice", "1234@ab890")) # Invalid contact number (contact letters)
