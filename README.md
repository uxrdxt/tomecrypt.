# TomeCrypt

TomeCrypt is a Python script for symmetric file encryption and decryption using security keys.

## Features
- Encrypt files with a symmetric key
- Decrypt encrypted files using the same key
- Generate secure symmetric keys

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/TomeCrypt.git
   cd TomeCrypt

2.Install dependencies:  
     
     pip install -r requirements.txt

## Usage
Encrypt a File
     
     python tomecrypt.py -e <input_file> <key_file>

Decrypt a File

     python tomecrypt.py -d <input_file> <key_file>

Generate a Symmetric Key

     python tomecrypt.py -g <key_file>



TomeCrypt - Command-Line Usage




Usage:      python3 tomecrypt.py [-h] [-e] [-d] [-g] [file] [key_file]




Encrypt or decrypt files using security keys.

Arguments:
file File to be encrypted or decrypted
key_file Security key file

Options:
-h, --help Show this help message and exit
-e, --encrypt Encrypt a file
-d, --decrypt Decrypt an encrypted file
-g, --generate-key Generate a symmetric key
