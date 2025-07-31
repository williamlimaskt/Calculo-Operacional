# Calculador de HeadCount

> **Versão:** V1.1.0 | **Status:** 🔄 Em Desenvolvimento

Este projeto tem o foco em calcular o HeadCout com base na LIB  `workalendar` para calcular dias úteis considerando feriados brasileiros.

## 🚀 **Nova Funcionalidade: Períodos Personalizados**

O sistema agora permite calcular dias úteis para **qualquer período personalizado**, não apenas meses completos!

## 🖥️ **Interface Gráfica (V1.1)**

Agora disponível uma **interface gráfica moderna** com:
- ✅ Campos de entrada intuitivos
- ✅ Validação em tempo real
- ✅ Resultados organizados
- ✅ Lista de feriados integrada
- ✅ Botões de ação (Calcular, Limpar, Sair)
- ✅ Design responsivo e profissional

## 🛡️ **Validações Robustas (V1.1)**

O sistema agora possui **validações completas** que protegem contra:
- ❌ **Valores absurdos**: 99999999999 chamados → Rejeitado (máximo 1.000.000)
- ❌ **TMA inválido**: "XP" ou 99999999 minutos → Rejeitado (máximo 24h)
- ❌ **Datas absurdas**: 01/01/1900 ou 31/02/2025 → Rejeitado
- ❌ **Períodos inválidos**: Datas invertidas ou muito longos → Rejeitado
- ❌ **Campos vazios**: Validação de entrada obrigatória
- ❌ **Formato incorreto**: Apenas números em campos numéricos

**Limites do Sistema:**
- 🔢 **Total de chamados**: 1 a 1.000.000
- ⏱️ **TMA**: 1 a 1.440 minutos (24 horas)
- 📅 **Datas**: 01/01/1901 a 31/12/2100
- 📊 **Períodos**: 1 a 3.650 dias (10 anos)

## Instalação

Primeiro, instale a biblioteca workalendar:

```bash
pip install workalendar
```

## Arquivos do Projeto

### 📁 Estrutura Modular

O projeto foi organizado em módulos separados para facilitar a manutenção e reutilização:

#### 1. `index.py` - Programa Principal
Arquivo principal que orquestra todos os módulos.

**Uso:**
```bash
python index.py
```

#### 2. `calendario_utils.py` - Utilitários de Calendário
Módulo para cálculos de dias úteis e feriados.

**Funcionalidades:**
- `calcular_dias_uteis_periodo(data_inicio, data_fim)` - Calcula dias úteis por período
- `calcular_dias_uteis(mes, ano)` - Calcula dias úteis por mês
- `validar_data(data_str)` - Valida data no formato DD/MM/AAAA
- `mostrar_feriados_periodo(data_inicio, data_fim)` - Lista feriados por período
- `obter_total_dias_periodo(data_inicio, data_fim)` - Total de dias por período

**Uso:**
```python
from calendario_utils import calcular_dias_uteis_periodo
import datetime

data_inicio = datetime.date(2024, 12, 1)
data_fim = datetime.date(2024, 12, 31)
dias = calcular_dias_uteis_periodo(data_inicio, data_fim)
print(f"Dias úteis: {dias}")
```

#### 3. `calculos_operacionais.py` - Cálculos de Negócio
Módulo para métricas operacionais.

**Funcionalidades:**
- `calcular_metricas_operacionais()` - Métricas completas
- `calcular_percentual_dias_uteis()` - Percentual
- `formatar_tempo_minutos()` - Formatação de tempo

**Uso:**
```python
from calculos_operacionais import calcular_metricas_operacionais

metricas = calcular_metricas_operacionais(500, 90, 22)
print(f"Pessoas necessárias: {metricas['pessoas_necessarias']}")
```

#### 4. `interface_usuario.py` - Interface do Usuário
Módulo para entrada e saída de dados.

**Funcionalidades:**
- `obter_dados_entrada()` - Coleta dados
- `exibir_resultados()` - Mostra resultados
- `exibir_erro()` - Tratamento de erros

#### 5. `exemplo_uso_modulos.py` - Exemplos de Uso
Demonstra como usar os módulos separadamente.

**Uso:**
```bash
python exemplo_uso_modulos.py
```

#### 6. `interface_gui.py` - Interface Gráfica (V1.1)
Interface gráfica moderna usando tkinter.

**Uso:**
```bash
python gui.py
```

#### 7. `gui.py` - Executor da Interface Gráfica
Arquivo principal para executar a GUI.

#### 8. `validacoes.py` - Validações Robustas (V1.1)
Módulo para validação de entrada de dados com limites e proteções.

**Funcionalidades:**
- Validação de números inteiros com limites
- Validação robusta de datas
- Verificação de períodos lógicos
- Proteção contra valores absurdos
- Mensagens de erro detalhadas

