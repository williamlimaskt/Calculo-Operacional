#!/usr/bin/env python3
"""
Arquivo principal para executar a interface gráfica
Validador de Dias Úteis - V1.1
"""

import sys
import os

# Adicionar o diretório atual ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from interface_gui import main
    print("=== Calculador de Headcount - V1.1 ===")
    print("Iniciando interface gráfica...")
    main()
except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    print("Certifique-se de que todos os arquivos estão no mesmo diretório.")
    input("Pressione Enter para sair...")
except Exception as e:
    print(f"Erro inesperado: {e}")
    input("Pressione Enter para sair...") 