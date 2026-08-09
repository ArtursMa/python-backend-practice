import json

from client import Client


def load_clients(file_name: str) -> list[Client]:
    client_list = []
    try:
        with open(file_name, "r") as file:
            data_from_json = json.load(file)
            for client in data_from_json:
                client_list.append(Client(**client))

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Wrong JSON file")
        return []
    return client_list


def save_clients(clients: list[Client], file_name: str) -> None:
    pass


def add_client(client: Client, file_name: str) -> None:
    pass


# my_clients = load_clients("clients.json")
# print(my_clients)
