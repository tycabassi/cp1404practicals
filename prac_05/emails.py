def main():
    emails_to_name = {}
    email = input("Email: ")
    while email != "":
        likely_name = get_plausible_name_from_email(email)
        name_check = input(f"Is your name {likely_name} y/n? ").lower()
        if name_check != "y" and name_check != "":
            name = input("Name: ")
        emails_to_name[email] = name
        email = input("Email: ")
    for email, name in emails_to_name.items():
        print(name, email)


def get_plausible_name_from_email(email):
    """ Returns the most likely name from the email address"""
    value_before_address = email.split("@")[0]
    parts = value_before_address.split('.')
    name = " ".join(parts).title()
    return name


main()
