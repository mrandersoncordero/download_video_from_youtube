import os

directory = 'assets'

# Listar solo archivos
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
print("Archivos:", files)
