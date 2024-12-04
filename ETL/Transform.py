import pandas as pd
import time

# Pandas
# O Pandas é uma biblioteca poderosa para análise e manipulação de dados. 
# Ele permite carregar, limpar, transformar e analisar dados de diversas fontes, 
# como arquivos CSV, Excel e bancos de dados.

# importar dados

csv_clientes = 'tabelasResultadoFaker/clientes.csv'
csv_vendedores = 'tabelasResultadoFaker/vendedores.csv'
csv_pedidos = 'tabelasResultadoFaker/pedidos.csv'
csv_itens_pedido = 'tabelasResultadoFaker/itens_pedido.csv'
csv_produtos = 'tabelasResultadoFaker/produtos.csv'
csv_enderecos = 'tabelasResultadoFaker/enderecos.csv'

# Tranformando os arquivos CSV em DataFrames

df_clientes = pd.read_csv(csv_clientes)
df_vendedores = pd.read_csv(csv_vendedores)
df_pedidos = pd.read_csv(csv_pedidos)
df_itens_pedido = pd.read_csv(csv_itens_pedido)
df_produtos = pd.read_csv(csv_produtos)
df_enderecos = pd.read_csv(csv_enderecos)

# O que é um DataFrames???

# DataFrame é uam tabela oferecida pelo pandas
# vários métodos disponibilizados para facilitar a manipulação dos dados

# Mostrando as linhas de um DataFrames

# print(df_clientes)

# Após análise dos dados percebi que:

# print(df_vendedores.isnull().sum())

# tenho clientes e vendedores com id nulos

# print(len(df_vendedores))
df_vendedores =  df_vendedores.dropna(subset=['id'])
# print(len(df_vendedores))

df_ids_nulos = df_clientes[df_clientes['id'].isnull()]
# print(df_ids_nulos)

ids_enderecos_nulos = df_ids_nulos['id_endereco']
# print(ids_enderecos_nulos)

# print(len(df_enderecos))
df_enderecos = df_enderecos[~df_enderecos['id'].isin(ids_enderecos_nulos)]
# print(len(df_enderecos))

print(len(df_clientes))
df_clientes = df_clientes.dropna(subset=['id'])
print(len(df_clientes))






# tenho cliente duplicados

# tenho alguns clientes com o email nulo

# retirar a coluna "celular" dos clientes

# alguns pedidos refereciam ids de clientes e vendedores que não existem

# Seria legal ter um jeito de  saber a comissão que o vendedor ganhou ( sabendo que a comissão é 4% do valor total do pedido )
# criar coluna comissao nos pedidos


# # TRANSFOMAR OS DATAFRAMES EM CSV

dataframes:list = [
    {"dataframe":df_clientes,
     "nome_arquivo": "clientes.csv"},
     {"dataframe":df_enderecos,
     "nome_arquivo": "enderecos.csv"},
     {"dataframe":df_pedidos,
     "nome_arquivo": "pedidos.csv"},
     {"dataframe":df_produtos,
     "nome_arquivo": "produtos.csv"},
     {"dataframe":df_itens_pedido,
     "nome_arquivo": "itens_pedido.csv"},
     {"dataframe":df_vendedores,
     "nome_arquivo": "vendedores.csv"},
]

def salvarDFs(dataframes:list):
    for dataframe in dataframes:
        dataframe.get("dataframe").to_csv("tabelasResultadoETL/" + dataframe.get("nome_arquivo"), index=False, encoding='utf-8', sep=',')
        print("Arquivo ", dataframe.get("nome_arquivo"), " salvo com sucesso!!!")
        time.sleep(1)

# salvarDFs(dataframes)
