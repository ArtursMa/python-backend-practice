from datetime import datetime
import pytest
from appointment import Appointment
from client import Client


def make_appointment(**changes):
    client = Client("TestClient", "TestNumber")
    data = {
        "client": client,
        "is_confirmed": True,
        "service_name": "Electrolysis",
        "price_in_cents_per_hour": 2200,
        "scheduled_start": datetime(2026, 8, 5, 14, 0),
        "estimated_end": datetime(2026, 8, 5, 15, 30),
        "actual_start": None,
        "actual_end": None

    }
    data.update(changes)
    return Appointment(**data)


def test_get_estimated_minutes():
    appointment = make_appointment()

    result = appointment.get_estimated_minutes()

    assert result == 90


def test_get_actual_minutes():
    result = make_appointment(actual_start=datetime(2026, 8, 5, 14, 00),
                              actual_end=datetime(2026, 8, 5, 15, 15)
                              ).get_actual_minutes()
    assert result == 75


def test_get_minutes_with_missing_data():
    appointment = make_appointment()
    appointment_two = make_appointment(actual_start=datetime(2026, 8, 5, 15, 30))
    appointment_three = make_appointment(actual_end=datetime(2026, 8, 5, 15, 30))

    result_with_no_actual_start_and_end = appointment.get_actual_minutes()
    result_with_no_actual_end = appointment_two.get_actual_minutes()
    result_with_no_actual_start = appointment_three.get_actual_minutes()
    assert result_with_no_actual_start_and_end is None
    assert result_with_no_actual_start is None
    assert result_with_no_actual_end is None


def test_appointment_with_negative_price_number():
    with pytest.raises(ValueError):
        make_appointment(price_in_cents_per_hour=-2)


def test_appointment_with_zero_price_number():
    with pytest.raises(ValueError):
        make_appointment(price_in_cents_per_hour=0)


def test_appointment_reject_price_in_string():
    with pytest.raises(TypeError):
        make_appointment(price_in_cents_per_hour="6000")
