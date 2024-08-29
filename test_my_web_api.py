import requests
import json


def test_read_root():
    url: str = "http://localhost:8000/"
    response = requests.get(url)
    assert json.loads(response.content.decode()) == {
                                                        "hello": "Hello world!",
                                                        "user": {
                                                            "name": "swadhikar",
                                                            "company": "TEL",
                                                            "age": 34
                                                        }
                                                    }

def test_read_item():
    url: str = f'http://localhost:8000/items/user'
    response = requests.get(url)
    assert json.loads(response.content.decode()) == {
                                                        "name": "swadhikar",
                                                        "company": "TEL",
                                                        "age": 34
                                                    }

    

