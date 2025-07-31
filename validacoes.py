"""
Módulo para validações robustas de entrada de dados
"""

import datetime
import re

# Constantes para limites
LIMITES = {
    'TOTAL_CHAMADOS_MIN': 1,
    'TOTAL_CHAMADOS_MAX': 10000,  # 1 milhão
    'TMA_MIN': 1,
    'TMA_MAX': 1440,  # 24 horas em minutos
    'ANO_MIN': 1901,
    'ANO_MAX': 2100,
    'PERIODO_MAX_DIAS': 3650,  # 10 anos
    'PERIODO_MIN_DIAS': 1
}

def validar_numero_inteiro(valor_str, nome_campo, min_valor=None, max_valor=None):
    """
    Valida se um valor é um número inteiro válido dentro dos limites
    
    Args:
        valor_str (str): Valor a ser validado
        nome_campo (str): Nome do campo para mensagens de erro
        min_valor (int): Valor mínimo permitido
        max_valor (int): Valor máximo permitido
        
    Returns:
        tuple: (bool, str, int) - (válido, mensagem, valor)
    """
    try:
        # Verificar se é um número
        if not valor_str.strip():
            return False, f"{nome_campo} não pode estar vazio", None
            
        # Verificar se contém apenas dígitos
        if not valor_str.isdigit():
            return False, f"{nome_campo} deve conter apenas números", None
            
        valor = int(valor_str)
        
        # Verificar limites
        if min_valor is not None and valor < min_valor:
            return False, f"{nome_campo} deve ser maior ou igual a {min_valor}", None
            
        if max_valor is not None and valor > max_valor:
            return False, f"{nome_campo} deve ser menor ou igual a {max_valor}", None
            
        return True, "Valor válido", valor
        
    except ValueError:
        return False, f"{nome_campo} deve ser um número inteiro válido", None
    except Exception as e:
        return False, f"Erro ao validar {nome_campo}: {str(e)}", None

def validar_total_chamados(valor_str):
    """
    Valida o total de chamados
    
    Args:
        valor_str (str): Valor a ser validado
        
    Returns:
        tuple: (bool, str, int) - (válido, mensagem, valor)
    """
    return validar_numero_inteiro(
        valor_str, 
        "Total de chamados",
        LIMITES['TOTAL_CHAMADOS_MIN'],
        LIMITES['TOTAL_CHAMADOS_MAX']
    )

def validar_tma(valor_str):
    """
    Valida o tempo médio de atendimento (TMA)
    
    Args:
        valor_str (str): Valor a ser validado
        
    Returns:
        tuple: (bool, str, int) - (válido, mensagem, valor)
    """
    return validar_numero_inteiro(
        valor_str,
        "Tempo médio de atendimento",
        LIMITES['TMA_MIN'],
        LIMITES['TMA_MAX']
    )

def validar_data_robusta(data_str):
    """
    Validação robusta de data no formato DD/MM/AAAA
    
    Args:
        data_str (str): Data no formato DD/MM/AAAA
        
    Returns:
        tuple: (bool, str, datetime.date) - (válido, mensagem, data)
    """
    try:
        # Verificar se não está vazio
        if not data_str.strip():
            return False, "Data não pode estar vazia", None
            
        # Verificar formato com regex
        if not re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', data_str):
            return False, "Formato inválido. Use DD/MM/AAAA", None
        
        # Separar componentes
        partes = data_str.split('/')
        if len(partes) != 3:
            return False, "Formato inválido. Use DD/MM/AAAA", None
            
        dia_str, mes_str, ano_str = partes
        
        # Validar se são números
        if not (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit()):
            return False, "Data deve conter apenas números", None
            
        dia, mes, ano = int(dia_str), int(mes_str), int(ano_str)
        
        # Validar ranges básicos
        if dia < 1 or dia > 31:
            return False, "Dia deve estar entre 1 e 31", None
        
        if mes < 1 or mes > 12:
            return False, "Mês deve estar entre 1 e 12", None
        
        if ano < LIMITES['ANO_MIN'] or ano > LIMITES['ANO_MAX']:
            return False, f"Ano deve estar entre {LIMITES['ANO_MIN']} e {LIMITES['ANO_MAX']}", None
        
        # Validar datas específicas (ex: 31/02/2025)
        try:
            data = datetime.date(ano, mes, dia)
        except ValueError:
            return False, "Data inválida (ex: 31/02 não existe)", None
            
        return True, "Data válida", data
        
    except Exception as e:
        return False, f"Erro ao validar data: {str(e)}", None

