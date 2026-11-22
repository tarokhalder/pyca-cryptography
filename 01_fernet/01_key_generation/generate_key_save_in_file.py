from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("secret.key", "wb") as file:
    file.write(key)

print("Saved in file")

with open("secret.key", "rb") as file:
    loaded_key = file.read()

print(loaded_key)
