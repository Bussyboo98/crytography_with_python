# RSA  (Rivest-Shamir-Adleman) algorithm implements Asymmetric Key Cryptography. It uses two keys 
# for encryption and decryption of text – a public and a private key.

import rsa

#generaye public and private key
# In practice, 512 bits is quite small and not recommended for secure applications. Longer key 
# lengths (e.g., 2048 or 4096 bits) are typically used for better security.
public_key, private_key = rsa.newkeys(2048)

plainText = input("Enter the plain text to be encrypted: ")

# It takes the plain text as input, encodes it into bytes using the `encode()` method, 
# and then encrypts it using the public key.
encrypt_data = rsa.encrypt(plainText.encode(), public_key)

# It takes the encrypted data (`encrypt_data`) and the private key as input, and 
# then decrypts the data using the RSA algorithm.
decrypt_data = rsa.decrypt(encrypt_data, private_key).decode()

print("The primordial string: ", plainText)
print("The Encrypted message: ", encrypt_data)  
print("The Decrypted message: ", decrypt_data)



# Keep in mind that RSA is widely used but may not be suitable for all scenarios. 
# For more robust security, it's important to consider key management, key length, and the 
# specific security requirements of your application. Additionally, modern applications may
# consider hybrid encryption techniques that combine the advantages of symmetric and asymmetric encryption.

# Hybrid encryption is a technique that combines the strengths of both symmetric and asymmetric 
# encryption to provide secure and efficient data encryption in modern applications. The core idea
# behind hybrid encryption is to use asymmetric encryption for securely exchanging a shared secret key, 
# and then use that shared secret key to perform fast and efficient symmetric encryption for the actual data.