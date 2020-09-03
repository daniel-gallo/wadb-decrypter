# WhatsApp DB Decryptor
## Requirements
- The computer should have access to the phone via adb.
- Note that root is required to fetch the key, which is needed for decryption.
- To install the requirements just run the following.

```bash
pip3 install -r requirements.txt
```
## Extraction of the database

`extractor.py` will get the files `msgstore.db.crypt12` and `key`.

```bash
python3 extractor.py
```
## Decryption of the database
`decrypter.py`  assumes that the files `msgstore.db.crypt12` and `key` are on the same directory as `decrypter.py` and will output `msgstore.db`.

```bash
python3 decrypter.py
```
To specify other paths pass them as parameters.
```bash
python3 decrypter.py --key my_key --input crypted_database.db.crypt12 --output decrypted_database.db
```