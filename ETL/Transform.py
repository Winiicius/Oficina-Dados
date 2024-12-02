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

# Mostrando as primeiras linhas dos DataFrames

# print(df_clientes.head())
# print(df_vendedores.head())
# print(df_pedidos.head())
# print(df_itens_pedido.head())
# print(df_produtos.head())
# print(df_enderecos)


# Após análise dos dados percebi que:

# tenho clientes e vendedores com id nulos
# tenho cliente duplicados
# tenho alguns clientes com o email nulos
# retirar a coluna "celular" dos clientes
# alguns pedidos refereciam ids de clientes e vendedores que não existem
# seria legal ter um jeito de  saber a comissão que o vendedor ganhou ( sabendo que a comissão é 4% do valor total do pedido )
# criar coluna  comissao nos pedidos


####################################################################################
# Tenho clientes e vendedores com id nulos

# Tenho duas opções ao encontrar um valor nulo ou indesejado

# 1 - excluir registro
# 2 - substituir valor

# excluir vendedores com nulo no id

# print("tamanho df_vendedores:", len(df_vendedores))
# print(print(df_vendedores["id"].isnull().sum()))

df_vendedores = df_vendedores[df_vendedores['id'].notnull()]

# print("tamanho df_vendedores:", len(df_vendedores))
# print(print(df_vendedores["id"].isnull().sum()))


# pegar os ids dos endereços que o id do cliente está nulo

df_clientes_nulos = df_clientes[df_clientes['id'].isnull()]

ids_nulos_enderecos = df_clientes_nulos['id_endereco']

# print(len(df_enderecos))
df_enderecos = df_enderecos[~df_enderecos['id'].isin(ids_nulos_enderecos)]
# print(len(df_enderecos))

# print(len(df_clientes))
df_clientes = df_clientes[df_clientes['id'].notnull()]
# print(len(df_clientes))


# Se eu exclui os clientes nulos e os respectivos endereços, 
# porque o tamanho está diferente levando em consideração que 
# eu tenho um endereço pra cada cliente?

####################################################################################
# Tenho clientes duplicados

# print(df_clientes.duplicated().sum())

df_clientes = df_clientes.drop_duplicates()

# print(len(df_clientes))

# print(len(df_enderecos))

####################################################################################
# Tenho alguns clientes com o email nulo

# print(df_clientes['email'].isnull().sum())

# null -> nomesobrenome@emailinvalido.com

# lambda argumentos: expressao
lambda a, b: a + b

df_clientes['email'] = df_clientes.apply(
    lambda linha: linha['nome'] + linha['sobrenome'] + "@emailinvalido.com" if pd.isnull(linha["email"]) else linha["email"],
    axis=1
)

# print(df_clientes['email'].isnull().sum())

####################################################################################
# retirar a coluna "celular" dos clientes

# print(df_clientes.columns)
df_clientes = df_clientes.drop(columns=["celular"])
# print(df_clientes.columns)

####################################################################################
# Alguns pedidos refereciam ids de clientes que não existem

ids_clientes_validos = df_clientes["id"]

# print(len(df_pedidos))
df_pedidos = df_pedidos[df_pedidos['id_cliente'].isin(ids_clientes_validos)]
# print(len(df_pedidos))

# Qual o problema ???

# itempedido que referencia id de pedido que não existe 

ids_pedidos_validos = df_pedidos["id"]

# print(len(df_itens_pedido))
df_itens_pedido = df_itens_pedido[df_itens_pedido["id_pedido"].isin(ids_pedidos_validos)]
# print(len(df_itens_pedido))

####################################################################################
# seria legal ter um jeito de  saber a comissão que o vendedor ganhou 
# ( sabendo que a comissão é 4% do valor total do pedido )
# criar coluna  comissao nos pedidos

df_pedidos["comissao"] = round(df_pedidos["preco_total"]*0.04, 2)
# print(df_pedidos.columns)


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

salvarDFs(dataframes)

