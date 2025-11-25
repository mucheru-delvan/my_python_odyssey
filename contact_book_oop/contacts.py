import json
from pathlib import Path


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = Path(__file__).parent / filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self, name, phone):
        # I added this to check if contact already exists thus updating instead of adding duplicate
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                contact["phone"] = phone
                self.save_contacts()
                return f"Updated {name}'s phone number to {phone}"
        
        new_contact = {"name": name, "phone": phone}
        self.contacts.append(new_contact)
        self.save_contacts()
        return f"Added new contact: {name} with phone number {phone}"

    def search_contact(self, name):

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return f"Found {contact['name']} with phone number {contact['phone']}"

        return f"Contact {name} not found"

    def remove_contact(self, name):

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return f"{name} removed from contacts."
        return f"{name} not found in contacts."

    def show_contacts(self):

        if not self.contacts:
            print("No contacts added yet!")
        else:
            print("\n📜 Your Contacts\n")
            for i, contact in enumerate(self.contacts):
                print(f"{i + 1}. {contact['name']}: {contact['phone']}")
