from dataclasses import dataclass


@dataclass
class Client:
    name: str
    phone: str
    is_active: bool


first_client = Client("Anna", "+327832223", True)
print(f"My first client name is {first_client.name}, her phone number is {first_client.phone}")
print(first_client)
second_client = Client("Veronika", "+32323232", False)
print(second_client)
