def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'e' to encrypt a message or 'd' to decrypt a message: ").strip().lower()
    message = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    if choice == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'd':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
