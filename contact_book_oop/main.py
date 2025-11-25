from contacts import ContactBook


phonebook1 = ContactBook()
phonebook1.add_contact("Dorian","+254729292456")
phonebook1.add_contact("Mutabaruka","+254789345768")
phonebook1.add_contact("Luciano","+254782345002")
print(phonebook1.search_contact("Luciano"))
print(phonebook1.remove_contact("DORIAN"))
phonebook1.show_contacts()

