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


print(Client("Anna", "+32212121", False))
try:
    Client("Zina", "+2323232", "active")
except TypeError as ex:
    print(ex)

print(Client.all_clients_count)

