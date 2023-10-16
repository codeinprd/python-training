def get_name_from_email(email_address):
    part_of_name = email_address.split("@")
    full_name = part_of_name[0].split(".")
    first_name = full_name[0].title()
    last_name = full_name[1].title()
    formatted_full_name = f"{first_name} {last_name}"
    return formatted_full_name


email_address = ["aviral.vishnoi@gmail.com", "ram.krishna@gmail.com"]

for email in email_address:
    name = get_name_from_email(email)
    print(name)

