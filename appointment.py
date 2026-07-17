from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Client:
    name: str
    phone: str
    is_active: bool = True
    all_clients_count: ClassVar[int] = 0

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Name should be string")
        stripped_name = self.name.strip()
        if not stripped_name:
            raise ValueError("Please write client name")
        self.name = stripped_name
        if not isinstance(self.phone, str):
            raise TypeError("Phone should be string")
        stripped_phone = self.phone.strip()
        if not stripped_phone:
            raise ValueError("Please write a number")
        self.phone = stripped_phone
        if not isinstance(self.is_active, bool):
            raise TypeError("is_active should be bool")
        Client.all_clients_count += 1

    def activate(self):
        if not self.is_active:
            self.is_active = True

    def deactivate(self):
        if self.is_active:
            self.is_active = False

    def rename(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name should be string")
        stripped_name = new_name.strip()
        if not stripped_name:
            raise ValueError("Empty name provided")
        self.name = stripped_name

    def change_phone(self, new_phone):
        if not isinstance(new_phone, str):
            raise TypeError("phone should be string")
        stripped_phone = new_phone.strip()
        if not stripped_phone:
            raise ValueError("Empty phone provided")
        self.phone = stripped_phone


client_one = Client("Anna", "+32323211")
client_one.change_phone("3333333")
client_one.rename("Oleg")
print(client_one.phone)
print(client_one.name)
client_one.rename(" Anna  ")
client_one.change_phone(" +33434 ")
print(f"{client_one.name} is name and phone is {client_one.phone}")
try:
    client_one.change_phone("   ")
except ValueError as ex:
    print(ex)
try:
    client_one.rename(2222)
except TypeError as ex:
    print(ex)
