# # Cryptocode is a library, which is basically a collection of modules.  It is the simplest 
# way of encryption and decryption as it is more suitable  for people wanting a mere abstraction.
# The encryption has two parameters – the string to be encoded and the key to decrypt the encoded string

import cryptocode

plain_text = input("Enter your text: ")
password = input("Enter the password: ")

# `encryptData = cryptocode.encrypt(plain_text, password)` is encrypting the `plain_text` using the
# `password` provided. The encrypted data is then stored in the variable `encryptData`.
encryptData = cryptocode.encrypt(plain_text, password)

#printing encrypted data
print("Encrypted data: ", encryptData)

decryptedData = cryptocode.decrypt(encryptData, password)
 
# Displaying the decrypted data
print("Decrypted data: ",decryptedData)