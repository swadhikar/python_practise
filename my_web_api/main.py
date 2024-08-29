from fastapi import FastAPI


app = FastAPI()

RESPONSE = {
    "hello": "Hello world!",
    "user": {
        "name": "swadhikar",
        "company": "TEL",
        "age": 34
    }
}

@app.get("/")
def read_root() -> dict:
    return RESPONSE

@app.get('/items/{item_id}')
def get_item(item_id: str) -> object:
    return RESPONSE[item_id]