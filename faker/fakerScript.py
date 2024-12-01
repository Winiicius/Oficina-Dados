from faker import Faker
import random
import unicodedata
import csv
import time

faker = Faker() # Faker com dados em inglês
fakerBR = Faker("pt_BR") # Faker com dados em português brasileiro

clientes = []
enderecos = []
vendedores = []
produtos = []
pedidos = []
itensPedido = []

def getDominioEmail() -> str:
    emails = ["@gmail.com",
            "@yahoo.com",
            "@hotmail.com",
            "@outlook.com",
            "@icloud.com",
            "@aol.com",
            "@live.com",
            "@msn.com",
            "@mail.com",
            "@protonmail.com",
            "@yandex.com",
            "@zoho.com",
            "@tutanota.com",
            "@fastmail.com",
            "@gmx.com"
    ]
    dominio_aleatorio = random.choice(emails)
    if (random.random() <= 0.02):
        dominio_aleatorio = "@emailinvalido.com"
    return dominio_aleatorio;

def getCargo():
    # Lista de cargos e suas respectivas probabilidades
    cargos = ["Vendedor Interno", "Telemarketing", "Vendedor Externo", "Promotor de Vendas", "Consultor de Vendas"]
    pesos = [15, 10, 7, 3, 1]  # Probabilidades relativas (quanto maior o número, maior a chance)

    return random.choices(cargos, weights=pesos, k=1)[0]  # Escolhe 1 cargo com base nos pesos


def remover_acentos(texto):
    # Normaliza a string para a forma "NFD" (caracter base + marcas de acentuação separadas)
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtra apenas caracteres que não são marcas de acentuação
    texto_sem_acento = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acento

def criarEndereco():
    endereco = {
            "id":random.randint(1, 10000000000), # garantir que o id não se repita
            "cidade":fakerBR.city(), # Gera Cidade aleatória
            "numero":fakerBR.building_number(), # Gera número de casa aleatório
            "bairro":fakerBR.bairro(), # Gera bairro aleatório
            "rua":fakerBR.street_name(), # Gera nome da rua aleatório
            "uf":fakerBR.estado_sigla() # Gera sigla de estado aleatória
        }
    enderecos.append(endereco) # Adiciona o endereco atual na lista de todos os endereços
    return endereco

def criarClientesEnderecos():
    print("Criando Clientes e seus endereços . . .")
    for i in range(30000, 35001): # os ids dos clientes vão de 30000 até a quantidade de preferência
        id_cliente = i if random.random() > 0.01 else "null"; # Chance de deixar o id null ( random.random() gera um número entre 0 e 1, se o número gerado for menor que 0.01 ele atribui null para o id do cliente )
        endereco = criarEndereco() # Chama a função criar endereço ( linha 54 )
        nome = faker.first_name() # Gera um nome aleatório
        sobrenome = faker.last_name() # Gera um sobrenome aleatório
        cliente = { # Definindo corpo da entidade Cliente
            "id":id_cliente,
            "id_endereco":endereco.get("id"), # Pega o id do endereço criado
            "nome":nome,
            "sobrenome":sobrenome,
            "data_nascimento": faker.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),  # Gera uma data de no mínimo 18 anos e no máximo 80, no formato -> ano/mês/dia
            "celular": fakerBR.cellphone_number(), # Gera um número de telefone aleatório
            "email":f"{remover_acentos(nome.lower())}{remover_acentos(sobrenome.lower())}{getDominioEmail()}" # Formata o e-mail com nome e sobrenome sem acentos e um domínio aleatório ( linha 17 )
        }
        clientes.append(cliente) # Adiciona o cliente na lista de todos os clientes
        if (random.random() < 0.01): # Chance de duplicar o cliente
            clientes.append(cliente)
    time.sleep(2) # Espera 2 segundos
    return clientes, enderecos

def criarVendedores() -> list: # criar vendedores
    print("Criando vendedores . . .")
    for i in range(80000, 82001): # Definindo o range do id
        nomeCompleto = fakerBR.name().split(" ") # se o nome for composto, divido o nome em um array
        sobrenomeArray = fakerBR.last_name().split(" ") # Se o sobrenome for composto, divido ele em um array
        sobrenome = sobrenomeArray[0] if len(sobrenomeArray) == 1 else sobrenomeArray[1] # se sobrenome for composto(ex: de sá, dos anjos) retiro o prefixo e guardo o resto do nome(sá, anjos)
        nome = nomeCompleto[0] + " " + nomeCompleto[1] if len(nomeCompleto) <= 2 else nomeCompleto[1] + " " + nomeCompleto[2] # As vezes os nome vem com prefixo(ex: sr. sra., etc) esse código serve pra evitar isso 
        
        # Definindo corpo da entidade Vendedor
        vendedor = {"id": i if random.random() > 0.01 else "null", # Chance do id ser null
                    "nome":nome,
                    "sobrenome":sobrenome,
                    "email":f"{remover_acentos(nomeCompleto[1].lower())}{remover_acentos(sobrenome.lower())}@nomeEmpresa.com", # Formata o e-mail com nome e sobrenome sem acentos.
                    "data_admissao":faker.date_of_birth(minimum_age=0, maximum_age=20).strftime('%Y-%m-%d'), # gera uma data entre 0 e 20 anos atrás no formatp ano/mes/dia
                    "cargo":getCargo() # Retorna um cargo ( linha 39 )
                }
        vendedores.append(vendedor) # adiciona o Vendedor na lista de todos os vendedores
    time.sleep(2) # Espera dois segundos
    return vendedores


