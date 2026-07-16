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


try:
    Client(" ", "+317372893823")

except ValueError as ex:
    print(ex)
print(Client(" Anna ", "+22323822"))
