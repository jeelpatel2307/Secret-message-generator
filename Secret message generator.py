import random

class SecretMessageGenerator:
    def __init__(self):
        # Initialize the SecretMessageGenerator with an empty key and message
        self.secret_key = None
        self.secret_message = None

    def generate_key(self):
        # Generate a random key for encryption
        self.secret_key = random.randint(1, 25)

    def encrypt_message(self, message):
        # Encrypt the message using a simple Caesar Cipher algorithm
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shift = self.secret_key % 26
                if char.isupper():
                    encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        self.secret_message = encrypted_message

    def decrypt_message(self):
        # Decrypt the stored secret message using the stored key
        decrypted_message = ""
        if self.secret_key is not None and self.secret_message is not None:
            for char in self.secret_message:
                if char.isalpha():
                    shift = self.secret_key % 26
                    if char.isupper():
                        decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
                    else:
                        decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
                    decrypted_message += decrypted_char
                else:
                    decrypted_message += char
            return decrypted_message
        else:
            return None

if __name__ == '__main__':
    # Example usage
    secret_message_generator = SecretMessageGenerator()

    # Generate a secret key
    secret_message_generator.generate_key()

    # User input for the message
    user_message = input("Enter your message: ")

    # Encrypt the message
    secret_message_generator.encrypt_message(user_message)
    print(f"Encrypted Message: {secret_message_generator.secret_message}")

    # Decrypt the message
    decrypted_message = secret_message_generator.decrypt_message()
    print(f"Decrypted Message: {decrypted_message}")
