import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np


class Gui:

    def __init__(self):
        
        # Instance variables for the GUI
        print("Initializing GUI...")
        self.root = tk.Tk()
        self.root.geometry("1000x600")
        self.frame_menu = tk.Frame(self.root)
        self.frame_data = tk.Frame(self.root)
    
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
        button_generate_games.pack(side=tk.LEFT, padx=20)
        button_generate_hotels.pack(side=tk.LEFT, padx=20)
        button_list_moviments.pack(side=tk.LEFT, padx=20)
        button_list_countries.pack(side=tk.LEFT, padx=20)
    
    
    
    # Frame para os gráficos e dados
    def create_data_frame(self):
        
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_data)
        self.canvas.get_tk_widget().pack()
    
    
    def generate_games(self):
        print("Generating games...")
    
    
    def generate_hotels(self):
        print("Generating hotels...")
    
    
    
    def list_moviments(self):
        
        print("Listing moviments...")
        self.ax.clear()
        x = np.random.randint(10, 50, 20) # Change this to the real data from the database
        y = np.random.randint(10, 50, 20) # Change this to the real data from the database
        self.ax.scatter(x, y)
        self.canvas.draw()
    
    
    def list_countries(self):
        print("Listing countries...")
        
    
    
    def start(self):
        print("Starting GUI...")
        self.create_menu_superior()
        self.create_data_frame()
        self.frame_menu.pack(side=tk.TOP)
        self.frame_data.pack(side=tk.BOTTOM)
        self.root.mainloop()