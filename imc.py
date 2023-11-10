import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura_cm = float(altura_entry.get())
        peso = float(peso_entry.get())

        
        altura = altura_cm / 100.0


        imc = peso / (altura ** 2)


        classificacao = obter_classificacao(imc)


        resultado_label.config(text=f"IMC: {imc:.2f} - {classificacao}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos para altura e peso.")

def obter_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def reiniciar():
    nome_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    peso_entry.delete(0, tk.END)
    resultado_label.config(text="IMC: ")

root = tk.Tk()
root.title("Calculadora de IMC")

frame2 = tk.Frame(root)
frame2.pack(side=tk.LEFT, padx=10)

tk.Label(frame2, text="Nome:").grid(row=0, column=0, pady=5)
nome_entry = tk.Entry(frame2)
nome_entry.grid(row=0, column=1, pady=5)

tk.Label(frame2, text="Endereço:").grid(row=1, column=0, pady=5)
endereco_entry = tk.Entry(frame2)
endereco_entry.grid(row=1, column=1, pady=5)

tk.Label(frame2, text="Altura (cm):").grid(row=2, column=0, pady=5)
altura_entry = tk.Entry(frame2)
altura_entry.grid(row=2, column=1, pady=5)

tk.Label(frame2, text="Peso (kg):").grid(row=3, column=0, pady=5)
peso_entry = tk.Entry(frame2)
peso_entry.grid(row=3, column=1, pady=5)

resultado_label = tk.Label(frame2, text="IMC: ")
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

calcular_button = tk.Button(root, text="Calcular IMC", command=calcular_imc)
calcular_button.pack(pady=10)

reiniciar_button = tk.Button(root, text="Reiniciar", command=reiniciar)
reiniciar_button.pack(pady=10)

root.mainloop()

