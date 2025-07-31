"""
Módulo para cálculos de calendário e dias úteis
"""

import datetime
from workalendar.america import Brazil

def calcular_dias_uteis_periodo(data_inicio, data_fim):
    """
    Calcula o total de dias úteis em um período específico
    usando a biblioteca workalendar (considerando feriados brasileiros)
    
    Args:
        data_inicio (datetime.date): Data de início do período
        data_fim (datetime.date): Data de fim do período
        
    Returns:
        int: Número de dias úteis no período
    """
    # Criar calendário brasileiro (inclui feriados nacionais)
    cal = Brazil()
    
    # Calcular dias úteis manualmente para maior precisão
    dias_uteis = 0
    data_atual = data_inicio
    
    while data_atual <= data_fim:
        # Verificar se é dia útil (não feriado e não fim de semana)
        if not cal.is_holiday(data_atual) and data_atual.weekday() < 5:
            dias_uteis += 1
        data_atual += datetime.timedelta(days=1)
    
    return dias_uteis

def calcular_dias_uteis(mes, ano):
    """
    Calcula o total de dias úteis em um mês específico
    usando a biblioteca workalendar (considerando feriados brasileiros)
    
    Args:
        mes (int): Mês (1-12)
        ano (int): Ano (1900-2100)
        
    Returns:
        int: Número de dias úteis no mês
    """
    # Obter o primeiro e último dia do mês
    primeiro_dia = datetime.date(ano, mes, 1)
    
    # Calcular o último dia do mês
    if mes == 12:
        ultimo_dia = datetime.date(ano + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        ultimo_dia = datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)
    
    return calcular_dias_uteis_periodo(primeiro_dia, ultimo_dia)

def validar_data(data_str):
    """
    Valida se uma data no formato DD/MM/AAAA é válida
    
    Args:
        data_str (str): Data no formato DD/MM/AAAA
        
    Returns:
        tuple: (bool, str, datetime.date) - (válido, mensagem, data)
    """
    try:
        # Verificar formato
        if len(data_str.split('/')) != 3:
            return False, "Formato inválido. Use DD/MM/AAAA", None
        
        dia, mes, ano = map(int, data_str.split('/'))
        
        # Validar ranges
        if dia < 1 or dia > 31:
            return False, "Dia deve estar entre 1 e 31", None
        
        if mes < 1 or mes > 12:
            return False, "Mês deve estar entre 1 e 12", None
        
        if ano < 1900 or ano > 2100:
            return False, "Ano deve estar entre 1900 e 2100", None
        
        # Testar se a data é válida
        data = datetime.date(ano, mes, dia)
        return True, "Data válida", data
        
    except ValueError:
        return False, "Data inválida", None

def validar_mes_ano(mes, ano):
    """
    Valida se o mês e ano informados são válidos
    
    Args:
        mes (int): Mês (1-12)
        ano (int): Ano (1900-2100)
        
    Returns:
        tuple: (bool, str) - (válido, mensagem)
    """
    try:
        if mes < 1 or mes > 12:
            return False, "Mês deve estar entre 1 e 12"
        
        if ano < 1900 or ano > 2100:
            return False, "Ano deve estar entre 1900 e 2100"
        
        # Testar se a data é válida
        datetime.date(ano, mes, 1)
        return True, "Data válida"
        
    except ValueError:
        return False, "Data inválida"

def mostrar_feriados_periodo(data_inicio, data_fim):
    """
    Mostra os feriados em um período específico
    
    Args:
        data_inicio (datetime.date): Data de início do período
        data_fim (datetime.date): Data de fim do período
        
    Returns:
        list: Lista de datas dos feriados
    """
    cal = Brazil()
    feriados = []
    data_atual = data_inicio
    
    while data_atual <= data_fim:
        if cal.is_holiday(data_atual):
            feriados.append(data_atual)
        data_atual += datetime.timedelta(days=1)
    
    return feriados

def mostrar_feriados_mes(mes, ano):
    """
    Mostra os feriados do mês especificado
    
    Args:
        mes (int): Mês (1-12)
        ano (int): Ano (1900-2100)
        
    Returns:
        list: Lista de datas dos feriados
    """
    primeiro_dia = datetime.date(ano, mes, 1)
    
    if mes == 12:
        ultimo_dia = datetime.date(ano + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        ultimo_dia = datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)
    
    return mostrar_feriados_periodo(primeiro_dia, ultimo_dia)

def obter_total_dias_periodo(data_inicio, data_fim):
    """
    Obtém o total de dias em um período
    
    Args:
        data_inicio (datetime.date): Data de início do período
        data_fim (datetime.date): Data de fim do período
        
    Returns:
        int: Total de dias no período (inclusive)
    """
    return (data_fim - data_inicio).days + 1

def obter_total_dias_mes(mes, ano):
    """
    Obtém o total de dias em um mês
    
    Args:
        mes (int): Mês (1-12)
        ano (int): Ano (1900-2100)
        
    Returns:
        int: Total de dias no mês
    """
    if mes == 12:
        return 31
    else:
        return (datetime.date(ano, mes + 1, 1) - datetime.date(ano, mes, 1)).days 