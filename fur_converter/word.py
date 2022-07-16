from flask import request, Blueprint

id = 'word'

word = Blueprint(id, __name__)

encoder = {
    "": "0000",
    "a": "0001",
    "l": "0010",
    "e": "0011",
    "u": "0100",
    "i": "0101",
    "c": "0110",
    "o": "0111",
    "t": "1000",
    "n": "1001",
    "m": "1010",
    "r": "1011",
    "s": "1100",
    "v": "1101",
    "p": "1110",
    "g": "11110000",
    "d": "11110001",
    "b": "11110010",
    "q": "11110011",
    "h": "11110100",
    "k": "11110101",
    "w": "11110110",
    "y": "11110111",
    "x": "11111000",
    "z": "11111001",
}

decoder = {
    "0000": "",
    "0001": "a",
    "0010": "l",
    "0011": "e",
    "0100": "u",
    "0101": "i",
    "0110": "c",
    "0111": "o",
    "1000": "t",
    "1001": "n",
    "1010": "m",
    "1011": "r",
    "1100": "s",
    "1101": "v",
    "1110": "p",
    "1111": {
        "0000": "g",
        "0001": "d",
        "0010": "b",
        "0011": "q",
        "0100": "h",
        "0101": "k",
        "0110": "w",
        "0111": "y",
        "1000": "x",
        "1001": "z",
    }
}

@word.get(f"/{id}/encode")
def encode():
    data = request.args.get("data", '0')
    size = request.args.get("size", '1')

    binary = ""
    for c in data:
        binary += encoder.get(c)

    size = int(size)
    rem = size - len(binary)
    resized_binary = binary + ('0' * rem)

    return resized_binary


@word.get(f"/{id}/decode")
def decode():
    binary = request.args.get("binary", '0')

    binary = [binary[i:i+4] for i in range(0, len(binary), 4)]
    print(binary)

    data = ""

    i = 0
    while i < len(binary):
        if binary[i] == "1111":
            print("AT_1111", i, binary[i])
            i += 1
            data += decoder.get("1111").get(binary[i])
        else:
            print("NO_1111", i, binary[i])
            data += decoder.get(binary[i])
        i += 1

    return data


@word.get(f"/{id}/compare")
def compare():
    a = request.args.get("a", '0')
    b = request.args.get("b", '0')

    a = encode(a)
    b = encode(b)

    if a < b:
        return "1"
    elif a > b:
        return "-1"
    else:
        return "0"
