"""
Módulo para interface gráfica (GUI) usando tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import datetime
from calendario_utils import (
    calcular_dias_uteis_periodo, 
    mostrar_feriados_periodo, 
    obter_total_dias_periodo
)
from calculos_operacionais import (
    calcular_metricas_operacionais, 
    calcular_percentual_dias_uteis, 
    formatar_tempo_minutos
)
from validacoes import validar_dados_completos, obter_mensagens_ajuda

class CalculoOperacionalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculador de Headcount - V1.1")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Configurar estilo
        self.setup_styles()
        
        # Criar interface
        self.criar_interface()
        
    def setup_styles(self):
        """Configura estilos para a interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Result.TLabel', font=('Arial', 10))
        
    def criar_interface(self):
        """Cria a interface principal"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Calculador de Headcount", style='Title.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Subtítulo
        subtitulo = ttk.Label(main_frame, text="Cálculo de métricas operacionais por período personalizado", 
                             font=('Arial', 10))
        subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Frame de entrada de dados
        self.criar_frame_entrada(main_frame)
        
        # Frame de resultados
        self.criar_frame_resultados(main_frame)
        
        # Frame de feriados
        self.criar_frame_feriados(main_frame)
        
        # Botões
        self.criar_botoes(main_frame)
        
    def criar_frame_entrada(self, parent):
        """Cria o frame de entrada de dados"""
        frame = ttk.LabelFrame(parent, text="Dados de Entrada", padding="10")
        frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        # Total de chamados
        ttk.Label(frame, text="Total de chamados:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_chamados = ttk.Entry(frame, width=20)
        self.entry_chamados.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        # TMA
        ttk.Label(frame, text="Tempo médio de atendimento (minutos):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_tma = ttk.Entry(frame, width=20)
        self.entry_tma.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        # Data de início
        ttk.Label(frame, text="Data de início (DD/MM/AAAA):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_data_inicio = ttk.Entry(frame, width=20)
        self.entry_data_inicio.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        self.entry_data_inicio.insert(0, "01/01/2025")
        
        # Data de fim
        ttk.Label(frame, text="Data de fim (DD/MM/AAAA):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.entry_data_fim = ttk.Entry(frame, width=20)
        self.entry_data_fim.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        self.entry_data_fim.insert(0, "31/01/2025")
        
    def criar_frame_resultados(self, parent):
        """Cria o frame de resultados"""
        frame = ttk.LabelFrame(parent, text="Resultados", padding="10")
        frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        frame.columnconfigure(1, weight=1)
        
        # Variáveis para os resultados
        self.resultado_dias_uteis = tk.StringVar()
        self.resultado_tempo_total = tk.StringVar()
        self.resultado_capacidade = tk.StringVar()
        self.resultado_pessoas = tk.StringVar()
        self.resultado_percentual = tk.StringVar()
        
        # Labels de resultados
        ttk.Label(frame, text="Dias úteis no período:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Label(frame, textvariable=self.resultado_dias_uteis, style='Result.TLabel').grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        ttk.Label(frame, text="Tempo total necessário:", style='Header.TLabel').grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(frame, textvariable=self.resultado_tempo_total, style='Result.TLabel').grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        ttk.Label(frame, text="Capacidade operacional:", style='Header.TLabel').grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Label(frame, textvariable=self.resultado_capacidade, style='Result.TLabel').grid(row=2, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        ttk.Label(frame, text="Pessoas necessárias:", style='Header.TLabel').grid(row=3, column=0, sticky=tk.W, pady=2)
        ttk.Label(frame, textvariable=self.resultado_pessoas, style='Result.TLabel').grid(row=3, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        ttk.Label(frame, text="Percentual de dias úteis:", style='Header.TLabel').grid(row=4, column=0, sticky=tk.W, pady=2)
        ttk.Label(frame, textvariable=self.resultado_percentual, style='Result.TLabel').grid(row=4, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
    def criar_frame_feriados(self, parent):
        """Cria o frame de feriados"""
        frame = ttk.LabelFrame(parent, text="Feriados no Período", padding="10")
        frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        # Área de texto para feriados
        self.text_feriados = scrolledtext.ScrolledText(frame, height=6, width=60)
        self.text_feriados.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def criar_botoes(self, parent):
        """Cria os botões de ação"""
        frame = ttk.Frame(parent)
        frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        
        # Botão calcular
        btn_calcular = ttk.Button(frame, text="Calcular", command=self.calcular)
        btn_calcular.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão limpar
        btn_limpar = ttk.Button(frame, text="Limpar", command=self.limpar)
        btn_limpar.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão ajuda
        btn_ajuda = ttk.Button(frame, text="Ajuda", command=self.mostrar_ajuda)
        btn_ajuda.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão sair
        btn_sair = ttk.Button(frame, text="Sair", command=self.root.quit)
        btn_sair.pack(side=tk.LEFT)
        
    def validar_entrada(self):
        """Valida os dados de entrada usando validações robustas"""
        try:
            # Obter valores dos campos
            total_chamados_str = self.entry_chamados.get()
            tma_str = self.entry_tma.get()
            data_inicio_str = self.entry_data_inicio.get()
            data_fim_str = self.entry_data_fim.get()
            
            # Validar todos os dados de uma vez
            valido, mensagem, dados_validados = validar_dados_completos(
                total_chamados_str, tma_str, data_inicio_str, data_fim_str
            )
            
            if not valido:
                messagebox.showerror("Erro de Validação", mensagem)
                return False, None
                
            return True, dados_validados
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")
            return False, None
            
    def calcular(self):
        """Executa os cálculos"""
        # Validar entrada
        valido, dados = self.validar_entrada()
        if not valido:
            return
            
        try:
            # Calcular dias úteis
            dias_uteis = calcular_dias_uteis_periodo(dados['data_inicio'], dados['data_fim'])
            
            # Calcular métricas operacionais
            metricas = calcular_metricas_operacionais(
                dados['total_chamados'],
                dados['tma'],
                dias_uteis
            )
            
            # Calcular métricas adicionais
            total_dias = obter_total_dias_periodo(dados['data_inicio'], dados['data_fim'])
            percentual = calcular_percentual_dias_uteis(dias_uteis, total_dias)
            
            # Atualizar resultados
            self.resultado_dias_uteis.set(f"{dias_uteis} dias")
            self.resultado_tempo_total.set(formatar_tempo_minutos(metricas['tempo_total']))
            self.resultado_capacidade.set(f"{metricas['capacidade_operacional']:.0f} chamados por período")
            self.resultado_pessoas.set(f"{int(metricas['pessoas_necessarias'])} pessoas")
            self.resultado_percentual.set(f"{percentual:.1f}%")
            
            # Mostrar feriados
            self.mostrar_feriados(dados['data_inicio'], dados['data_fim'])
            
            messagebox.showinfo("Sucesso", "Cálculos realizados com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro durante os cálculos: {str(e)}")
            
    def mostrar_feriados(self, data_inicio, data_fim):
        """Mostra os feriados no período"""
        try:
            feriados = mostrar_feriados_periodo(data_inicio, data_fim)
            
            # Limpar área de texto
            self.text_feriados.delete(1.0, tk.END)
            
            if feriados:
                self.text_feriados.insert(tk.END, f"Feriados encontrados ({len(feriados)}):\n\n")
                for feriado in feriados:
                    self.text_feriados.insert(tk.END, f"• {feriado.strftime('%d/%m/%Y')} ({feriado.strftime('%A')})\n")
            else:
                self.text_feriados.insert(tk.END, "Nenhum feriado encontrado no período.")
                
        except Exception as e:
            self.text_feriados.delete(1.0, tk.END)
            self.text_feriados.insert(tk.END, f"Erro ao carregar feriados: {str(e)}")
            
    def limpar(self):
        """Limpa todos os campos"""
        self.entry_chamados.delete(0, tk.END)
        self.entry_tma.delete(0, tk.END)
        self.entry_data_inicio.delete(0, tk.END)
        self.entry_data_inicio.insert(0, "01/01/2025")
        self.entry_data_fim.delete(0, tk.END)
        self.entry_data_fim.insert(0, "31/01/2025")
        
        # Limpar resultados
        self.resultado_dias_uteis.set("")
        self.resultado_tempo_total.set("")
        self.resultado_capacidade.set("")
        self.resultado_pessoas.set("")
        self.resultado_percentual.set("")
        
        # Limpar feriados
        self.text_feriados.delete(1.0, tk.END)
        
    def mostrar_ajuda(self):
        """Mostra informações de ajuda sobre os limites"""
        mensagens = obter_mensagens_ajuda()
        
        ajuda_texto = """📋 **LIMITES E VALIDAÇÕES**

🔢 **Total de Chamados:**
• {total_chamados}

⏱️ **Tempo Médio de Atendimento (TMA):**
• {tma}

📅 **Datas:**
• {data}

📊 **Período:**
• {periodo}

💡 **Dicas:**
• Use apenas números nos campos numéricos
• Datas devem estar no formato DD/MM/AAAA
• O sistema valida automaticamente todos os campos
• Períodos muito longos podem demorar para calcular""".format(**mensagens)
        
        messagebox.showinfo("Ajuda - Limites do Sistema", ajuda_texto)

def main():
    """Função principal para iniciar a GUI"""
    root = tk.Tk()
    app = CalculoOperacionalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 