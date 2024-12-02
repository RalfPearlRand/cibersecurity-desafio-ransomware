import os
import hashlib
from cryptography.fernet import Fernet

def decrypt_directory():
    current_dir = os.getcwd()
    
    # Gerar chave usando SHA256
    key = hashlib.sha256(b"testeransomwares").digest()
    fernet_key = Fernet.generate_key()
    cipher_suite = Fernet(fernet_key)
    
    for filename in os.listdir(current_dir):
        if filename.endswith('.ransomwaretroll'):
            try:
                file_path = os.path.join(current_dir, filename)
                
                with open(file_path, "rb") as file:
                    file_data = file.read()
                
                decrypt_data = cipher_suite.decrypt(file_data)
                
                os.remove(file_path)
                
                original_filename = filename[:-16]
                new_file_path = os.path.join(current_dir, original_filename)
                
                with open(new_file_path, "wb") as new_file:
                    new_file.write(decrypt_data)
                
                print(f"Descriptografado: {filename}")
            except Exception as e:
                print(f"Erro ao descriptografar {filename}: {e}")

decrypt_directory()