def validar_periodo_datas(data_inicio, data_fim):
    """
    Valida se o período entre duas datas é válido
    
    Args:
        data_inicio (datetime.date): Data de início
        data_fim (datetime.date): Data de fim
        
    Returns:
        tuple: (bool, str) - (válido, mensagem)
    """
    try:
        # Verificar se data de fim é posterior à data de início
        if data_fim < data_inicio:
            return False, "A data de fim deve ser posterior à data de início"
            
        # Verificar se o período não é muito longo
        dias_periodo = (data_fim - data_inicio).days + 1
        if dias_periodo > LIMITES['PERIODO_MAX_DIAS']:
            return False, f"Período muito longo. Máximo de {LIMITES['PERIODO_MAX_DIAS']} dias"
            
        if dias_periodo < LIMITES['PERIODO_MIN_DIAS']:
            return False, f"Período muito curto. Mínimo de {LIMITES['PERIODO_MIN_DIAS']} dia"
            
        return True, "Período válido"
        
    except Exception as e:
        return False, f"Erro ao validar período: {str(e)}"

def validar_dados_completos(total_chamados_str, tma_str, data_inicio_str, data_fim_str):
    """
    Valida todos os dados de entrada de uma vez
    
    Args:
        total_chamados_str (str): Total de chamados
        tma_str (str): Tempo médio de atendimento
        data_inicio_str (str): Data de início
        data_fim_str (str): Data de fim
        
    Returns:
        tuple: (bool, str, dict) - (válido, mensagem, dados_validados)
    """
    try:
        # Validar total de chamados
        valido_chamados, msg_chamados, total_chamados = validar_total_chamados(total_chamados_str)
        if not valido_chamados:
            return False, msg_chamados, None
            
        # Validar TMA
        valido_tma, msg_tma, tma = validar_tma(tma_str)
        if not valido_tma:
            return False, msg_tma, None
            
        # Validar data de início
        valido_inicio, msg_inicio, data_inicio = validar_data_robusta(data_inicio_str)
        if not valido_inicio:
            return False, f"Data de início: {msg_inicio}", None
            
        # Validar data de fim
        valido_fim, msg_fim, data_fim = validar_data_robusta(data_fim_str)
        if not valido_fim:
            return False, f"Data de fim: {msg_fim}", None
            
        # Validar período
        valido_periodo, msg_periodo = validar_periodo_datas(data_inicio, data_fim)
        if not valido_periodo:
            return False, msg_periodo, None
            
        # Retornar dados validados
        dados_validados = {
            'total_chamados': total_chamados,
            'tma': tma,
            'data_inicio': data_inicio,
            'data_fim': data_fim
        }
        
        return True, "Todos os dados são válidos", dados_validados
        
    except Exception as e:
        return False, f"Erro inesperado na validação: {str(e)}", None

def obter_mensagens_ajuda():
    """
    Retorna mensagens de ajuda para o usuário
    
    Returns:
        dict: Dicionário com mensagens de ajuda
    """
    return {
        'total_chamados': f"Digite um número entre {LIMITES['TOTAL_CHAMADOS_MIN']:,} e {LIMITES['TOTAL_CHAMADOS_MAX']:,}",
        'tma': f"Digite um número entre {LIMITES['TMA_MIN']} e {LIMITES['TMA_MAX']} minutos (máximo 24 horas)",
        'data': f"Use o formato DD/MM/AAAA (ano entre {LIMITES['ANO_MIN']} e {LIMITES['ANO_MAX']})",
        'periodo': f"Período deve ter entre {LIMITES['PERIODO_MIN_DIAS']} e {LIMITES['PERIODO_MAX_DIAS']} dias"
    } 