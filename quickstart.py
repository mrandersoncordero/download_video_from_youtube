import os
from pydrive.auth import GoogleAuth

file_path = './credentials_module.json'

# Verificar si el archivo existe
if os.path.exists(file_path):
    os.remove(file_path) # eliminar el archivo
    print(f"El archivo {file_path} ha sido eliminado.")
else:
    print(f"El archivo {file_path} no existe.")

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

