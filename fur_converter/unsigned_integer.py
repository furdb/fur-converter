from flask import request, Blueprint

id = 'unsigned_integer'

unsigned_integer = Blueprint(id, __name__)


@unsigned_integer.get(f"/{id}/encode")
def encode():
    data = request.args.get("data", '0')
    size = request.args.get("size", '1')

    data = int(data)
    binary = bin(data)[2:]

    size = int(size)
    rem = size - len(binary)
    resized_binary = ('0' * rem) + binary

    return resized_binary


@unsigned_integer.get(f"/{id}/decode")
def decode():
    binary = request.args.get("binary", '0')

    data = int(binary, 2)
    data = str(data)

    return data


@unsigned_integer.get(f"/{id}/compare")
def compare():
    a = request.args.get("a", '0')
    b = request.args.get("b", '0')

    a = int(a, 2)
    b = int(b, 2)

    if a < b:
        return "1"
    elif a > b:
        return "-1"
    else:
        return "0"
