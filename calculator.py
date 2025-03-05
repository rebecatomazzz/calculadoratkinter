import tkinter as tk

# Função para realizar cálculos
def calcular():
    try:
        resultado = eval(entry.get())
        label_resultado.config(text="Resultado: " + str(resultado))
    except Exception as e:
        label_resultado.config(text="Erro: " + str(e))

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Definindo o estilo com tons de rosa
root.config(bg='#ffccff')

# Caixa de entrada para expressões matemáticas
entry = tk.Entry(root, font=("Arial", 20), bg="#ff99cc", bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Rótulo para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 15), bg="#ffccff", fg="purple")
label_resultado.grid(row=1, column=0, columnspan=4)

# Funções dos botões
botões = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
]

# Criando os botões
for (texto, linha, coluna) in botões:
    if texto == "=":
        botao = tk.Button(root, text=texto, font=("Arial", 20), bg="#ff66cc", fg="white", bd=5, command=calcular)
    else:
        botao = tk.Button(root, text=texto, font=("Arial", 20), bg="#ff66cc", fg="white", bd=5, command=lambda t=texto: entry.insert(tk.END, t))
    botao.grid(row=linha, column=coluna, ipadx=20, ipady=20, sticky="nsew")

# Função para limpar a entrada
def limpar():
    entry.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

# Adicionando o botão de limpar
botao_limpar = tk.Button(root, text="Limpar", font=("Arial", 20), bg="#ff66cc", fg="white", bd=5, command=limpar)
botao_limpar.grid(row=6, column=0, columnspan=4, ipadx=20, ipady=20, sticky="nsew")

# Ajustando a expansão das células
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Rodando a interface
root.mainloop()
