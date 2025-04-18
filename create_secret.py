import secrets

sk = secrets.token_bytes(36)  

print(sk.hex())