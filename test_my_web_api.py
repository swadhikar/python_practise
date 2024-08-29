import requests
import json 


def test_read_root():
    url: str = "http://localhost:8000/"
    response = requests.get(url)
    return json.loads(response.content.decode())


def test_read_item(endpoint: str):
    url: str = f'http://localhost:8000/{endpoint}'
    response = requests.get(url)
    return json.loads(response.content.decode())


if __name__ == '__main__':
    return_dict = test_read_root()
    print("Get full response:\n", json.dumps(return_dict, indent=4))
    return_dict = test_read_item(r'items/user')
    print("Get items/user response:\n", json.dumps(return_dict, indent=4))

