import json
from client import Client
from dataclasses import asdict


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

    data_list = [asdict(client) for client in clients]
    with open(file_name, "w") as file:
        json.dump(data_list, file)





def add_client(client: Client, file_name: str) -> None:
    pass


# my_clients = load_clients("clients.json")
# print(my_clients)
