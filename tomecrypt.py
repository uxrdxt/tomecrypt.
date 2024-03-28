import argparse
import os
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_symmetric_key():
    return secrets.token_bytes(32)  # 256-bit key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key_from_file(filename):
    with open(filename, 'rb') as f:
        key_data = f.read()
    return key_data

def encrypt_file_symmetric(key, input_file, output_file):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(iv)
        while True:
            chunk = f_in.read(1024)
            if not chunk:
                break
            encrypted_chunk = encryptor.update(chunk)
            f_out.write(encrypted_chunk)
        f_out.write(encryptor.finalize())

def decrypt_file_symmetric(key, input_file, output_file):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        iv = f_in.read(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        while True:
            chunk = f_in.read(1024)
            if not chunk:
                break
            decrypted_chunk = decryptor.update(chunk)
            f_out.write(decrypted_chunk)
        f_out.write(decryptor.finalize())

def generate_and_save_key(filename):
    key = generate_symmetric_key()
    save_key_to_file(key, filename + ".key")  # Append ".key" to the filename
    print(f"Key generated and saved to {filename}.key")

def parse_arguments():
    parser = argparse.ArgumentParser(description="TomeCrypt - Encrypt or decrypt files using security keys")
    parser.add_argument("-e", "--encrypt", help="Encrypt a file", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Decrypt a file", action="store_true")
    parser.add_argument("-g", "--generate-key", help="Generate a symmetric key", action="store_true")
    parser.add_argument("file", nargs="?")
    parser.add_argument("key_file", nargs="?")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.generate_key:
        if args.file:
            generate_and_save_key(args.file)
        else:
            print("Please provide a filename for the key.")
        return

    if args.encrypt:
        if args.file and args.key_file:
            filename = args.file
            key_filename = args.key_file
            if not os.path.isfile(key_filename):
                print("Error: Key file not found.")
                return
            key = load_key_from_file(key_filename)
            output_file = os.path.splitext(filename)[0] + ".encrypted"
            encrypt_file_symmetric(key, filename, output_file)
            print("File encrypted successfully.")
        else:
            print("Please provide both the file and key file for encryption.")
    
    if args.decrypt:
        if args.file and args.key_file:
            filename = args.file
            key_filename = args.key_file
            if not os.path.isfile(key_filename):
                print("Error: Key file not found.")
                return
            key = load_key_from_file(key_filename)
            output_file = os.path.splitext(filename)[0] + ".txt" if filename.endswith(".encrypted") else filename
            decrypt_file_symmetric(key, filename, output_file)
            print("File decrypted successfully.")
        else:
            print("Please provide both the file and key file for decryption.")

if __name__ == "__main__":
    main()
