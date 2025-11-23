import string
import secrets
import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Função para calcular a força da senha
# ------------------------------
def calcular_forca(senha):
    pontuacao = 0

    if len(senha) >= 12:
        pontuacao += 2
    elif len(senha) >= 8:
        pontuacao += 1

    if any(c.islower() for c in senha):
        pontuacao += 1
    if any(c.isupper() for c in senha):
        pontuacao += 1
    if any(c.isdigit() for c in senha):
        pontuacao += 1
    if any(c in string.punctuation for c in senha):
        pontuacao += 1

    if pontuacao <= 2:
        return "Fraca", "red"
    elif pontuacao == 3:
        return "Média", "orange"
    elif pontuacao == 4:
        return "Forte", "green"
    else:
        return "Muito Forte", "darkgreen"


# ------------------------------
# Função principal de geração de senha
# ------------------------------
def gerar_senha():
    usar_politica = var_politica.get() == 1

    if usar_politica:
        try:
            minimo = int(campo_minimo.get())
            maximo = int(campo_maximo.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos para mínimo e máximo.")
            return

        if minimo <= 0 or maximo <= 0 or minimo > maximo:
            messagebox.showerror("Erro", "Valores de mínimo/máximo inválidos.")
            return

        usar_maiusculas = var_maiusculas.get()
        usar_minusculas = var_minusculas.get()
        usar_numeros = var_numeros.get()
        usar_especiais = var_especiais.get()

        conjunto_caracteres = ""

        if usar_maiusculas:
            conjunto_caracteres += string.ascii_uppercase
        if usar_minusculas:
            conjunto_caracteres += string.ascii_lowercase
        if usar_numeros:
            conjunto_caracteres += string.digits
        if usar_especiais:
            conjunto_caracteres += string.punctuation

        if not conjunto_caracteres:
            messagebox.showerror("Erro", "Selecione ao menos um tipo de caractere.")
            return

        tamanho_senha = secrets.choice(range(minimo, maximo + 1))

    else:
        conjunto_caracteres = string.ascii_letters + string.digits + string.punctuation
        tamanho_senha = 12

    senha = "".join(secrets.choice(conjunto_caracteres) for _ in range(tamanho_senha))

    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, senha)

    classificacao, cor = calcular_forca(senha)
    texto_forca.config(text=f"Força da senha: {classificacao}", fg=cor)


# ------------------------------
# Habilitar / desabilitar política personalizada
# ------------------------------
def alternar_politica():
    estado = tk.NORMAL if var_politica.get() else tk.DISABLED

    for item in lista_widgets_politica:
        item.config(state=estado)


# ------------------------------
# Configuração da janela
# ------------------------------
janela = tk.Tk()
janela.title("Gerador de Senhas com Política e Força")
janela.geometry("420x520")
janela.resizable(False, False)

# ------------------------------
# Checkbutton principal
# ------------------------------
var_politica = tk.IntVar()
check_politica = tk.Checkbutton(
    janela,
    text="Ativar política personalizada",
    variable=var_politica,
    command=alternar_politica
)
check_politica.pack(pady=10)

# ------------------------------
# Frame para agrupar as opções da política
# ------------------------------
frame_politica = tk.Frame(janela)
frame_politica.pack(pady=10)

rotulo_minimo = tk.Label(frame_politica, text="Mínimo de caracteres:")
campo_minimo = tk.Entry(frame_politica, width=5)

rotulo_maximo = tk.Label(frame_politica, text="Máximo de caracteres:")
campo_maximo = tk.Entry(frame_politica, width=5)

var_maiusculas = tk.IntVar()
var_minusculas = tk.IntVar()
var_numeros = tk.IntVar()
var_especiais = tk.IntVar()

check_maiusculas = tk.Checkbutton(frame_politica, text="Incluir letras maiúsculas", variable=var_maiusculas)
check_minusculas = tk.Checkbutton(frame_politica, text="Incluir letras minúsculas", variable=var_minusculas)
check_numeros = tk.Checkbutton(frame_politica, text="Incluir números", variable=var_numeros)
check_especiais = tk.Checkbutton(frame_politica, text="Incluir caracteres especiais", variable=var_especiais)

rotulo_minimo.grid(row=0, column=0, sticky="w")
campo_minimo.grid(row=0, column=1, padx=5)

rotulo_maximo.grid(row=1, column=0, sticky="w")
campo_maximo.grid(row=1, column=1, padx=5)

check_maiusculas.grid(row=2, column=0, columnspan=2, sticky="w")
check_minusculas.grid(row=3, column=0, columnspan=2, sticky="w")
check_numeros.grid(row=4, column=0, columnspan=2, sticky="w")
check_especiais.grid(row=5, column=0, columnspan=2, sticky="w")

# Lista para habilitar/desabilitar widgets em massa
lista_widgets_politica = [
    rotulo_minimo, campo_minimo, rotulo_maximo, campo_maximo,
    check_maiusculas, check_minusculas, check_numeros, check_especiais
]

alternar_politica()


# ------------------------------
# Botão de gerar senha
# ------------------------------
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=15)

# ------------------------------
# Campo que exibe a senha gerada
# ------------------------------
campo_resultado = tk.Entry(janela, width=45, font=("Arial", 14))
campo_resultado.pack(pady=10)

# ------------------------------
# Indicador de força da senha
# ------------------------------
texto_forca = tk.Label(janela, text="Força da senha: ---", font=("Arial", 12))
texto_forca.pack(pady=5)

# ------------------------------
# Loop principal
# ------------------------------
janela.mainloop()