import os
from docx import Document

def editar_arquivo_word(nome_disc):
    # Caminho do arquivo de template
    caminho_template = os.path.join('template', 'Declarações $nomeDisc.docx')
    
    # Verifica se o arquivo de template existe
    if not os.path.exists(caminho_template):
        print(f"O arquivo {caminho_template} não foi encontrado.")
        return
    
    # Abre o arquivo de template
    doc = Document(caminho_template)
    
    # Substitui $nomeDisc pelo nome fornecido sem alterar a formatação
    for paragrafo in doc.paragraphs:
        for run in paragrafo.runs:
            if '$nomeDisc' in run.text:
                run.text = run.text.replace('$nomeDisc', nome_disc)
    
    # Cria a nova pasta se ela não existir
    nova_pasta = f'DEFESA {nome_disc}'
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)
    
    # Define o caminho do novo arquivo
    novo_caminho_arquivo = os.path.join(nova_pasta, f'Declarações {nome_disc}.docx')
    
    # Salva o documento editado
    doc.save(novo_caminho_arquivo)
    
    print(f"Arquivo editado salvo como: {novo_caminho_arquivo}")

# Solicita o nome ao usuário
nome_disc = input("Digite o nome: ")

# Edita o arquivo Word com o nome fornecido
editar_arquivo_word(nome_disc)