#### 9. `teste_validacoes.py` - Teste de Validações
Script para testar todas as validações do sistema.



## Como Funciona

### 🆕 Nova Funcionalidade: Períodos Personalizados

O sistema agora permite calcular dias úteis para **qualquer período personalizado**, não apenas meses completos:

- **Data de início**: Qualquer data no formato DD/MM/AAAA
- **Data de fim**: Qualquer data posterior à data de início
- **Períodos que cruzam meses/anos**: Totalmente suportado
- **Validação automática**: Verifica se as datas são válidas

### Cálculo de Dias Úteis

A biblioteca `workalendar` considera:
- **Fins de semana**: Sábados e domingos
- **Feriados nacionais brasileiros**: Incluindo feriados móveis (Carnaval, Páscoa, etc.)

### Feriados Brasileiros Incluídos

- 1º de Janeiro (Ano Novo)
- 21 de Abril (Tiradentes)
- 1º de Maio (Dia do Trabalho)
- 7 de Setembro (Independência)
- 12 de Outubro (Nossa Senhora Aparecida)
- 2 de Novembro (Finados)
- 15 de Novembro (Proclamação da República)
- 25 de Dezembro (Natal)
- Carnaval (móvel)
- Sexta-feira Santa (móvel)
- Páscoa (móvel)
- Corpus Christi (móvel)

## Exemplos de Uso

### 🎯 Uso dos Módulos Separadamente

#### Exemplo 1: Cálculo de Dias Úteis por Período
```python
from calendario_utils import calcular_dias_uteis_periodo
import datetime

data_inicio = datetime.date(2024, 12, 1)
data_fim = datetime.date(2024, 12, 31)
dias = calcular_dias_uteis_periodo(data_inicio, data_fim)
print(f"Dias úteis no período: {dias}")
```

#### Exemplo 2: Apenas Cálculos Operacionais
```python
from calculos_operacionais import calcular_metricas_operacionais

metricas = calcular_metricas_operacionais(500, 90, 22)
print(f"Pessoas necessárias: {metricas['pessoas_necessarias']:.2f}")
```

#### Exemplo 3: Função Personalizada por Período
```python
def analise_rapida_periodo(total_chamados, tma, data_inicio, data_fim):
    from calendario_utils import calcular_dias_uteis_periodo
    from calculos_operacionais import calcular_metricas_operacionais
    
    dias_uteis = calcular_dias_uteis_periodo(data_inicio, data_fim)
    metricas = calcular_metricas_operacionais(total_chamados, tma, dias_uteis)
    
    return {
        'dias_uteis': dias_uteis,
        'pessoas_necessarias': metricas['pessoas_necessarias']
    }

import datetime
data_inicio = datetime.date(2025, 8, 1)
data_fim = datetime.date(2025, 8, 31)
resultado = analise_rapida_periodo(600, 100, data_inicio, data_fim)
print(resultado)
```

### 📚 Exemplos Avançados

#### Exemplo 4: Cálculo Simples (Workalendar Direto)
```python
from workalendar.america import Brazil
import datetime

cal = Brazil()
inicio = datetime.date(2024, 12, 1)
fim = datetime.date(2024, 12, 31)
dias_uteis = cal.get_working_days_delta(inicio, fim)
print(f"Dias úteis em dezembro/2024: {dias_uteis}")
```

### Exemplo 2: Verificar se é Feriado
```python
from workalendar.america import Brazil
import datetime

cal = Brazil()
data = datetime.date(2024, 12, 25)  # Natal
if cal.is_holiday(data):
    print("É feriado!")
```

### Exemplo 3: Listar Feriados do Mês
```python
from workalendar.america import Brazil
import datetime

cal = Brazil()
mes = 12
ano = 2024

primeiro_dia = datetime.date(ano, mes, 1)
ultimo_dia = datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)

feriados = []
data_atual = primeiro_dia
while data_atual <= ultimo_dia:
    if cal.is_holiday(data_atual):
        feriados.append(data_atual)
    data_atual += datetime.timedelta(days=1)

for feriado in feriados:
    print(f"Feriado: {feriado.strftime('%d/%m/%Y')}")
```

## Vantagens do Workalendar

1. **Precisão**: Considera feriados reais do Brasil
2. **Feriados móveis**: Calcula automaticamente Carnaval, Páscoa, etc.
3. **Flexibilidade**: Suporta diferentes países e regiões
4. **Facilidade**: API simples e intuitiva
5. **Manutenção**: Atualizações automáticas de feriados

## Dependências

- Python 3.6+
- workalendar
- datetime (biblioteca padrão)

## Licença

Esse projeto é de uso exclusivo mediante a prévia aprovação.