def criarProdutos(): # não adicionar produtos com valores muito caros!!! entre 0 e 3000/5000
    print("Criando os Produtos . . .")
    produtos = [ # Criando produtos de sua preferência
        {"id":303, "nome":"Violão Start Giannini", "preco":300, "categoria":"Música"},
        {"id":34, "nome":"Guaravita", "preco":5.50, "categoria":"Refrigerante"},
        {"id":398, "nome":"Piano", "preco":10000, "categoria":"Música"},
        {"id":234, "nome":"Playstation 5", "preco":3000, "categoria":"Entretenimento"},
        {"id":3, "nome":"Kwid", "preco":30000, "categoria":"Automóvel"},
        {"id":3032, "nome":"Sandália", "preco":50, "categoria":"Vestimenta"},
        
    ]
    time.sleep(2)
    return produtos

def criarPedidos(): # Cria um pedido e seus itens pedido
    print("Criando pedidos e itens pedidos . . .")
    for i in range(100000, 110001): # Definindo o range do id de pedidos

        id_vendedor = random.choice(vendedores)["id"] # A partir da lista de todos os vendedores pego o id de um vendedor aleatório
        cliente = random.choice(clientes) # A partir da lista de todos os clientes pego um cliente aleatório
        id_cliente = cliente["id"] # Pego o id do clientes escolhido
        
        fake = False # Flag usado para saber se o id do cliente ou vendedor é null

        if(id_cliente == "null" or id_vendedor == "null"): # Se o id do vendedor ou do cliente for "null", fake = True
            fake = True

        preco_total:float = 0

        for x in range(1, random.randint(2, 4)): 
            item = criarItemPedido(i) # crio os itens do pedido
            preco_total += (item.get("preco_produto") * item.get("quantidade")) # Para cada item, guardo o valor da quantidade * o valor do produto, depoi somo tudo e atribuo ao preco_total

        pedido = {"id":i,
                "id_vendedor":id_vendedor if fake == False else random.randint(1, 20000), # Se o id de cliente ou vendedor igual a null, crio um id que não existe
                "id_cliente":id_cliente if fake == False else random.randint(1, 20000), # Se o id de cliente ou vendedor igual a null, crio um id que não existe
                "preco_total":preco_total,
                "data_pedido":faker.date_of_birth(minimum_age=0, maximum_age=15).strftime('%Y-%m-%d')
                # "comissao":round( preco_total * 0.04, 2)
                }
        pedidos.append(pedido)
    time.sleep(2)
    return pedidos

def criarItemPedido(id:int):
    produto = random.choice(produtos) # Escolhe um produto aleatoriamente
    
    quantidadeMaxima = 0 # quantidade maxima de produtos que podem ser comprados

    precoProduto = produto.get("preco")
    if( precoProduto < 250): quantidadeMaxima = 7 # Quanto maior o valor do produto, menor é a quantidade que ele pode comprar do mesmo
    elif( precoProduto < 500 ): quantidadeMaxima = 5 
    elif( precoProduto < 750 ): quantidadeMaxima = 4
    else: quantidadeMaxima = 2
    item_pedido = {
        "id":random.randint(0, 99999999999999), # número alto para evitar replicação de id
         "id_pedido":id,
         "id_produto":produto.get("id"), # Pega o id do pedido
         "preco_produto":precoProduto, # Pega o preco do produto
         "quantidade":random.randint(1, quantidadeMaxima) # Gera um número de 1 a 4, que é a quantidade de produto comprada
    }
    itensPedido.append(item_pedido) # Adiciona o item pedido na lista de todos os itens pedido
    return item_pedido
    
produtos = criarProdutos()
clientes, enderecos = criarClientesEnderecos()
vendedores = criarVendedores()
pedidos = criarPedidos()
print("Base de Dados Criada!!!!!")


def criar_arquivo_csv(nome_arquivo, lista_objeto):
    with open("tabelasResultadoFaker/" + nome_arquivo, mode="w", newline="", encoding="UTF-8") as arquivo: # intelliJ -> ../tabelasResultadoFaker/
        # Criar o objeto writer
        escritor = csv.DictWriter(arquivo, fieldnames=lista_objeto[0].keys())
        # Escrever o cabeçalho
        escritor.writeheader()
        # Escrever os dados
        # lista_embaralhada = random.shuffle(lista_objeto[1:]) # checar
        escritor.writerows(lista_objeto)

arquivos = [
        {
        "nome_arquivo":"produtos.csv",
        "lista_objeto":produtos
        },
        {
        "nome_arquivo":"enderecos.csv",
        "lista_objeto":enderecos
        },
        {
        "nome_arquivo":"clientes.csv",
        "lista_objeto":clientes
        },
        {
        "nome_arquivo":"vendedores.csv",
        "lista_objeto":vendedores
        },
        {
        "nome_arquivo":"pedidos.csv",
        "lista_objeto":pedidos
        },
        {
        "nome_arquivo":"itens_pedido.csv",
        "lista_objeto":itensPedido
        },
    ]

for arquivo in arquivos:
    criar_arquivo_csv(arquivo.get("nome_arquivo"), arquivo.get("lista_objeto"))


