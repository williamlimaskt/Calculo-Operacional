"""
Módulo para cálculos operacionais e métricas de negócio
"""

def calcular_metricas_operacionais(total_chamados, tma, dias_uteis):
    """
    Calcula as métricas operacionais baseadas nos parâmetros fornecidos
    
    Args:
        total_chamados (int): Total de chamados a serem atendidos
        tma (int): Tempo médio de atendimento em minutos
        dias_uteis (int): Número de dias úteis no período
        
    Returns:
        dict: Dicionário com todas as métricas calculadas
    """
    # Constantes
    HORAS_POR_DIA = 7.5
    MINUTOS_POR_HORA = 60
    
    # Cálculos
    tempo_total = total_chamados * tma
    horas_uteis_mes = dias_uteis * (HORAS_POR_DIA * MINUTOS_POR_HORA)
    capacidade_operacional = horas_uteis_mes / tma
    pessoas_necessarias = tempo_total / horas_uteis_mes
    
    return {
        'tempo_total': tempo_total,
        'horas_uteis_mes': horas_uteis_mes,
        'capacidade_operacional': capacidade_operacional,
        'pessoas_necessarias': pessoas_necessarias
    }

def calcular_percentual_dias_uteis(dias_uteis, total_dias):
    """
    Calcula o percentual de dias úteis
    
    Args:
        dias_uteis (int): Número de dias úteis
        total_dias (int): Total de dias no período
        
    Returns:
        float: Percentual de dias úteis
    """
    return (dias_uteis / total_dias) * 100

def calcular_dias_nao_uteis(total_dias, dias_uteis):
    """
    Calcula o número de dias não úteis
    
    Args:
        total_dias (int): Total de dias no período
        dias_uteis (int): Número de dias úteis
        
    Returns:
        int: Número de dias não úteis
    """
    return total_dias - dias_uteis

def formatar_tempo_minutos(minutos):
    """
    Formata tempo em minutos para uma string legível
    
    Args:
        minutos (int): Tempo em minutos
        
    Returns:
        str: Tempo formatado
    """
    if minutos < 60:
        return f"{minutos} minutos"
    elif minutos < 1440:  # Menos de 1 dia
        horas = minutos // 60
        mins = minutos % 60
        return f"{horas}h {mins}min"
    else:
        dias = minutos // 1440
        horas = (minutos % 1440) // 60
        mins = minutos % 60
        return f"{dias}d {horas}h {mins}min" 