from dataclasses import dataclass
from datetime import datetime
from client import Client


def get_minutes(start_time, end_time):
    duration = end_time - start_time
    duration_in_seconds = duration.total_seconds()
    duration_in_minutes = int(duration_in_seconds / 60)
    return duration_in_minutes


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

    def get_estimated_minutes(self) -> int:
        duration_in_minutes = get_minutes(self.scheduled_start,self.estimated_end)
        return duration_in_minutes

    def get_actual_minutes(self) -> int | None:
        if self.actual_start is None or self.actual_end is None:
            return None
        return get_minutes(self.actual_start,self.actual_end)

















