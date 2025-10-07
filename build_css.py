import os
import re

# Ordem dos arquivos CSS baseada nas dependências
FILES = [
    # Base (fundação)
    "Base/_reset.css",
    "Base/_variables.css",
    "Base/_typography.css",
    "Base/_base.css",
    "Base/_utilities.css",
    
    # Layouts (estrutura principal)
    "Layouts/_grid.css",
    "Layouts/_dashboard.css",
    "Layouts/_auth.css",
    "Layouts/_responsive.css",
    
    # Components (elementos de UI - ordem por frequência de uso)
    "Components/_navbars.css",
    "Components/_sidebar.css",
    "Components/_buttons.css",
    "Components/_badges.css",
    "Components/_forms.css",
    "Components/_forms-filtro.css",
    "Components/_tables.css",
    "Components/_modals.css",
    "Components/_alerts.css",
    "Components/_cards.css",
    "Components/_progressbars.css",
    "Components/_charts.css",
    "Components/_kamban.css",
    "Components/_footer.css",
    
    # Themes (temas - o padrão primeiro)
    "Themes/_default.css",
    "Themes/_dark.css",
    "Themes/_high-contrast.css",
    
    # Vendors (bibliotecas externas)
    "Vendors/dataTables.css",
    "Vendors/_chartjs.css",
]

INPUT_DIR = "projeto\static\css"
OUTPUT_FILE = "projeto\static/css/main.min.css"
OUTPUT_FILE_DEV = "projeto\static/css/main.css"  # Versão desenvolvimento (não minificada)

def minify_css(css: str) -> str:
    """Remove comentários, espaços e quebras de linha para reduzir tamanho."""
    # Remove comentários /* ... */
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    # Remove espaços extras
    css = re.sub(r"\s+", " ", css)
    # Remove espaço antes/depois de {} ; : ,
    css = re.sub(r"\s*([{};:,])\s*", r"\1", css)
    # Remove último ponto e vírgula
    css = re.sub(r";\s*}", "}", css)
    # Remove espaços no começo/fim
    return css.strip()

def build_main_css():
    print("🔨 Concatenando arquivos CSS...")
    combined_css = ""
    missing_files = []

    for fname in FILES:
        path = os.path.join(INPUT_DIR, fname)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                css_content = f.read()
                # Adiciona comentário com nome do arquivo (apenas na versão dev)
                combined_css += f"\n/* === {fname} === */\n" + css_content + "\n"
            print(f"✅ {fname}")
        else:
            print(f"⚠️  Aviso: {fname} não encontrado")
            missing_files.append(fname)

    # Salvar versão desenvolvimento (não minificada)
    with open(OUTPUT_FILE_DEV, "w", encoding="utf-8") as out:
        out.write(combined_css)
    print(f"✅ Arquivo de desenvolvimento gerado: {OUTPUT_FILE_DEV}")

    # Minificação para produção
    minified_css = minify_css(combined_css)

    # Salvar versão minificada
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(minified_css)

    # Estatísticas
    original_size = len(combined_css.encode('utf-8'))
    minified_size = len(minified_css.encode('utf-8'))
    reduction = ((original_size - minified_size) / original_size) * 100

    print(f"✅ Arquivo de produção gerado: {OUTPUT_FILE}")
    print(f"📊 Estatísticas:")
    print(f"   - Tamanho original: {original_size:,} bytes")
    print(f"   - Tamanho minificado: {minified_size:,} bytes")
    print(f"   - Redução: {reduction:.1f}%")
    
    if missing_files:
        print(f"⚠️  Arquivos não encontrados: {len(missing_files)}")
        for missing in missing_files:
            print(f"   - {missing}")

def check_css_structure():
    """Verifica se a estrutura de diretórios está correta"""
    print("🔍 Verificando estrutura de diretórios...")
    
    required_dirs = ["Base", "Components", "Layouts", "Themes", "Vendors"]
    for dir_name in required_dirs:
        dir_path = os.path.join(INPUT_DIR, dir_name)
        if os.path.exists(dir_path):
            print(f"✅ Diretório {dir_name}/ encontrado")
        else:
            print(f"❌ Diretório {dir_name}/ não encontrado")

if __name__ == "__main__":
    print("🚀 Iniciando build do CSS...")
    check_css_structure()
    print("\n" + "="*50)
    build_main_css()
    print("\n🎉 Build concluído!")