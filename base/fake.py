from random import randint, choice
from string import ascii_uppercase, digits

def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)

def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(choice(ascii_uppercase + digits) for _ in range(randint(start, end)))