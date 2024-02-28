import tkinter as tk

root = tk.Tk() #cria uma janela principal 

#nome para janela principal 

root.title("Sistema Supervisório")

#cria um rótulo

label = tk.Label(root, text='Sistema Supervisório em Python')
label.pack() #coloca o rótulo na janela

#cria um botão

button = tk.Button(root, text="Click me!")

button.pack() #coloca o botão na janela

#inicia o loop de eventos

root.mainloop()
