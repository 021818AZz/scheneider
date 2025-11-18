#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para padronizar cores em todos os arquivos HTML
Substitui cores antigas pelas cores do esquema azul/preto/verde
"""

import os
import re
from pathlib import Path

# Diretório com os arquivos HTML
BASE_DIR = r"c:\Users\us\Desktop\zarck"

# Mapeamento de cores antigas para novas
COLOR_MAP = {
    # Verde para azul (cores principais)
    "#35c85b": "#3b82f6",      # Verde para azul
    "#85e06a": "#1e3a8a",      # Verde claro para azul escuro
    "#1fe3a2": "#3b82f6",      # Turquesa para azul
    "#043c5a": "#ffffff",      # Azul escuro para branco
    "#2d649f": "#1e3a8a",      # Azul indigo para azul
    
    # Gradientes verdes para azuis
    "linear-gradient(51deg, #85e06a, #85e06a, #1fe3a2)": "linear-gradient(135deg, #1e3a8a, #3b82f6)",
    "linear-gradient(51deg, #85e06a, #85e06a, #1fe3a2) !important": "linear-gradient(135deg, #1e3a8a, #3b82f6) !important",
    "linear-gradient(135deg, #85e06a, #1fe3a2)": "linear-gradient(135deg, #1e3a8a, #3b82f6)",
    "linear-gradient(135deg, #85e06a, #1fe3a2) !important": "linear-gradient(135deg, #1e3a8a, #3b82f6) !important",
    
    # RGB para hex
    "rgb(53, 200, 91)": "#3b82f6",
    "rgba(53, 200, 91": "rgba(59, 130, 246",  # Aproximação
    
    # Texto em shadow/opacity
    "rgba(0, 0, 0 / 30%)": "rgba(0, 0, 0, 0.3)",
}

def standardize_colors(file_path):
    """Lê um arquivo e substitui as cores"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar substituições em ordem (maiores primeiro para evitar conflitos)
        for old_color, new_color in COLOR_MAP.items():
            content = content.replace(old_color, new_color)
        
        # Se houve mudanças, gravar o arquivo
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Atualizado: {file_path}")
            return True
        else:
            print(f"- Nenhuma mudança: {file_path}")
            return False
    
    except Exception as e:
        print(f"✗ Erro ao processar {file_path}: {e}")
        return False

def main():
    """Processa todos os arquivos HTML"""
    html_files = list(Path(BASE_DIR).glob("*.html"))
    
    if not html_files:
        print(f"Nenhum arquivo HTML encontrado em {BASE_DIR}")
        return
    
    print(f"Processando {len(html_files)} arquivos HTML...")
    print("-" * 60)
    
    updated_count = 0
    for html_file in sorted(html_files):
        if standardize_colors(str(html_file)):
            updated_count += 1
    
    print("-" * 60)
    print(f"Total de arquivos atualizados: {updated_count}/{len(html_files)}")

if __name__ == "__main__":
    main()
