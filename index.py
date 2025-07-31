# Importar módulos
from calendario_utils import (
    calcular_dias_uteis_periodo, 
    validar_data, 
    mostrar_feriados_periodo, 
    obter_total_dias_periodo
)
from calculos_operacionais import calcular_metricas_operacionais
from interface_usuario import obter_dados_entrada, exibir_resultados, exibir_erro

def main():
    """Função principal do programa"""
    # Obter dados de entrada
    dados = obter_dados_entrada()
    if dados is None:
        return
    
    # Validação das datas
    valido_inicio, msg_inicio, data_inicio = validar_data(dados['data_inicio_str'])
    if not valido_inicio:
        exibir_erro(f"Data de início: {msg_inicio}")
        return
    
    valido_fim, msg_fim, data_fim = validar_data(dados['data_fim_str'])
    if not valido_fim:
        exibir_erro(f"Data de fim: {msg_fim}")
        return
    
    # Verificar se data de fim é posterior à data de início
    if data_fim < data_inicio:
        exibir_erro("A data de fim deve ser posterior à data de início")
        return

    # Calcular dias úteis
    dias_uteis = calcular_dias_uteis_periodo(data_inicio, data_fim)
    
    # Calcular métricas operacionais
    metricas = calcular_metricas_operacionais(
        dados['total_chamados'], 
        dados['tma'], 
        dias_uteis
    )

    # Obter feriados do período
    feriados = mostrar_feriados_periodo(data_inicio, data_fim)
    
    # Obter total de dias no período
    total_dias = obter_total_dias_periodo(data_inicio, data_fim)

    # Exibir resultados
    exibir_resultados(dados, metricas, dias_uteis, feriados, total_dias, data_inicio, data_fim)

if __name__ == "__main__":
    main()