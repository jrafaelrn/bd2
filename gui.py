import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np


class Gui:

    def __init__(self):
        
        # Instance variables for the GUI
        print("Initializing GUI...")
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.frame_menu = tk.Frame(self.root)
        self.frame_data = tk.Frame(self.root)
        
        
    def create_menu_lateral(self):
        
        button_generate_games = tk.Button(self.frame_menu, text="Gerar programação dos jogos", command=self.generate_games)
        button_generate_hotels = tk.Button(self.frame_menu, text="Gerar programação dos hotéis", command=self.generate_hotels)
        button_list_moviments = tk.Button(self.frame_menu, text="Listar jogos / nº de movimentos", command=self.list_moviments)
        button_list_countries = tk.Button(self.frame_menu, text="Listar jogadores / país", command=self.list_countries)
        
        # Add to interface
        button_generate_games.pack(side=tk.LEFT, padx=20)
        button_generate_hotels.pack(side=tk.LEFT, padx=20)
        button_list_moviments.pack(side=tk.LEFT, padx=20)
        button_list_countries.pack(side=tk.LEFT, padx=20)
        
    
    def generate_games(self):
        print("Generating games...")
    
    
    def generate_hotels(self):
        print("Generating hotels...")
    
    
    def list_moviments(self):
        print("Listing moviments...")
    
    
    def list_countries(self):
        print("Listing countries...")
        
    
    
    def start(self):
        print("Starting GUI...")
        self.create_menu_lateral()
        self.frame_menu.pack(side=tk.TOP)
        self.frame_data.pack(side=tk.BOTTOM)
        self.root.mainloop()