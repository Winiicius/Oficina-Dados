DROP TABLE IF EXISTS itens_venda;
DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS vendedores;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS enderecos;

CREATE TABLE enderecos (
    id bigint PRIMARY KEY,
    cidade varchar(100),
    numero int,
    bairro varchar(90),
    rua varchar(90),
    uf varchar(2)
);

CREATE TABLE vendedores (
    id bigint PRIMARY KEY,
    nome varchar(100),
    sobrenome varchar(100),
    email varchar(100),
    dataAdmissao DATE,
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
    dataNascimento DATE,
    celular varchar(100),
    email varchar(110),
    CONSTRAINT fk_endereco FOREIGN KEY (id_endereco) REFERENCES enderecos(id)
);
CREATE TABLE vendas (
    id bigint PRIMARY KEY,
    id_vendedor bigint,
    id_cliente bigint,
    preco_total float,
    data_venda DATE,
    comissao float,
    CONSTRAINT fk_vendedor FOREIGN KEY (id_vendedor) REFERENCES vendedores(id),
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
CREATE TABLE itens_venda (
    id bigint PRIMARY KEY,
    id_venda bigint,
    id_produto bigint,
    preco_produto float,
    quantidade int,
    CONSTRAINT fk_venda FOREIGN KEY (id_venda) REFERENCES vendas(id),
    CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES produtos(id)
);

-- vendas por ano
	SELECT 
	    EXTRACT(YEAR FROM data_venda) AS ano,
	    COUNT(*) AS numero_de_vendas
	FROM 
	    vendas
	GROUP BY 
	    ano
	ORDER BY 
	    ano;
--

 
SELECT * FROM enderecos;
SELECT * FROM clientes;
SELECT * FROM vendas;
SELECT * FROM itens_venda;
SELECT * FROM vendedores;
SELECT * FROM produtos;

-- vendedores - id,nome,sobrenome,email,dataAdmissao,cargo
-- vendas - id,id_vendedor,id_cliente,preco_total,data_venda,comissao
-- produtos - id,nome,preco,categoria
-- clientes - id,id_endereco,nome,sobrenome,dataNascimento,celular,email
-- itens_venda - id,id_venda,id_produto,preco_produto,quantidade
-- enderecos - id, cidade, numero, bairro, rua, uf

SET client_encoding TO 'UTF-8' -- Rodar esse código antes de prosseguir

\COPY enderecos(id, cidade, numero, bairro, rua, uf) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\enderecos.csv' DELIMITER ',' CSV HEADER;
\COPY clientes(id,id_endereco,nome,sobrenome,dataNascimento,celular,email) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\clientes.csv' DELIMITER ',' CSV HEADER;
\COPY vendedores(id,nome,sobrenome,email,dataAdmissao,cargo) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\vendedores.csv' DELIMITER ',' CSV HEADER;
\COPY produtos(id,nome,preco,categoria) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\produtos.csv' DELIMITER ',' CSV HEADER;
\COPY vendas(id,id_vendedor,id_cliente,preco_total,data_venda,comissao) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\vendas.csv' DELIMITER ',' CSV HEADER;
\COPY itens_venda(id,id_venda,id_produto,preco_produto,quantidade) FROM 'C:\Users\202115020017\IdeaProjects\oficina-dados\Oficina-Dados\tabelasResultadoFaker\itens_venda.csv' DELIMITER ',' CSV HEADER;



