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
entry_nome = tk.Entry(root, width=100)
entry_nome.pack(pady=5)

# Label e campo de entrada para o cpf
label_cpf = tk.Label(root, text="Digite o cpf:")
label_cpf.pack(pady=5)
entry_cpf = tk.Entry(root, width=100)
entry_cpf.pack(pady=5)

# Label e campo de entrada para o tile
label_tile = tk.Label(root, text="Digite o tile:")
label_tile.pack(pady=5)
entry_tile = tk.Entry(root, width=100)
entry_tile.pack(pady=5)

# Label e campo de entrada para a area 
label_area = tk.Label(root, text="Digite a area:")
label_area.pack(pady=5)
entry_area = tk.Entry(root, width=100)
entry_area.pack(pady=5)

# Label e campo de entrada para o format
label_format = tk.Label(root, text="Digite o formato:")
label_format.pack(pady=5)
entry_format = tk.Entry(root, width=100)
entry_format.pack(pady=5)

# Botão de submissão
btn_submit = tk.Button(root, text="Gerar Declaração", command=submit_form)
btn_submit.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
