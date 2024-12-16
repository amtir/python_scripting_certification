import re
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# You must store this key securely. Anyone with this key can decrypt your data.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def is_valid_reference_id(reference_id):
    # Check if the Reference ID is exactly 12 characters long and contains only alphanumeric characters
    pattern = re.compile(r'^[a-zA-Z0-9]{12}$')
    return bool(pattern.match(reference_id))

def encrypt_reference_id(reference_id):
    # Encrypt the Reference ID
    encrypted_id = cipher_suite.encrypt(reference_id.encode())
    return encrypted_id

def decrypt_reference_id(encrypted_id):
    # Decrypt the Reference ID
    decrypted_id = cipher_suite.decrypt(encrypted_id).decode()
    return decrypted_id

def main():
    # Read input from the command line
    reference_id = input("Enter the Reference ID (12 alphanumeric characters): ")
    
    # Validate the Reference ID
    if not is_valid_reference_id(reference_id):
        print("Invalid Reference ID. It should be exactly 12 alphanumeric characters.")
        return
    
    # Encrypt the Reference ID
    encrypted_id = encrypt_reference_id(reference_id)
    print(f"Encrypted Reference ID: {encrypted_id}")
    
    # Ask user if they want to decrypt it
    choice = input("Do you want to decrypt the Reference ID? (yes/no): ")
    if choice.lower() == 'yes':
        decrypted_id = decrypt_reference_id(encrypted_id)
        print(f"Decrypted Reference ID: {decrypted_id}")

if __name__ == "__main__":
    main()
