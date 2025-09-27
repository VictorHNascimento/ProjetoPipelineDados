import json
import csv
from pathlib import Path
from processamento_dados import Dados

# Caminho Dos Arquivos
path_A = Path('data_raw/dados_empresaA.json')
path_B = Path('data_raw/dados_empresaB.csv')

# Extração
dados_empresaA = Dados.Leitura_Dados(path_A, str(path_A.suffix))
print(f'Carregamento Da Empresa A Com Sucesso. \n Colunas: {dados_empresaA.nome_colunas} \n Quantidade de Linhas: {dados_empresaA.qtde_linhas}')
print()
dados_empresaB = Dados.Leitura_Dados(path_B, str(path_B.suffix))
print(f'Carregamento da Empresa B Com Sucesso. \n Colunas: {dados_empresaB.nome_colunas} \n Quantidade de Linhas: {dados_empresaA.qtde_linhas}')
print()

# Transformação
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.Renomeia_Colunas(key_mapping)
print(f'Colunas Empresa B Renomeadas!\n Colunas: {dados_empresaB.nome_colunas}')
print()

## Combinando os Dados
dados_fusao = Dados.Unificacao_Dados(dados_empresaA, dados_empresaB)
print(f'Dados Unidos Com Sucesso!. \n Colunas: {dados_fusao.nome_colunas} \n Quantidade de Linhas: {dados_fusao.qtde_linhas}')
print()

#Load
path_download = 'data_processed/dados_fusao.csv'
dados_fusao.Salvando_Dados(path_download)