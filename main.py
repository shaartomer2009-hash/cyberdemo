"""
Author: Tomer Shaar

Program Name: Encrypt/Decrypt

Description:
"""

import sys

#encoding dictionary
ENCODE_TABLE = {
    "A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41, "G": 42, "H": 43, "I": 44,
    "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63,
    "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69, "Y": 10, "Z": 11,
    "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18, "h": 19, "i": 30,
    "j": 31, "k": 32, "l": 33, "m": 34, "n": 35, "o": 36, "p": 37, "q": 38, "r": 39,
    "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95, "y": 96, "z": 97,
    " ": 98, ",": 99, ".": 100, "'": 101, "!": 102, "-": 103
}

#reversed dictionary
DECODE_TABLE = {v: k for k, v in ENCODE_TABLE.items()}


def encode_text(text: str) -> str:
    if not text:
        return ""
    encoded_values = []
    for ch in text:
        if ch in ENCODE_TABLE:
            encoded_values.append(str(ENCODE_TABLE[ch]))
        else:
            raise ValueError(f"Invalid character: {repr(ch)}")
    return ",".join(encoded_values)


def decode_text(data: str) -> str:
    if not data.strip():
        return ""
    result = []
    for num in data.split(","):
        if not num.strip():
            continue
        try:
            val = int(num)
        except ValueError:
            raise ValueError(f"Invalid number: {num}")
        result.append(DECODE_TABLE.get(val, ""))
    return "".join(result)


def assert_tests():
    #asserts
    assert encode_text("") == ""
    assert decode_text("") == ""

    sample = "Hi"
    assert decode_text(encode_text(sample)) == sample

    text2 = "Hi, tomer."
    assert decode_text(encode_text(text2)) == text2

    print("All asserts passed.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python cipher_tool.py [encrypt|decrypt]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "encrypt":
        message = input("Enter message to encrypt: ")
        try:
            cipher = encode_text(message)
            with open("encrypted_msg.txt", "w") as f:
                f.write(cipher)
            print("Message saved to 'encrypted_msg.txt'.")
        except Exception as err:
            print(f"Error during encryption: {err}")

    elif command == "decrypt":
        try:
            with open("encrypted_msg.txt", "r") as f:
                content = f.read().strip()
            plain = decode_text(content)
            print("Decrypted message:", plain)
        except FileNotFoundError:
            print("File 'encrypted_msg.txt' not found.")
        except Exception as err:
            print(f"Error during decryption: {err}")
    else:
        print("Invalid command. Use 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    assert_tests()
    main()
