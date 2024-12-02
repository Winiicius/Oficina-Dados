# Oficina-Dados

Este repositório tem como objetivo armazenar/disponibilizar os códigos usados na **Oficina de Dados** que será ofertada no **SEMITI VIII**.

A oficina será lecionada por **Winicius**, **Carlos Ryan** e **Rharhuandrew Souza**, e terá como objetivo mostrar uma introdução aos processos de: **ETL**, **SQL para Análise de Dados** e **visualização de dados no Power BI**.

---

## Guias

- [Explicando cada classe](#explicando-cada-classe)
- [Como Usar?](#como-usar)
- [Bibliotecas](#bibliotecas)
- [Instrutores](#instrutores)

---

## Explicando cada classe

### Primeira Etapa: **[fakerScript.py](faker/fakerScript.py)**

A primeira etapa do projeto envolve a utilização da biblioteca [Faker](#faker) para gerar dados falsos. Esses dados são usados para preencher as linhas dos arquivos CSV que serão manipulados nas etapas seguintes.

Os dados gerados contêm erros propositais, como:
- IDs de clientes e vendedores nulos
- Emails inválidos
- Clientes duplicados
- Vendas referenciando IDs inexistentes de clientes e vendedores

Após rodar o código, os arquivos CSV gerados estarão localizados na pasta **[tabelasResultadoFaker](tabelasResultadoFaker/)**.

A estrutura das tabelas pode ser visualizada no diagrama: **[diagrama.png](Diagrama/Diagrama.png)**.

### Segunda Etapa: **[ETL.py](ETL/ETL.py)**

A segunda etapa é a **transformação dos dados**, usando a biblioteca [Pandas](#pandas). O código se encarrega de tratar os erros dos arquivos CSV gerados na etapa anterior, como valores nulos e duplicados.

Após rodar o código, os arquivos CSV tratados estarão na pasta **[tabelasResultadoETL](tabelasResultadoETL/)**.

### Última Etapa: **[ConfiguracoesBanco.py](ETL/ConfiguracoesBanco.py)**

Na última etapa, utilizamos as bibliotecas **[psycopg2](#psycopg2)** e **[SQLAlchemy](#sqlalchemy)** para interagir com o banco de dados PostgreSQL.

- **psycopg2** é usado para criar o banco de dados PostgreSQL.
- **SQLAlchemy** é utilizado para criar as tabelas no banco de dados e para inserir os dados dos arquivos CSV.

Após rodar o código, o banco e as tabelas estarão criados no PostgreSQL, prontos para uso.

---

## Como usar?

### Instalação das Bibliotecas

Primeiramente, instale as bibliotecas necessárias executando o comando abaixo no terminal:

```bash
pip install pandas Faker sqlalchemy psycopg2-binary
```

bibliotecas instaladas, vamos rodar a classe [fakerScript.py](faker/fakerScript.py), isso vai gerar 6 arquivos CSV com erros propositais para serem tratados na próxima etapa. 

Agora na classe [ETL.py](ETL/ETL.py) será onde vamos usar o pandas tratar os erros da nossa base de dados, após fazer todo processo de tratamento dos dados, os mesmo arquivos CSV, mas agora sem erros, serão salvos na pasta [tabelasResultadoETL](tabelasResultadoETL/).

### Integração com PostgreSQL (Opcional)

E por último, na classe [ConfiguracaoBanco](ETL/ConfiguracoesBanco.py), é onde é feito a integração com o postgreSQL, é onde os arquivos CSV e seus dados são tranformados em tabelas no postgres

### Importação dos dados no Power Bi

...




# Bibliotecas

## [Faker](https://faker.readthedocs.io/en/master/)

A biblioteca Faker é usada para gerar dados fictícios. Ela cria informações como nomes, endereços, emails e outros dados aleatórios, permitindo a simulação de grandes volumes de dados para testes, sem comprometer a privacidade.

- Usada em: [fakerScript.py](faker/fakerScript.py)
- Função: Geração de dados falsos para preencher os arquivos CSV com informações de clientes, vendedores, vendas, etc.

## [Pandas](https://pandas.pydata.org/docs/reference/index.html)

O Pandas é uma biblioteca poderosa para análise e manipulação de dados. Ele permite carregar, limpar, transformar e analisar dados de diversas fontes, como arquivos CSV, Excel e bancos de dados.

- Usada em: [ETL.py](ETL/ETL.py)
- Função: Manipulação e tratamento dos dados, como a remoção de valores nulos, filtragem de dados e correção de erros nos arquivos CSV.

## [sqlalchemy](https://docs.sqlalchemy.org/en/20/)

- O SQLAlchemy é uma biblioteca ORM (Object Relational Mapper) para Python, que fornece uma interface para interagir com bancos de dados relacionais de forma mais abstrata, sem a necessidade de escrever SQL manualmente.

- Usada em: [ConfiguracoesBanco.py](ETL/ConfiguracoesBanco.py)
- Função: Criação de tabelas no banco de dados PostgreSQL e inserção de dados dos arquivos CSV nas tabelas.


## [psycopg2](https://www.psycopg.org/docs/)

O psycopg2 é um adaptador de banco de dados PostgreSQL para Python. Ele é usado para conectar e executar comandos SQL em bancos de dados PostgreSQL.

- Usada em: [ConfiguracoesBanco.py](ETL/ConfiguracoesBanco.py)
- Função: Criação do banco de dados PostgreSQL e execução de comandos SQL para manipulação do banco.

# Instrutores

<div style="display: flex; justify-content: space-around; align-items: center; gap: 20px;">
  <!-- Winicius -->
  <div style="text-align: center;">
    <strong>Winicius</strong>
    <p></p>
    <p>
      <a href="https://github.com/Winiicius" rel="noopener">
        <img width="100" height="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/102719335?v=4" alt="Foto Winicius">
      </a>
    </p>
    <p>
      <a href="www.linkedin.com/in/winicius-alexandre-066a92248" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
      </a>
    </p>
  </div>

  <!-- Rharhuandrew -->
  <div style="text-align: center;">
  <strong>Rharhuandrew</strong>
    <p></p>
    <p>
      <a href="https://github.com/rharhuandew" rel="noopener">
        <img width="100" height="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/100100347?v=4" alt="Foto Rharhuandrew">
      </a>
    </p>
    <p>
      <a href="https://www.linkedin.com/in/rharhuandrew-souza/" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
      </a>
    </p>
    
  </div>

  <!-- Ryan -->
  <div style="text-align: center;">
    <strong>Carlos Ryan</strong>
    <p></p>
    <p>
      <a href="https://github.com/carlosryan" rel="noopener">
        <img width="100" height="100" style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/140994484?v=4" alt="Foto Carlos Ryan">
      </a>
    </p>
    <p>
      <a href="https://www.linkedin.com/in/carlos-ryan-726820279/" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
      </a>
    </p>
    
  </div>
</div>
