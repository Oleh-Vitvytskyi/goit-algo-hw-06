from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Номер телефону повинен складатися з 10 цифр")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value: str):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]

    def edit_phone(self, old_phone_value: str, new_phone_value: str):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value
                break

    def find_phone(self, phone_value: str):
        for phone in self.phones:
            if phone.value == phone_value:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, name_value: str):
        return self.data.get(name_value)

    def delete_record(self, name_value: str):
        if name_value in self.data:
            del self.data[name_value]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Приклад використання
try:
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book)


    john = book.find_record("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")

    
    book.delete_record("Jane")
    print(book)

except ValueError as e:
    print(e)
