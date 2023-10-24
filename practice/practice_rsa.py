import rsa
import time

public_key, private_key = rsa.newkeys(1024)

# The code is creating a new file called "public_key.pem" and writing the contents of the public key
# in PEM format to that file. --wb(write byte)
# save_pkcs1("PEM"), which converts the public key into PEM (Privacy Enhanced Mail) format, 
# a widely used format for storing X.509 certificates and cryptographic keys.
with open("public_key.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

# The code is creating a new file called "private_key.pem" and writing the contents of the private key
# in PEM format to that file.
with open("private_key.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open("public_key.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private_key.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# The code is encrypting the message "Hello my password is bussyboo343" using the RSA encryption
# algorithm.
message1= "Hello my password is bussyboo343"

start_time = time.time()
# The line `encrypt_mess = rsa.encrypt(message1.encode(), public_key)` is encrypting the message
# `message1` using the RSA encryption algorithm.
encrypt_mess = rsa.encrypt(message1.encode(), public_key)
encrypt_time = time.time() - start_time

print("The encrypted data is: ", encrypt_mess)

with open("encrypted.message1", "wb") as f:
    f.write(encrypt_mess)


# decrypting the message
encrypt_mess1 = open("encrypted.message1", "rb").read()

start_time = time.time()
decrypt_message = rsa.decrypt(encrypt_mess, private_key)
decrypt_time = time.time() - start_time

print("Decrypted message: ", decrypt_message.decode())

print("Encryption Time:", encrypt_time, "seconds")
print("Decryption Time:", decrypt_time, "seconds")