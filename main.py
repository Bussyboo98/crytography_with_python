# implementing cryptography in Python using the Fernet module.

# Fernet module comes under the cryptography package. Here, a unique key is generated without which
# the data cannot be read/modified. Hence it implements Symmetric Key Cryptography

from cryptography.fernet import Fernet

# The code `key = Fernet.generate_key()` generates a unique encryption key using the Fernet module.
# This key is used to encrypt and decrypt data.
key = Fernet.generate_key()
f = Fernet(key)

plainText = input("Enter your text to be encrypted: ").encode()
encryptedData = f.encrypt(plainText)


#encrypting the ciphertext
print("The encrypted data is: ", encryptedData)


# Decrypting the ciphertext
decryptedData = f.decrypt(encryptedData)

# Printing the decrypted data by converting it from byte to string
print("The decrypted data is: ", decryptedData.decode())


