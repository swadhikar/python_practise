import math 

class InvalidUserDataException(Exception):
    pass

def add(num_1: int, num_2: int) -> int:
    return num_1 + num_2 


# def square_root(num: float) -> float:
#     assert math.sqrt(num)

def multiply_numbers(args: list[int]) -> int:
    product = 1
    for arg in args:
        product *= arg
    return product

def add_numbers(args: list[int]) -> int:
    summation = 0
    for arg in args:
        summation += arg
    return summation

def is_substring(text: str, search_text: str) -> bool:
    return search_text.lower() in text.lower()

def process_user_data(user_data: dict) -> bool:
    """
        Process user data. Raises InvalidUserDataException if data is invalid.
        :param user_data: Dictionary with user information
    """
    if not user_data.get("name"):
        raise InvalidUserDataException("User name is required")
    
    if not isinstance(user_data.get("age"), int) or user_data["age"] <= 0:
        raise InvalidUserDataException("Invalid age")
    
    # Process the data
    return True