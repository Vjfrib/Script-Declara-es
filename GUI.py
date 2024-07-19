import tkinter as tk
from tkinter import messagebox
from declarations import declarations

def submit_form():
    nome_disc = entry_nome.get()
    if nome_disc:
        declarations(nome_disc)
        messagebox.showinfo("Sucesso", f"Arquivo editado salvo como: DEFESA {nome_disc}/Declarações {nome_disc}.docx")
    else:
        messagebox.showwarning("Aviso", "Nenhum nome foi fornecido.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Declarações")

# Label e campo de entrada para o nome
label_nome = tk.Label(root, text="Digite o nome:")
label_nome.pack(pady=5)
entry_nome = tk.Entry(root, width=50)
entry_nome.pack(pady=5)

# Botão de submissão
btn_submit = tk.Button(root, text="Gerar Declaração", command=submit_form)
btn_submit.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
