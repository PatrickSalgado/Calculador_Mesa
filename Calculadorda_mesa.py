import tkinter as tk

def calcular_gorjeta():
    mesa = float(entry_mesa.get())
    pessoas = float(entry_pessoas.get())
    gorjeta = entry_gorjeta.get().lower()
    tot = 0
    if gorjeta == "s":
        percentual = float(entry_percentual.get())
        tot = (percentual * mesa) / 100
    elif gorjeta == "n":
        resultado_gorjeta.set("Sem gorjeta")
    despesas = float(entry_despesas.get())
    valor_total = mesa + despesas
    valor_mesa = (mesa + despesas) / pessoas
    valor_gorjeta = tot / pessoas
    resultado_mesa.set("Valor Total da mesa: R$ {:.2f}".format(valor_total))
    resultado_gorjeta.set("Valor Total da gorjeta: R$ {:.2f}".format(tot))
    resultado_total.set("Valor Total: R$ {:.2f}".format(valor_total + tot))
    resultado_por_pessoa.set("Valor total por pessoa: R$ {:.2f}".format(valor_mesa + valor_gorjeta))

root = tk.Tk()
root.title("Calculadora de Gorjeta")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_mesa = tk.Label(frame, text="Valor da mesa: R$")
label_mesa.grid(row=0, column=0, sticky="e")
entry_mesa = tk.Entry(frame)
entry_mesa.grid(row=0, column=1)

label_pessoas = tk.Label(frame, text="Quantidade de Pessoas na mesa: ")
label_pessoas.grid(row=1, column=0, sticky="e")
entry_pessoas = tk.Entry(frame)
entry_pessoas.grid(row=1, column=1)

label_gorjeta = tk.Label(frame, text="Deseja adição de gorjeta (S/N): ")
label_gorjeta.grid(row=2, column=0, sticky="e")
entry_gorjeta = tk.Entry(frame)
entry_gorjeta.grid(row=2, column=1)

label_percentual = tk.Label(frame, text="Valor da gorjeta em percentual: ")
label_percentual.grid(row=3, column=0, sticky="e")
entry_percentual = tk.Entry(frame)
entry_percentual.grid(row=3, column=1)

label_despesas = tk.Label(frame, text="Valor da despesas: R$")
label_despesas.grid(row=4, column=0, sticky="e")
entry_despesas = tk.Entry(frame)
entry_despesas.grid(row=4, column=1)

botao_calcular = tk.Button(frame, text="Calcular", command=calcular_gorjeta)
botao_calcular.grid(row=5, columnspan=2)

resultado_mesa = tk.StringVar()
resultado_gorjeta = tk.StringVar()
resultado_total = tk.StringVar()
resultado_por_pessoa = tk.StringVar()

label_resultado_mesa = tk.Label(frame, textvariable=resultado_mesa)
label_resultado_mesa.grid(row=6, columnspan=2, sticky="w")

label_resultado_gorjeta = tk.Label(frame, textvariable=resultado_gorjeta)
label_resultado_gorjeta.grid(row=7, columnspan=2, sticky="w")

label_resultado_total = tk.Label(frame, textvariable=resultado_total)
label_resultado_total.grid(row=8, columnspan=2, sticky="w")

label_resultado_por_pessoa = tk.Label(frame, textvariable=resultado_por_pessoa)
label_resultado_por_pessoa.grid(row=9, columnspan=2, sticky="w")

root.mainloop()
