import os
import pandas as pd
import bibtexparser

def converter_bib_para_csv(caminho_bib_origem, pasta_destino, nome_arquivo_csv):
    """
    Lê um arquivo .bib específico, converte para DataFrame e salva como .csv.
    """
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_csv = os.path.join(pasta_destino, nome_arquivo_csv)
    
    with open(caminho_bib_origem, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        
    df = pd.DataFrame(bib_database.entries)
    df.to_csv(caminho_csv, index=False, encoding='utf-8')
    
    print(f"Convertido: {nome_arquivo_csv}")
    return df

# ==========================================
# Configurações de Pastas e Arquivos
# ==========================================
pasta_origem = 'Bib_Files'
pasta_destino = 'dados_mapeamento'

# Essa linha mágica lê a pasta e pega automaticamente todos os arquivos que terminam com .bib
arquivos_bib = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.endswith('.bib')]

lista_dataframes = []

print("Iniciando conversões individuais...\n")

# Loop para processar cada arquivo encontrado automaticamente
for arquivo in arquivos_bib:
    caminho_completo_bib = os.path.join(pasta_origem, arquivo)
    nome_csv = arquivo.replace('.bib', '.csv')
    
    df_atual = converter_bib_para_csv(caminho_completo_bib, pasta_destino, nome_csv)
    lista_dataframes.append(df_atual)

# ==========================================
# Unificação dos Arquivos
# ==========================================
if lista_dataframes: # Só unifica se tiver encontrado algum arquivo
    print("\nIniciando unificação dos arquivos...")
    
    # Concatena todos os DataFrames da lista em um só
    df_unificado = pd.concat(lista_dataframes, ignore_index=True)
    
    # Salva o DataFrame unificado em um CSV final
    caminho_unificado = os.path.join(pasta_destino, 'base_artigos_unificada.csv')
    df_unificado.to_csv(caminho_unificado, index=False, encoding='utf-8')
    
    print(f"\nSucesso! Arquivo unificado com {len(df_unificado)} artigos salvo em: {caminho_unificado}")
else:
    print("\nNenhum arquivo .bib foi encontrado na pasta origem.")