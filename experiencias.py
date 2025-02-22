import os

# Caminho do ficheiro
caminho_ficheiro = "caminho/do/teu/ficheiro.txt"

# Verificar se o ficheiro existe
if os.path.isfile(caminho_ficheiro):
    print("O ficheiro existe.")
else:
    print("O ficheiro não existe.")
