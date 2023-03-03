import uuid
from random import randint


def generate_pass() -> str:
    int_pass = randint(1000, 9999)
    password = ''
    for i in (str(uuid.uuid4()).split('-')):
        password += i + str(int_pass)
    return password

