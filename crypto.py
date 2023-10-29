from tkinter import Label
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

message = b'Hello :D'
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

cyphertext = key.public_key().encrypt(message, 
padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256(),algorithm=hashes.SHA256(),label=None)))

print(cyphertext)
