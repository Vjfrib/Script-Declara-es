import os
from docx import Document

def declarations(dados):
    nome_disc = dados.get('nome_disc')
    cpf = dados.get('cpf')
    title = dados.get('title')
    area = dados.get('area')
    format = dados.get('format')

    # Caminho do arquivo de template
    caminho_template = os.path.join('template', 'Declarações $nomeDisc.docx')
    
    # Verifica se o arquivo de template existe
    if not os.path.exists(caminho_template):
        print(f"O arquivo {caminho_template} não foi encontrado.")
        return
    
    # Abre o arquivo de template
    doc = Document(caminho_template)
    
    # Substitui os placeholders pelos valores fornecidos sem alterar a formatação
    for paragrafo in doc.paragraphs:
        for run in paragrafo.runs:
            if '$nomeDisc' in run.text:
                run.text = run.text.replace('$nomeDisc', nome_disc)
            elif '$cpf' in run.text:
                run.text = run.text.replace('$cpf', cpf)
            elif '$title' in run.text:
                run.text = run.text.replace('$title', title)
            elif '$area' in run.text:
                run.text = run.text.replace('$area', area)
            elif '$format' in run.text:
                run.text = run.text.replace('$format', format)
    
    # Cria a nova pasta se ela não existir
    nova_pasta = f'DEFESA {nome_disc}'
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)
    
    # Define o caminho do novo arquivo
    novo_caminho_arquivo = os.path.join(nova_pasta, f'Declarações {nome_disc}.docx')
    
    # Salva o documento editado
    doc.save(novo_caminho_arquivo)
    
    print(f"Arquivo editado salvo como: {novo_caminho_arquivo}")
