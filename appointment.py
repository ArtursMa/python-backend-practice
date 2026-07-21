from dataclasses import dataclass
from datetime import timedelta
from client import Client


@dataclass
class Appointment:
    client: Client
    service_name: str
    client_hours: str
    price_in_cents_per_hour: int
    is_confirmed: bool


first_client = Client("Anna","+322323232")
first_appointment = Appointment(first_client,"Electrolysis", "2", 60, True)

