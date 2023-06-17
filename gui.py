import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk
import tkinter as tk
import numpy as np
from db import Db


class Gui:

    def __init__(self):
        
        # Instance variables for the GUI
        print("Initializing GUI...")
        self.root = tk.Tk()
        self.root.geometry("1100x600")
        self.root.title("Campeonato de Xadrex")
        self.frame_menu = tk.Frame(self.root)
        self.frame_data = tk.Frame(self.root)
        self.toolbar = None
    
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
                           
    def on_closing(self):
        print("Closing GUI...")
        self.root.destroy()
        self.root.quit()
    
    
    
    # Frame para o menu superior com os botões     
    def create_menu_superior(self):
        
        button_generate_games = tk.Button(self.frame_menu, text="Gerar programação dos jogos", command=self.generate_games)
        button_generate_hotels = tk.Button(self.frame_menu, text="Gerar programação dos hotéis", command=self.generate_hotels)
        button_list_moviments = tk.Button(self.frame_menu, text="Listar jogos / nº de movimentos", command=self.list_moviments)
        button_list_countries = tk.Button(self.frame_menu, text="Listar jogadores / país", command=self.list_countries)
        
        # Add to interface
        PADX = 20
        PADY = 20
        button_generate_games.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        button_generate_hotels.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        button_list_moviments.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        button_list_countries.pack(side=tk.LEFT, padx=PADX, pady=PADY)
    
    
    
    # Frame para os gráficos
    def create_chart_frame(self):
        
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_data)
        self.canvas.get_tk_widget().pack()
    
    
    # Frame para as tabelas
    def create_table_frame(self):
        
        print("Creating table frame...")
        self.remove_table_frame()
        self.my_tree = ttk.Treeview(self.root)
        
    
    def remove_table_frame(self):
        try:
            self.my_tree.destroy()
        except:
            pass
        
        
    def set_table_data(self, headers, data):
        
        print(f'Columns: {headers}')
        print(f'Data: {data}')
        
        self.my_tree["columns"] = headers
        
        # Format columns
        self.my_tree.column("#0", width=0)
        for i in range(0, len(headers)):
            width_ = self.get_width_by_type(data[0][i])
            self.my_tree.column(headers[i], anchor=tk.W, width=width_)
            
        # Create headings
        self.my_tree.heading("#0", text="", anchor=tk.W)
        for i in range(0, len(headers)):
            self.my_tree.heading(headers[i], text=headers[i], anchor=tk.W)
            
        # Add data
        for i in range(len(data)):
            self.my_tree.insert(parent="", index="end", iid=i, text="", values=data[i])
        
        # Pack to screen
        self.my_tree.pack()

    
    def get_width_by_type(self, data):
        
        print(f'Getting width by type: {data} -> {type(data)}')
        
        if type(data) == str:
            return 170
        
        if type(data) == int or type(data) == float or str(type(data)) == "<class 'decimal.Decimal'>":
            return 80
        
        return 100
        
    ####################################
    #              BOTÕES              #
    ####################################    
    
    def generate_games(self):
        
        print("Generating games...")
        
        self.create_table_frame()
    
        command = """
        select DISTINCT get_name_by_id(num_jogador) as Nome_Jogador,
        A.num_jogo, get_name_by_id(B.num_arbitro) as Nome_Arbitro, dia, mes, ano, D.id_salao, E.nome
        from JOGA A, JOGO B, JORNADA C, E_CELEBRADO_EM D, HOTEL E, SALAO F
        where A.num_jogo = B.num_jogo AND B.id_jornada = C.id
        AND B.num_jogo = D.num_jogo AND D.id_salao = F.id AND F.id_hotel = E.id
        ORDER BY A.num_jogo
        """
        
        data = self.db.execute_bd(command.replace("\n", ""))
        headers = ["Nome Jogador", "Núm. Jogo", "Nome Árbitro", "Dia", "Mês", "Ano", "ID Salão", "Nome Hotel"]
        
        self.set_table_data(headers, data)
    
    
    def generate_hotels(self):
    
        print("Generating hotels...")
    
    
    
    def list_moviments(self):
        
        print("Listing moviments...")
        self.ax.clear()
            
        x = []
        y = []
    
        self.ax.scatter(x, y)
        self.create_toolbar()
        self.canvas.draw()
    
    
    def list_countries(self):
        print("Listing countries...")
        
        
    def create_toolbar(self):
        if self.toolbar == None:     
            self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame_data, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack()
        
    
    def start_database(self):
        self.db = Db()
        
    
    def start(self):
        print("Starting GUI...")
        self.create_menu_superior()
        self.frame_menu.pack(side=tk.TOP)
        self.frame_data.pack(side=tk.BOTTOM)
        self.start_database()
        self.root.mainloop()