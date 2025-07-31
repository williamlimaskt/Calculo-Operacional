#!/usr/bin/env python3
"""
Script para gerar o executável do Calculo Operacional V1.1
"""

import os
import subprocess
import sys

def main():
    print("🔨 Gerando executável do Calculo Operacional V1.1...")
    
    # Verificar se PyInstaller está instalado
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado!")
    except ImportError:
        print("❌ PyInstaller não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado com sucesso!")
    
    # Comando para gerar o executável
    cmd = [
        "pyinstaller",
        "--onefile",                    # Arquivo único
        "--windowed",                   # Sem console (GUI)
        "--name=Calculo_Operacional_V1.1",  # Nome do executável
        "--add-data=README.md;.",       # Incluir README
        "--add-data=VERSION.md;.",      # Incluir VERSION
        "--icon=icon.ico",              # Ícone (se existir)
        "gui.py"                        # Arquivo principal
    ]
    
    # Remover opções que podem não existir
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    print("📦 Executando PyInstaller...")
    print(f"Comando: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("\n🎉 Executável gerado com sucesso!")
        print("📁 Arquivo criado em: dist/Calculo_Operacional_V1.1.exe")
        print("\n📋 Próximos passos:")
        print("1. O executável está em: dist/Calculo_Operacional_V1.1.exe")
        print("2. Você pode copiar este arquivo para qualquer computador Windows")
        print("3. Não é necessário ter Python instalado no computador de destino")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao gerar executável: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main() 