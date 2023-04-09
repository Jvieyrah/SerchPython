import sys

def txt_importer(path_file):
    """Aqui irá sua implementação"""
# Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem Formato inválido na stderr;
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")

# A função deve retornar uma lista contendo as linhas do arquivo.
    try:
        with open(path_file, "r") as file:
            data = file.readlines()
        data = [line.strip("\n") for line in data]
        return data
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
