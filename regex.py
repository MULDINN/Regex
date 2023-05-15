import tkinter as tk
import re

def verificar_regex():
    regex = entrada_regex.get()
    texto = entrada_texto.get()
    correspondencia = re.match(regex, texto)
    if correspondencia:
        resultado.config(text="Válido")
    else:
        resultado.config(text="Inválido")

janela = tk.Tk()

# Cria os widgets
rotulo_regex = tk.Label(janela, text="Regex:")
entrada_regex = tk.Entry(janela)
rotulo_texto = tk.Label(janela, text="Texto:")
entrada_texto = tk.Entry(janela)
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_regex)
resultado = tk.Label(janela, text="")

# Adiciona os widgets na janela
rotulo_regex.pack()
entrada_regex.pack()
rotulo_texto.pack()
entrada_texto.pack()    
botao_verificar.pack()
resultado.pack()

janela.mainloop()   