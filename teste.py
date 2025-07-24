# teste.py
import os

def listar_estrutura_diretorios(caminho, prefixo=""):
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)
        if os.path.isdir(caminho_completo):
            print(f"{prefixo}📁 {item}/")
            listar_estrutura_diretorios(caminho_completo, prefixo + "    ")
        else:
            print(f"{prefixo}📄 {item}")

# Caminho inicial (por exemplo, o diretório onde está o manage.py)
caminho_inicial = os.path.dirname(os.path.abspath(__file__))
print(f"Estrutura de diretórios do projeto Django em: {caminho_inicial}\n")
listar_estrutura_diretorios(caminho_inicial)
