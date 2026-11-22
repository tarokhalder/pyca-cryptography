from cryptography.fernet import Fernet

with open("secret.key" ,"rb") as file:
    key = file.read()

fernet = Fernet(key)

msg = "Hello , How are You?"

encrypted = fernet.encrypt(msg.encode())

print(msg)
print(encrypted)
