# Controle de Versões - Validador de Dias Úteis

## V1.0.0 - Versão Inicial (2024)

### 🎯 Funcionalidades Principais

#### ✅ **Cálculo de Dias Úteis por Período Personalizado**
- Suporte a qualquer período (data início e fim)
- Validação automática de datas (formato DD/MM/AAAA)
- Períodos que cruzam meses/anos
- Cálculo preciso usando workalendar (feriados brasileiros)

#### ✅ **Módulos Organizados**
- `calendario_utils.py` - Cálculos de calendário
- `calculos_operacionais.py` - Métricas de negócio
- `interface_usuario.py` - Interface do usuário
- `index.py` - Programa principal
- `exemplo_uso_modulos.py` - Exemplos de uso

#### ✅ **Funcionalidades Avançadas**
- Listagem de feriados no período
- Cálculo de percentual de dias úteis
- Análise de capacidade operacional
- Cálculo de pessoas necessárias
- Formatação de tempo em formato legível

### 📋 **Arquivos do Projeto**
```
calculo_operacional/
├── index.py                    # Programa principal
├── calendario_utils.py         # Utilitários de calendário
├── calculos_operacionais.py    # Cálculos de negócio
├── interface_usuario.py        # Interface do usuário
├── exemplo_uso_modulos.py      # Exemplos de uso
├── README.md                   # Documentação
├── requirements.txt            # Dependências
├── VERSION.md                  # Este arquivo
└── .gitignore                  # Arquivos ignorados
```

### 🔧 **Dependências**
- Python 3.6+
- workalendar
- datetime (biblioteca padrão)

### 🚀 **Como Usar**
```bash
# Instalar dependências
pip install workalendar

# Executar programa principal
python index.py

# Ver exemplos de uso
python exemplo_uso_modulos.py
```

### 📝 **Changelog**
- **V1.0.0**: Versão inicial com todas as funcionalidades básicas
  - Cálculo de dias úteis por período personalizado
  - Sistema modular organizado
  - Interface de usuário completa
  - Documentação detalhada
  - Exemplos de uso

### 🎉 **Status**
✅ **Versão Estável** - Pronta para uso em produção 