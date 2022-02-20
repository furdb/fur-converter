from flask import request, Blueprint

id = 'long_string'

long_string = Blueprint(id, __name__)


@long_string.get(f"/{id}/encode")
def encode():
    data = request.args.get("data", '0')
    size = request.args.get("size", '1')

    binary = ""
    for c in data:
        cur = ""
        cur += bin(ord(c))[2:]
        while len(cur) < 8:
            cur = '0' + cur
        binary += cur
        print(ord(c), bin(ord(c)))

    size = int(size)
    rem = size - len(binary)
    resized_binary = binary + ('0' * rem)

    return resized_binary


@long_string.get(f"/{id}/decode")
def decode():
    binary = request.args.get("binary", '0')

    binary = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    trimmed_binary = ""

    for c in binary:
        if int(c, 2) == 0:
            break
        trimmed_binary += chr(int(c, 2))

    data = ''.join(trimmed_binary)

    return data
