import pandas as pd

# importar dados

csv_clientes = 'tabelasResultadoFaker/clientes.csv'
csv_vendedores = 'tabelasResultadoFaker/vendedores.csv'
csv_vendas = 'tabelasResultadoFaker/vendas.csv'
csv_itens_venda = 'tabelasResultadoFaker/itens_venda.csv'
csv_produtos = 'tabelasResultadoFaker/produtos.csv'
csv_enderecos = 'tabelasResultadoFaker/enderecos.csv'

# Porque usar DataFrames???

# TARARA TARARA

# Lendo os arquivos CSV
df_clientes = pd.read_csv(csv_clientes)
df_vendedores = pd.read_csv(csv_vendedores)
df_vendas = pd.read_csv(csv_vendas)
df_itens_venda = pd.read_csv(csv_itens_venda)
df_produtos = pd.read_csv(csv_produtos)
df_enderecos = pd.read_csv(csv_enderecos)

# Mostrando as primeiras linhas dos DataFrames
# print(df_clientes.head())
# print(df_vendedores.head())
# print(df_vendas.head())
# print(df_itens_venda.head())
# print(df_produtos.head())
# print(df_enderecos)


# Clientes e vendedores com id null, futuramente adicionar outros campos nulos onde os ids são nulos

# mostra true onde é nulo
# print(df_clientes.isnull())

# mostra a quantidade de nulo por coluna
print(df_clientes.isnull().sum())

# Explicar quais as soluções(2) ao encontrar um valor indesejado

# nosso caso, excluir clientes com id null:

df_clientes_nulos = df_clientes[df_clientes['id'].isnull()] # inicial -> df_clientes = df_clientes[df_clientes['id'].notnull()]

# MAAAAAS, para excluir cliente com id null, primeiro excuir endereço( reforça o cuidado na hora de tratar os dados )
# mudar linha 43 para guardar apenas os valores nulos

ids_enderecos_para_excluir = df_clientes_nulos['id_endereco']

print(len(ids_enderecos_para_excluir.to_list()))

print("tamanho antes: ", len(df_enderecos))
df_enderecos = df_enderecos[~df_enderecos['id'].isin(ids_enderecos_para_excluir)]
print("tamanho depois: ", len(df_enderecos)) # o tamanho pode não ser o mesmo dos ids, pois pode haver duplicatas

# Agora com os endereços excluídos, podemos excluir os clientes cujos ids estão nulos

print("tamanho antes: ", len(df_clientes))
df_clientes = df_clientes[df_clientes['id'].notnull()]
print("tamanho depois: ", len(df_clientes))

df_vendedores = df_vendedores[df_vendedores['id'].notnull()]

# CLIENTE E ENDEREÇO DEVERIAM SER DO MESMO TAMANHO, OU NÃO? 
print(len(df_clientes))
print(len(df_enderecos))

# DUPLICATAS
# clientes duplicados

print(df_clientes.duplicated().sum())

df_clientes = df_clientes.drop_duplicates() # Primeira ocorrência é mantida
print(len(df_clientes)) # TUDO CERTO E NADA ERRADO



# print(df_clientes[df_clientes['id'].isnull()])
# df_clientes[df_clientes['id'].notnull()]
# print(df_clientes.isnull().sum())

# SEGUNDA OPÇÃO ( SOBRESCREVER )
# emails inválidos

# df_clientes['email'] = df_clientes['email'].str.replace(r'^(.*)@$',r'\1@emailinvalido',regex=True) # testar depois

# df_clientes['email'] = df_clientes['email'].apply(
#     lambda x: x + 'emailinvalido' if x.endswith('@') else x outra abordagem
# )

# mascara = df['email'].str.endswith('@')
# # Atualizar os emails que atendem ao critério # Outra alternativa, esses exemplo são para "nomepessoa@"
# df.loc[mascara, 'email'] = df.loc[mascara, 'email'] + 'emailinvalido'  


# vendas referenciando clientes que não existem

# pensamento lógico
# ids válidos estão em df_clientes, pegos os válido e removo os que não estão na lista
ids_clientes_validos = df_clientes['id']
print("antes: ", len(df_vendas))



df_vendas = df_vendas[df_vendas['id_cliente'].isin(ids_clientes_validos)]
print("depois: ", len(df_vendas))

ids_vendas_validos = df_vendas['id']

df_itens_venda = df_itens_venda[df_itens_venda['id_venda'].isin(ids_vendas_validos)]

# retirar coluna celular
print(df_clientes.columns)
df_clientes = df_clientes.drop(columns=['celular'])
print(df_clientes.columns)


# TRANSFOMAR OS DATAFRAMES EM CSV

dataframes:list = [
    {"dataframe":df_clientes,
     "nome_arquivo": "clientes.csv"},
     {"dataframe":df_enderecos,
     "nome_arquivo": "enderecos.csv"},
     {"dataframe":df_vendas,
     "nome_arquivo": "vendas.csv"},
     {"dataframe":df_produtos,
     "nome_arquivo": "produtos.csv"},
     {"dataframe":df_itens_venda,
     "nome_arquivo": "itens_venda.csv"},
     {"dataframe":df_vendedores,
     "nome_arquivo": "vendedores.csv"},
]

def salvarDFs(dataframes:list):
    for dataframe in dataframes:
        dataframe.get("dataframe").to_csv("tabelasResultadoETL/" + dataframe.get("nome_arquivo"), index=False, encoding='utf-8', sep=',')

salvarDFs(dataframes)

