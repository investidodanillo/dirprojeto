import os

# Caminho base da pasta
base_path = r"projeto\static"  # ou use os.path.join para compatibilidade multiplataforma

for root, dirs, files in os.walk(base_path):
    # Calcula nível de profundidade (para identação)
    level = root.replace(base_path, '').count(os.sep)
    indent = '    ' * level

    # Nome da pasta atual
    folder_name = os.path.basename(root)
    print(f"{indent}[DIR] {folder_name}")

    # Lista os arquivos dentro da pasta atual
    sub_indent = '    ' * (level + 1)
    for f in files:
        print(f"{sub_indent}- {f}")
