from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print(key)

generate_key()    
