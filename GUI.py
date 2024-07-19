import tkinter as tk
from tkinter import messagebox
from declarations import declarations

def submit_form():
    nome_disc = entry_nome.get()
    cpf = entry_cpf.get()
    title = entry_title.get()
    area = entry_area.get()
    formato = entry_formato.get()

    print(f"Dados do formulário: nome_disc={nome_disc}, cpf={cpf}, title={title}, area={area}, formato={formato}")

    if nome_disc and cpf and title and area and formato:
        dados = {
            'nome_disc': nome_disc,
            'cpf': cpf,
            'title': title,
            'area': area,
            'formato': formato
        }
        print(f"Dados enviados para declarations: {dados}")
        declarations(dados)
        messagebox.showinfo("Sucesso", f"Arquivo editado salvo como: DEFESA {nome_disc}/Declarações {nome_disc}.docx")
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Declarações")

# Label e campo de entrada para o nome
label_nome = tk.Label(root, text="Digite o nome:")
label_nome.pack(pady=5)
entry_nome = tk.Entry(root, width=100)
entry_nome.pack(pady=5)

# Label e campo de entrada para o CPF
label_cpf = tk.Label(root, text="Digite o CPF:")
label_cpf.pack(pady=5)
entry_cpf = tk.Entry(root, width=100)
entry_cpf.pack(pady=5)

# Label e campo de entrada para o título
label_title = tk.Label(root, text="Digite o título:")
label_title.pack(pady=5)
entry_title = tk.Entry(root, width=100)
entry_title.pack(pady=5)

# Label e campo de entrada para a área
label_area = tk.Label(root, text="Digite a área:")
label_area.pack(pady=5)
entry_area = tk.Entry(root, width=100)
entry_area.pack(pady=5)

# Label e campo de entrada para o formato
label_formato = tk.Label(root, text="Digite o formato:")
label_formato.pack(pady=5)
entry_formato = tk.Entry(root, width=100)
entry_formato.pack(pady=5)

# Botão de submissão
btn_submit = tk.Button(root, text="Gerar Declaração", command=submit_form)
btn_submit.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
