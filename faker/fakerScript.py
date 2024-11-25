from faker import Faker
import random
import unicodedata
import csv
import time

faker = Faker()
fakerBR = Faker("pt_BR")

clientes = []
enderecos = []
vendedores = []
produtos = []
vendas = []
itensVendas = []

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
            "id":random.randint(1, 100000),
            "cidade":fakerBR.city(),
            "numero":fakerBR.building_number(),
            "bairro":fakerBR.bairro(),
            "rua":fakerBR.street_name(),
            "uf":fakerBR.estado_sigla()
        }
    enderecos.append(endereco)
    return endereco

def criarClientesEnderecos():
    print("Criando Clientes e seus endereços . . .")
    for i in range(30000, 30011):
        id_cliente = i if random.random() > 0.01 else "null";
        endereco = criarEndereco()
        nome = faker.first_name()
        sobrenome = faker.last_name()
        cliente = {
            "id":id_cliente,
            "id_endereco":endereco.get("id"),
            "nome":nome,
            "sobrenome":sobrenome,
            "dataNascimento": faker.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d-%m-%Y'),  # Formata a data
            "celular": fakerBR.cellphone_number(),
            "email":f"{remover_acentos(nome.lower())}{remover_acentos(sobrenome.lower())}{getDominioEmail()}" # Formata o e-mail com nome e sobrenome
        }
        clientes.append(cliente)
        if (random.random() < 0.01):
            clientes.append(cliente) 
    time.sleep(2)
    return clientes, enderecos



def showClients(clientes):
    for cliente in clientes:
        print(f'\n"id":{cliente.get("id")},\n"id_endereco":{cliente.get("id_endereco")},\n"nome":{cliente.get("nome")},\n"sobrenome":{cliente.get("sobrenome")},\n"dataNascimento":{cliente.get("dataNascimento")},\n"celular":{cliente.get("celular")},\n"email":{cliente.get("email")}')


def criarVendedores() -> list: # criar vendedores
    print("Criando vendedores . . .")
    for i in range(80000, 80010): # Definindo o range do id
        nomeCompleto = fakerBR.name().split(" ") # divido o nome em um array
        sobrenomeArray = fakerBR.last_name().split(" ") # uso o faker para gerar um sobrenome
        sobrenome = sobrenomeArray[0] if len(sobrenomeArray) == 1 else sobrenomeArray[1] # se sobrenome for composto(ex: de sá, dos anjos) retiro o prefixo e guardo o resto do nome(sá, anjos)
        nome = nomeCompleto[0] + " " + nomeCompleto[1] if len(nomeCompleto) <= 2 else nomeCompleto[1] + " " + nomeCompleto[2] # As vezes os nome vem com prefixo(ex: sr. sra., etc) esse código serve pra evitar isso 
        
        # Criando corpo da entidade vendedor
        vendedor = {"id":i,
                    "nome":nome,
                    "sobrenome":sobrenome,
                    "email":f"{remover_acentos(nomeCompleto[1].lower())}{remover_acentos(sobrenome.lower())}@nomeEmpresa.com",
                    "dataAdmissao":faker.date_of_birth(minimum_age=0, maximum_age=20).strftime('%Y-%m-%d'), # gera uma data entre 0 e 20 anos atrás 
                    "cargo":getCargo()
                }
        vendedores.append(vendedor) # adiciona o vendedor na lista de vendedores
    time.sleep(2)
    return vendedores


def criarProdutos(): # não adicionar produtos com valores muito caros!!! entre 0 e 3000/5000
    print("Criando os Produtos . . .")
    produtos = [
        {"id":303, "nome":"Violão Start Giannini", "preco":300, "categoria":"Música"},
        {"id":34, "nome":"Guaravita", "preco":5.50, "categoria":"Refrigerante"},
        {"id":398, "nome":"Piano", "preco":10000, "categoria":"Música"},
        {"id":234, "nome":"Playstation 5", "preco":3000, "categoria":"Entretenimento"},
        {"id":3, "nome":"Kwid", "preco":30000, "categoria":"Automóvel"},
        {"id":3032, "nome":"Sandália", "preco":50, "categoria":"Roupa"},
    ]
    time.sleep(2)
    return produtos

def criarVendas():
    print("Criando vendas e itens venda . . .")
    for i in range(100000, 100010):
        preco_total:float = 0
        # se id == None
        id_vendedor = random.choice(vendedores)["id"]
        # se o email == invalido, não asssocialo a venda, excluir endereço atribuído
        cliente = random.choice(clientes)
        id_cliente = cliente["id"]
        fake = False
        if(id_cliente == "null" or id_vendedor == "null"): # or "@invalidemail.com" in email_cliente ): # vou renomear os emails
            fake = True

        for x in range(1, random.randint(2, 4)): 
            item = criarItemVenda(i)
            preco_total += (item.get("preco_produto"))

        venda = {"id":i,
                "id_vendedor":id_vendedor if fake == False else random.randint(1, 20000),
                "id_cliente":id_cliente if fake == False else random.randint(1, 20000),
                "preco_total":preco_total,
                "data_venda":faker.date_of_birth(minimum_age=0, maximum_age=15).strftime('%Y-%m-%d'),
                "comissao":round( preco_total * 0.04, 2)
                }
        vendas.append(venda)
    time.sleep(2)
    return vendas

def criarItemVenda(id:int):
    produto = random.choice(produtos) # ajustar quantidade através do preço
    item_venda = {
        "id":random.randint(0, 99999999999999),
         "id_venda":id,
         "id_produto":produto.get("id"),
         "preco_produto":produto.get("preco"),
         "quantidade":random.randint(1, 5)
    }
    itensVendas.append(item_venda)
    return item_venda
    

produtos = criarProdutos()
clientes, enderecos = criarClientesEnderecos()
vendedores = criarVendedores()
vendas = criarVendas()
print("Base de Dados Criada!!!!!")


def criar_arquivo_csv(nome_arquivo, lista_objeto):
    with open("tabelasResultadoFaker/" + nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        # Criar o objeto writer
        escritor = csv.DictWriter(arquivo, fieldnames=lista_objeto[0].keys())
        # Escrever o cabeçalho
        escritor.writeheader()
        # Escrever os dados
        escritor.writerows(lista_objeto)

arquivos = [{
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
        "nome_arquivo":"vendas.csv",
        "lista_objeto":vendas
        },
        {
        "nome_arquivo":"itens_venda.csv",
        "lista_objeto":itensVendas
        },
    ]

for arquivo in arquivos:
    criar_arquivo_csv(arquivo.get("nome_arquivo"), arquivo.get("lista_objeto"))


