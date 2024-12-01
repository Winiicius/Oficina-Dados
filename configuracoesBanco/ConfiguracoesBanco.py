import pandas as pd
from sqlalchemy import create_engine, text

# Definir a conexão com o PostgreSQL
def conectar_banco(nome_banco):
    """Conectar ao banco de dados PostgreSQL usando SQLAlchemy."""
    engine = create_engine(f'postgresql://user:password@postgres:5432/{nome_banco}')
    return engine


# Função para enviar os dados do CSV para o banco
def enviar_csv_para_postgres(nome_banco, arquivos):
    
    # Conectar ao banco
    engine = conectar_banco(nome_banco)

    criar_tabelas(engine)

    for arquivo in arquivos: 
        # Carregar o CSV para um DataFrame
        df = pd.read_csv("tabelasResultadoETL/" + arquivo.get("caminho_arquivo"))

        # Enviar os dados para o banco de dados usando o método to_sql do Pandas
        df.to_sql(arquivo.get("nome_tabela"), con=engine, if_exists='append', index=False)
        print(f"Dados do {arquivo.get("nome_tabela")}.csv transformados em tabela com sucesso!")

def criar_tabelas(engine):

    # Testar a conexão
    try:
        with engine.connect() as connection:
            print("Conexão estabelecida com sucesso!")
            # Comando SQL para criar uma tabela
            comando_sql = """
            CREATE TABLE IF NOT EXISTS enderecos (
                id BIGINT PRIMARY KEY,
                cidade VARCHAR(100),
                numero INT,
                bairro VARCHAR(90),
                rua VARCHAR(90),
                uf VARCHAR(2)
            );
            CREATE TABLE vendedores (
                id bigint PRIMARY KEY,
                nome varchar(100),
                sobrenome varchar(100),
                email varchar(100),
                data_admissao DATE,
                cargo varchar(100)
            );
            CREATE TABLE produtos (
                id bigint PRIMARY KEY,
                nome varchar(100),
                preco float,
                categoria varchar(100)
            );
            CREATE TABLE clientes (
                id bigint PRIMARY KEY,
                id_endereco bigint,
                nome varchar(100),
                sobrenome varchar(100),
                data_nascimento DATE,
                email varchar(110),
                CONSTRAINT fk_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos(id)
            );
            CREATE TABLE pedidos (
                id bigint PRIMARY KEY,
                id_vendedor bigint,
                id_cliente bigint,
                preco_total float,
                data_pedido DATE,
                comissao float,
                CONSTRAINT fk_vendedor FOREIGN KEY (id_vendedor) REFERENCES vendedores(id),
                CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            );
            CREATE TABLE itens_pedido (
                id bigint PRIMARY KEY,
                id_pedido bigint,
                id_produto bigint,
                preco_produto float,
                quantidade int,
                CONSTRAINT fk_pedido FOREIGN KEY (id_pedido) REFERENCES pedidos(id),
                CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES produtos(id)
            );
            """
            # Executar o comando SQL diretamente no banco
            connection.execute(text(comando_sql))
            connection.commit()
            print("Tabela(s) criada(s) com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

arquivos:list = [
    {"caminho_arquivo":"enderecos.csv",
    "nome_tabela": "enderecos"},
    {"caminho_arquivo":"produtos.csv",
    "nome_tabela": "produtos"},
    {"caminho_arquivo":"vendedores.csv",
    "nome_tabela": "vendedores"},
    {"caminho_arquivo":"clientes.csv",
    "nome_tabela": "clientes"},
    {"caminho_arquivo":"pedidos.csv",
    "nome_tabela": "pedidos"},
    {"caminho_arquivo":"itens_pedido.csv",
    "nome_tabela": "itens_pedido"}
]

enviar_csv_para_postgres("mydatabase", arquivos)