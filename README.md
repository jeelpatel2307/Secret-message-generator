# Secret Message Generator

Welcome to the Secret Message Generator! This Python project provides a simple program that generates and decrypts secret messages using a basic encryption algorithm.

## How to Use

1. Run the script (`secret_message_generator.py`).
2. The program will generate a random secret key for encryption.
3. Enter your message when prompted.
4. The program will encrypt the message and display the result.
5. The program will then decrypt the encrypted message using the generated key and display the original message.

## Features

### `SecretMessageGenerator` Class

- Manages the generation of a secret key and the encryption/decryption of messages.
- Uses a basic Caesar Cipher algorithm for encryption.

### Methods

### `generate_key()`

- Generates a random key for encryption.

### `encrypt_message(message)`

- Encrypts a user-provided message using a simple Caesar Cipher algorithm.

### `decrypt_message()`

- Decrypts the stored secret message using the stored key.

## Example Usage

```python
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

```

## Additional Considerations

- **Algorithm:**
    - The project uses a basic Caesar Cipher algorithm. For increased security, explore more advanced encryption techniques.
- **User Input:**
    - Validate user input for messages to ensure proper encryption and decryption.
- **Error Handling:**
    - Consider implementing error handling for unexpected scenarios.

## Author

Jeel patel
