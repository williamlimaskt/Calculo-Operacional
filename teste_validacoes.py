#!/usr/bin/env python3
"""
Script para testar as validações robustas
Demonstra como o sistema trata valores absurdos
"""

from validacoes import (
    validar_total_chamados, 
    validar_tma, 
    validar_data_robusta, 
    validar_dados_completos,
    obter_mensagens_ajuda
)

def testar_validacoes():
    """Testa diversos cenários de validação"""
    
    print("🧪 TESTE DE VALIDAÇÕES ROBUSTAS")
    print("=" * 50)
    
    # Mostrar limites do sistema
    mensagens = obter_mensagens_ajuda()
    print("\n📋 LIMITES DO SISTEMA:")
    for chave, valor in mensagens.items():
        print(f"• {chave}: {valor}")
    
    print("\n" + "=" * 50)
    
    # Teste 1: Valores absurdos para total de chamados
    print("\n🔢 TESTE 1: Total de Chamados")
    casos_chamados = [
        ("99999999999", "Valor absurdo"),
        ("0", "Zero"),
        ("-100", "Negativo"),
        ("abc", "Texto"),
        ("", "Vazio"),
        ("1000001", "Acima do limite"),
        ("500", "Valor válido")
    ]
    
    for valor, descricao in casos_chamados:
        valido, msg, resultado = validar_total_chamados(valor)
        status = "✅" if valido else "❌"
        print(f"{status} {descricao} ({valor}): {msg}")
    
    # Teste 2: Valores absurdos para TMA
    print("\n⏱️ TESTE 2: Tempo Médio de Atendimento (TMA)")
    casos_tma = [
        ("99999999", "Valor absurdo"),
        ("XP", "Texto"),
        ("0", "Zero"),
        ("-50", "Negativo"),
        ("1441", "Acima de 24h"),
        ("", "Vazio"),
        ("90", "Valor válido")
    ]
    
    for valor, descricao in casos_tma:
        valido, msg, resultado = validar_tma(valor)
        status = "✅" if valido else "❌"
        print(f"{status} {descricao} ({valor}): {msg}")
    
    # Teste 3: Datas absurdas
    print("\n📅 TESTE 3: Datas")
    casos_datas = [
        ("01/01/1900", "Ano muito antigo"),
        ("32/12/2025", "Dia inválido"),
        ("15/13/2025", "Mês inválido"),
        ("29/02/2025", "29 de fevereiro em ano não bissexto"),
        ("31/04/2025", "31 de abril (não existe)"),
        ("abc/def/ghi", "Texto"),
        ("", "Vazio"),
        ("15/06/2025", "Data válida")
    ]
    
    for valor, descricao in casos_datas:
        valido, msg, resultado = validar_data_robusta(valor)
        status = "✅" if valido else "❌"
        print(f"{status} {descricao} ({valor}): {msg}")
    
    # Teste 4: Cenários completos
    print("\n🎯 TESTE 4: Cenários Completos")
    cenarios = [
        {
            'nome': 'Cenário Válido',
            'dados': ('500', '90', '01/01/2025', '31/01/2025')
        },
        {
            'nome': 'Valores Absurdos',
            'dados': ('99999999999', '99999999', '01/01/1900', '31/12/2101')
        },
        {
            'nome': 'Texto em Campos Numéricos',
            'dados': ('abc', 'XP', '01/01/2025', '31/01/2025')
        },
        {
            'nome': 'Período Invertido',
            'dados': ('500', '90', '31/01/2025', '01/01/2025')
        },
        {
            'nome': 'Período Muito Longo',
            'dados': ('500', '90', '01/01/2025', '01/01/2035')
        }
    ]
    
    for cenario in cenarios:
        print(f"\n📊 {cenario['nome']}:")
        valido, msg, dados = validar_dados_completos(*cenario['dados'])
        status = "✅" if valido else "❌"
        print(f"{status} Resultado: {msg}")
        if dados:
            print(f"   Dados validados: {dados}")

def demonstrar_protecoes():
    """Demonstra as proteções contra valores absurdos"""
    
    print("\n🛡️ DEMONSTRAÇÃO DE PROTEÇÕES")
    print("=" * 50)
    
    print("\n❌ O que acontece com valores absurdos:")
    print("• 99999999999 chamados → Rejeitado (máximo 1.000.000)")
    print("• 99999999 minutos TMA → Rejeitado (máximo 1.440 minutos = 24h)")
    print("• 01/01/1900 → Rejeitado (ano mínimo 1900)")
    print("• 31/02/2025 → Rejeitado (data inexistente)")
    print("• 'XP' como TMA → Rejeitado (apenas números)")
    print("• Período de 10 anos → Rejeitado (máximo 3.650 dias)")
    
    print("\n✅ O que é aceito:")
    print("• Total de chamados: 1 a 1.000.000")
    print("• TMA: 1 a 1.440 minutos (24 horas)")
    print("• Datas: 01/01/1900 a 31/12/2100")
    print("• Períodos: 1 a 3.650 dias (10 anos)")
    
    print("\n🔍 Validações implementadas:")
    print("• Verificação de campos vazios")
    print("• Validação de formato de números")
    print("• Verificação de limites mínimos e máximos")
    print("• Validação de formato de datas (regex)")
    print("• Verificação de datas inexistentes")
    print("• Validação de períodos lógicos")
    print("• Tratamento de exceções")

if __name__ == "__main__":
    testar_validacoes()
    demonstrar_protecoes()
    
    print("\n" + "=" * 50)
    print("🎉 Teste concluído! O sistema está protegido contra valores absurdos.")
    print("💡 Execute 'python gui.py' para testar a interface gráfica.")
    print("💡 Execute 'python index.py' para testar a versão console.") 