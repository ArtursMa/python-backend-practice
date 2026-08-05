from datetime import datetime

from appointment import Appointment
from client import Client


def test_get_estimated_minutes():
    client = Client("Anna", "+328232232")

    appointment = Appointment(
        client=client,
        is_confirmed=True,
        service_name="Electrolysis",
        price_in_cents_per_hour=2200,
        scheduled_start=datetime(2026, 8, 5, 14, 0),
        estimated_end=datetime(2026, 8, 5, 15, 30),
    )

    result = appointment.get_estimated_minutes()

    assert result == 90


def test_get_actual_minutes():
    client = Client("Zina", "+324232322")
    appointment = Appointment(
        client=client,
        is_confirmed=True,
        service_name="Electrolysis",
        price_in_cents_per_hour=2200,
        scheduled_start=datetime(2026, 8, 5, 14, 10),
        estimated_end=datetime(2026, 8, 5, 15, 25),
        actual_start=datetime(2026, 8, 5, 14, 10),
        actual_end=datetime(2026, 8, 5, 15, 25),
    )

    result = appointment.get_actual_minutes()

    assert result == 75


def test_get_minutes_with_missing_data():
    client_two = Client("Nina", "2321111")
    appointment = Appointment(
        client=client_two,
        is_confirmed=True,
        service_name="Electrolysis",
        price_in_cents_per_hour=6000,
        scheduled_start=datetime(2026, 8, 5, 14, 0),
        estimated_end=datetime(2026, 8, 5, 15, 30),
        actual_start=None,
        actual_end=None
    )

    appointment_two = Appointment(
        client=client_two,
        is_confirmed=True,
        service_name="Electrolysis",
        price_in_cents_per_hour=6000,
        scheduled_start=datetime(2026, 8, 5, 14, 0),
        estimated_end=datetime(2026, 8, 5, 15, 30),
        actual_start=datetime(2026, 8, 5, 15, 30),
        actual_end=None
    )
    appointment_three = Appointment(
        client=client_two,
        is_confirmed=True,
        service_name="Electrolysis",
        price_in_cents_per_hour=6000,
        scheduled_start=datetime(2026, 8, 5, 14, 0),
        estimated_end=datetime(2026, 8, 5, 15, 30),
        actual_start=None,
        actual_end=datetime(2026, 8, 5, 15, 30)
    )

    result_with_no_actual_start_and_end = appointment.get_actual_minutes()
    result_with_no_actual_end = appointment_two.get_actual_minutes()
    result_with_no_actual_start = appointment_three.get_actual_minutes()
    assert result_with_no_actual_start_and_end is None
    assert result_with_no_actual_start is None
    assert result_with_no_actual_end is None
