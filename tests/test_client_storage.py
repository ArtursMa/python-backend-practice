import json

import pytest

from client import Client
import client_storage

test_data = [
    {
        "name": "Anna",
        "phone": "+371111111",
        "is_active": True,
    },
    {
        "name": "Nina",
        "phone": "+371222222",
        "is_active": False,
    },
]


def test_load_clients_from_valid_json(tmp_path):
    test_client_list = [Client(**client) for client in test_data]
    file_path = tmp_path / "clients.json"
    with open(file_path, "w") as file:
        json.dump(test_data, file)

    result = client_storage.load_clients(file_path)
    assert result == test_client_list


def test_load_clients_failed_no_file():
    result = client_storage.load_clients("wrong_file_path")
    assert result == []


def test_load_clients_from_wrong_json_file(tmp_path):
    file_path = tmp_path/"client_storage_wrong.json"
    with open(file_path, "w") as file:
        file.write("{,,}")
    result = client_storage.load_clients(file_path)
    assert result == []
