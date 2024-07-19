import os
from docx import Document

def declarations(dados):
    nome_disc = dados.get('nome_disc')
    cpf = dados.get('cpf')
    title = dados.get('title')
    area = dados.get('area')
    formato = dados.get('formato')

    print(f"Recebidos: nome_disc={nome_disc}, cpf={cpf}, title={title}, area={area}, formato={formato}")

    # Caminho do arquivo de template
    caminho_template = os.path.join('template', 'Declara.docx')
    print(f"Caminho do template: {caminho_template}")
    
    # Verifica se o arquivo de template existe
    if not os.path.exists(caminho_template):
        print(f"O arquivo {caminho_template} não foi encontrado.")
        return
    
    # Abre o arquivo de template
    doc = Document(caminho_template)
    print(f"Documento carregado: {caminho_template}")

    # Substitui os placeholders pelos valores fornecidos sem alterar a formatação
    for paragrafo in doc.paragraphs:
        print(f"Processando parágrafo: '{paragrafo.text}'")
        
        # Consolidar todo o texto do parágrafo em uma única string
        texto_completo = ''.join(run.text for run in paragrafo.runs)
        print(f"Texto completo do parágrafo: '{texto_completo}'")

        # Substituir placeholders
        texto_modificado = (texto_completo
                            .replace('$nomeDisc', nome_disc)
                            .replace('$cpf', cpf)
                            .replace('$title', title)
                            .replace('$area', area)
                            .replace('$formato', formato))
        
        print(f"Texto modificado: '{texto_modificado}'")

        # Atualizar cada run com o texto modificado
        for i, run in enumerate(paragrafo.runs):
            start = sum(len(run.text) for run in paragrafo.runs[:i])
            end = start + len(run.text)
            run.text = texto_modificado[start:end]

    # Cria a nova pasta se ela não existir
    nova_pasta = f'DEFESA {nome_disc}'
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)
    print(f"Pasta criada: {nova_pasta}")
    
    # Define o caminho do novo arquivo
    novo_caminho_arquivo = os.path.join(nova_pasta, f'Declarações {nome_disc}.docx')
    print(f"Novo caminho do arquivo: {novo_caminho_arquivo}")
    
    # Salva o documento editado
    doc.save(novo_caminho_arquivo)
    print(f"Arquivo editado salvo como: {novo_caminho_arquivo}")

