from Crypto.Cipher import AES
from zlib import decompress
from sys import stderr
from argparse import ArgumentParser


def abort(message: str):
    stderr.write(f"[!] {message}")
    exit(1)


def decrypt(ket_filename: str, input_filename: str, output_filename: str):
    print(f"[+] Reading {ket_filename}...")
    with open(ket_filename, "rb") as key_file:
        key_file.seek(30)
        t1 = key_file.read(32)
        key_file.seek(126)
        ket_filename = key_file.read(32)

    with open(input_filename, "rb") as input_database:
        input_database.seek(3)
        t2 = input_database.read(32)
        if t1 != t2:
            abort("Key does not match with database")

        input_database.seek(51)
        iv = input_database.read(16)

        print(f"[+] Reading {input_filename}...")
        input_database.seek(67)
        data = input_database.read()[:-20]

        print(f"[+] Decrypting {input_filename}...")
        decipher = AES.new(ket_filename, AES.MODE_GCM, iv)
        sqlite = decompress(decipher.decrypt(data))
        if sqlite[:6].decode("ascii") != "SQLite":
            abort("Decryption failed")

        print(f"[+] Writing decrypted data to {output_filename}")
        with open(output_filename, "wb") as output_database:
            output_database.write(sqlite)


def main():
    parser = ArgumentParser()
    parser.add_argument("--key", help="specify the key filename", default="key")
    parser.add_argument("--input", help="specify the encrypted database filename", default="msgstore.db.crypt12")
    parser.add_argument("--output", help="specify the decrypted database filename", default="msgstore.db")
    args = parser.parse_args()

    decrypt(args.key, args.input, args.output)


if __name__ == "__main__":
    main()
