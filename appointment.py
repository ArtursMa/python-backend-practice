from dataclasses import dataclass
from datetime import datetime
from client import Client


@dataclass
class Appointment:
    client: Client
    is_confirmed: bool
    service_name: str
    price_in_cents_per_hour: int
    scheduled_start: datetime
    estimated_end: datetime
    actual_start: datetime | None = None
    actual_end: datetime | None = None

    def __post_init__(self):
        if not isinstance(self.client, Client):
            raise TypeError("Client must be a Client instance")
        if not isinstance(self.is_confirmed, bool):
            raise TypeError("Boolean value should be provided")
        if not isinstance(self.service_name, str):
            raise TypeError("Service name should provide string")
        stripped_service_name = self.service_name.strip()
        if not stripped_service_name:
            raise ValueError("Service name is empty")
        self.service_name = stripped_service_name
        if not isinstance(self.price_in_cents_per_hour, int) or isinstance(self.price_in_cents_per_hour, bool):
            raise TypeError("price should be int")
        if self.price_in_cents_per_hour <= 0:
            raise ValueError("Price should be positive")
        if not isinstance(self.scheduled_start, datetime):
            raise TypeError("scheduled start should be datetime")
        if not isinstance(self.actual_start, datetime) and self.actual_start is not None:
            raise TypeError("scheduled start should be datetime")
        if not isinstance(self.estimated_end, datetime):
            raise TypeError("scheduled start should be datetime")
        if not isinstance(self.actual_end, datetime) and self.actual_end is not None:
            raise TypeError("scheduled start should be datetime")
        if self.estimated_end <= self.scheduled_start:
            raise ValueError("Time of appointment should be more than zero")
        if self.actual_start and self.actual_end:
            if self.actual_end <= self.actual_start:
                raise ValueError("Time of appointment should be more than zero")








