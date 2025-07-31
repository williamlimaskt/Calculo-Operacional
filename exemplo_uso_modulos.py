"""
Exemplo de como usar os módulos separadamente
"""

# Exemplo 1: Usar apenas o módulo de calendário (período personalizado)
print("=== EXEMPLO 1: CÁLCULO DE DIAS ÚTEIS POR PERÍODO ===")
from calendario_utils import calcular_dias_uteis_periodo, mostrar_feriados_periodo
import datetime

# Período personalizado
data_inicio = datetime.date(2024, 12, 1)
data_fim = datetime.date(2024, 12, 31)

dias_uteis = calcular_dias_uteis_periodo(data_inicio, data_fim)
feriados = mostrar_feriados_periodo(data_inicio, data_fim)

print(f"Período: {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}")
print(f"Dias úteis: {dias_uteis}")
print(f"Feriados: {len(feriados)}")
for feriado in feriados:
    print(f"  - {feriado.strftime('%d/%m/%Y')}")

print("\n" + "="*50)

# Exemplo 2: Usar apenas o módulo de cálculos operacionais
print("=== EXEMPLO 2: APENAS CÁLCULOS OPERACIONAIS ===")
from calculos_operacionais import calcular_metricas_operacionais, formatar_tempo_minutos

total_chamados = 500
tma = 90  # minutos
dias_uteis = 22

metricas = calcular_metricas_operacionais(total_chamados, tma, dias_uteis)

print(f"Total de chamados: {total_chamados}")
print(f"TMA: {tma} minutos")
print(f"Dias úteis: {dias_uteis}")
print(f"Tempo total necessário: {formatar_tempo_minutos(metricas['tempo_total'])}")
print(f"Capacidade operacional: {metricas['capacidade_operacional']:.0f} chamados/mês")
print(f"Pessoas necessárias: {int(metricas['pessoas_necessarias'])}")

print("\n" + "="*50)

# Exemplo 3: Usar módulos em conjunto (período personalizado)
print("=== EXEMPLO 3: MÓDULOS EM CONJUNTO (PERÍODO PERSONALIZADO) ===")
from calendario_utils import calcular_dias_uteis_periodo, obter_total_dias_periodo
from calculos_operacionais import calcular_metricas_operacionais, calcular_percentual_dias_uteis
import datetime

# Dados de exemplo com período personalizado
data_inicio = datetime.date(2025, 7, 1)
data_fim = datetime.date(2025, 7, 31)

dados_exemplo = {
    'total_chamados': 800,
    'tma': 120
}

# Calcular dias úteis
dias_uteis = calcular_dias_uteis_periodo(data_inicio, data_fim)
total_dias = obter_total_dias_periodo(data_inicio, data_fim)

# Calcular métricas
metricas = calcular_metricas_operacionais(
    dados_exemplo['total_chamados'],
    dados_exemplo['tma'],
    dias_uteis
)

# Calcular percentual
percentual = calcular_percentual_dias_uteis(dias_uteis, total_dias)

# Exibir resultados
print(f"Análise para período {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}:")
print(f"  - Dias úteis: {dias_uteis}/{total_dias} ({percentual:.1f}%)")
print(f"  - Capacidade: {metricas['capacidade_operacional']:.0f} chamados/período")
print(f"  - Pessoas necessárias: {int(metricas['pessoas_necessarias'])}")

print("\n" + "="*50)

# Exemplo 4: Função personalizada usando os módulos (período personalizado)
def analise_rapida_periodo(total_chamados, tma, data_inicio, data_fim):
    """
    Função personalizada que usa os módulos para análise rápida por período
    """
    from calendario_utils import calcular_dias_uteis_periodo
    from calculos_operacionais import calcular_metricas_operacionais
    
    dias_uteis = calcular_dias_uteis_periodo(data_inicio, data_fim)
    metricas = calcular_metricas_operacionais(total_chamados, tma, dias_uteis)
    
    return {
        'dias_uteis': dias_uteis,
        'pessoas_necessarias': metricas['pessoas_necessarias'],
        'capacidade': metricas['capacidade_operacional']
    }

print("=== EXEMPLO 4: FUNÇÃO PERSONALIZADA (PERÍODO) ===")
import datetime
data_inicio = datetime.date(2025, 8, 1)
data_fim = datetime.date(2025, 8, 31)
resultado = analise_rapida_periodo(600, 100, data_inicio, data_fim)
print(f"Análise rápida para período {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}: {resultado}")

# Exemplo 5: Período que cruza meses/anos
print("\n=== EXEMPLO 5: PERÍODO QUE CRUZA MESES/ANOS ===")
data_inicio = datetime.date(2024, 12, 15)
data_fim = datetime.date(2025, 1, 15)
resultado = analise_rapida_periodo(500, 90, data_inicio, data_fim)
print(f"Análise para período longo {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}: {resultado}") 