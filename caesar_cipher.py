




✅ caesar_cipher.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if _name_ == "_main_":
    print("=== Caesar Cipher Encryption/Decryption ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' or 'd'.")
    else:
        message = input("Enter your message: ")
        shift = int(input("Enter the shift key (number): "))

        if choice == 'e':
            encrypted = encrypt(message, shift)
            print(f"Encrypted message: {encrypted}")
        else:
            decrypted = decrypt(message, shift)
            print(f"Decrypted message: {decrypted}")

