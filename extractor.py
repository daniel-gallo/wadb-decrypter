from os import system


def run(command: str):
    return_code = system(command)

    if return_code != 0:
        exit(1)


# Fetch latest database
print("Fetching database...")
run("adb pull /sdcard/WhatsApp/Databases/msgstore.db.crypt12 .")

# Fetch database key (root needed).
# We have to temporary store the key file on /sdcard so we can fetch it with adb.
print("Fetching database key...")
run("adb shell 'su -c cp /data/data/com.whatsapp/files/key /sdcard/key'")
run("adb pull /sdcard/key key")
run("adb shell 'rm /sdcard/key'")
