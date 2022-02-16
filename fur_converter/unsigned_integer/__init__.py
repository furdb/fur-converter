from unicodedata import decimal
from flask import request, Blueprint

unsigned_integer = Blueprint('unsigned_integer', __name__)


@unsigned_integer.get("/unsigned_integer/encode")
def encode():
    data = request.args.get("data", '0')

    data = int(data)
    binary = bin(data)[2:]
    binary = str(binary)

    return {"binary": binary}


@unsigned_integer.get("/unsigned_integer/decode")
def decode():
    binary = request.args.get("binary", '0')

    data = int(binary, 2)
    data = str(data)

    return {"data": data}
