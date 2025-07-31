"""
Inputs / Interface

"""

def obter_dados_entrada():
    """
    Obtém os dados de entrada do usuário com validações robustas
    
    Returns:
        dict: Dicionário com os dados informados ou None se inválido
    """
    try:
        from validacoes import validar_dados_completos, obter_mensagens_ajuda
        
        # Mostrar limites
        mensagens = obter_mensagens_ajuda()
        print("📋 LIMITES DO SISTEMA:")
        print(f"• {mensagens['total_chamados']}")
        print(f"• {mensagens['tma']}")
        print(f"• {mensagens['data']}")
        print(f"• {mensagens['periodo']}")
        print()
        
        # Obter dados
        total_chamados_str = input("Digite o total de chamados: ")
        tma_str = input("Digite o tempo médio de atendimento em minutos: ")
        
        print("\nInforme o período para análise:")
        data_inicio_str = input("Data de início (DD/MM/AAAA): ")
        data_fim_str = input("Data de fim (DD/MM/AAAA): ")
        
        # Validar todos os dados
        valido, mensagem, dados_validados = validar_dados_completos(
            total_chamados_str, tma_str, data_inicio_str, data_fim_str
        )
        
        if not valido:
            print(f"❌ Erro: {mensagem}")
            return None
            
        # Converter para formato esperado pelo sistema
        return {
            'total_chamados': dados_validados['total_chamados'],
            'tma': dados_validados['tma'],
            'data_inicio_str': data_inicio_str,
            'data_fim_str': data_fim_str
        }
        
    except ImportError:
        print("Erro: Módulo de validações não encontrado.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        return None

def exibir_resultados(dados, metricas, dias_uteis, feriados, total_dias, data_inicio, data_fim):
    """
    Exibe os resultados dos cálculos
    
    Args:
        dados (dict): Dados de entrada
        metricas (dict): Métricas calculadas
        dias_uteis (int): Número de dias úteis
        feriados (list): Lista de feriados
        total_dias (int): Total de dias no período
        data_inicio (datetime.date): Data de início
        data_fim (datetime.date): Data de fim
    """
    # Resultados principais
    print("\n=== RESULTADOS ===")
    print(f"Total de chamados: {dados['total_chamados']}")
    print(f"Tempo médio de atendimento: {dados['tma']} minutos")
    print(f"Período: {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}")
    print(f"Dias úteis no período: {dias_uteis}")
    print(f"Tempo total necessário: {metricas['tempo_total']} minutos")
    print(f"Tempo útil no período: {metricas['horas_uteis_mes']} minutos")
    print(f"A capacidade operacional é de {metricas['capacidade_operacional']:.0f} chamados por período")
    print(f"Pessoas necessárias: {metricas['pessoas_necessarias']:.3f}")
    
    # Feriados
    if feriados:
        print(f"\nFeriados no período:")
        for feriado in feriados:
            print(f"  - {feriado.strftime('%d/%m/%Y')} ({feriado.strftime('%A')})")
    else:
        print(f"\nNenhum feriado no período")
    
    # Análise adicional
    from calculos_operacionais import calcular_percentual_dias_uteis, calcular_dias_nao_uteis
    
    dias_nao_uteis = calcular_dias_nao_uteis(total_dias, dias_uteis)
    percentual = calcular_percentual_dias_uteis(dias_uteis, total_dias)
    
    print(f"\n=== ANÁLISE ADICIONAL ===")
    print(f"Total de dias no período: {total_dias}")
    print(f"Dias não úteis (fins de semana + feriados): {dias_nao_uteis}")
    print(f"Percentual de dias úteis: {percentual:.1f}%")

def exibir_erro(mensagem):
    """
    Exibe mensagem de erro
    
    Args:
        mensagem (str): Mensagem de erro
    """
    print(f"Erro: {mensagem}")

def exibir_sucesso(mensagem):
    """
    Exibe mensagem de sucesso
    
    Args:
        mensagem (str): Mensagem de sucesso
    """
    print(f"✅ {mensagem}") 