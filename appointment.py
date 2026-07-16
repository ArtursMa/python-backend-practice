from dataclasses import dataclass


@dataclass
class Client:
    name: str
    phone: str
    is_active: bool = True

    def __post_init__(self):
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



try:
    Client(" ", "+317372893823")

except ValueError as ex:
    print(ex)
print(Client(" Anna ", "+22323822"))
try:
    Client("Valery", 3333)
except TypeError as ex:
    print(ex)
try:
    Client("sds", " ")
except ValueError as ex:
    print(ex)
