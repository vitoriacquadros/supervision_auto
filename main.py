import tkinter as tk
import tkinter as ttk 
# from PIL import Image, ImageTk
# import paho.mqtt.client as mqtt

class SystemSupervisory:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Supervisório")
        
        self.label = tk.Label(self.root, text='Sistema Supervisório em Python para Instalações Industriais')
        self.label.pack()

        self.button = tk.Button(self.root, text="Acionar LED")
        self.button.pack()
        
        self.button_exit = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.button_exit.pack()
    
    def button_click(self):
        print("Botão clicado")

def create_tab(notebook, tab_name):
    # Cria um novo frame para a aba
    tab = ttk.Frame(notebook)

    # Adiciona widgets ao frame
    label = ttk.Label(tab, text=f"This is {tab_name} tab")
    label.pack(padx=10, pady=10)

    # Adiciona a aba ao notebook
    notebook.add(tab, text=tab_name)

def main():
    root = tk.Tk()
    root.title("Exemplo de Abas")

    # Cria o notebook
    notebook = ttk.notebook(root)

    # Cria as abas
    create_tab(notebook, "Tab 1")
    create_tab(notebook, "Tab 2")
    create_tab(notebook, "Tab 3")

    # Empacota o notebook na janela principal
    notebook.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemSupervisory(root)
    root.mainloop()
    main()
