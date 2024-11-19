from faker import Faker
import random
import unicodedata
import datetime

faker = Faker()
fakerBR = Faker("pt_BR")

clientesEstrutura = [
    {"id":"", "id_endereco":"", "nome":"", "sobrenome":"", "dataNascimento":"", "celular":"", "email":""}
]
produtosEstrutura = [
    {"id":"", "nome":"", "preco":"", "categoria":""}
]
enderecosEstrutura = [
    {"id":"", "cidade":"", "numero":"", "bairro":"", "rua":"", "uf":""}
]
vendedoresEstrutura = [
    {"id":int, "nome":str, "email":str, "dataAdmissao":datetime, "cargo":str}
]
vendasEstrutura = [
    {"id":"", "id_vendedor":"", "id_cliente":"", "preco_total":"", "data_venda":"", "comissao":""}
]
itemVendaEstrutura = [
    {"id":"", "id_venda":"", "id_produto":"", "preco_produto":"", "quantidade":""}
]

clientes = []
enderecos = []
vendedores = []
vendedores.append(vendedoresEstrutura)
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

def criarClientesEnderecos():
    print("Criando Clientes e seus endereços...")
    for i in range(30000, 30011):
        endereco = {
            "id":random.randint(1, 100000),
            "cidade":fakerBR.city(),
            "numero":fakerBR.building_number(),
            "bairro":fakerBR.bairro(),
            "rua":fakerBR.street_name(),
            "uf":fakerBR.estado_sigla()
        }

        nome = faker.first_name()
        sobrenome = faker.last_name()
        cliente = {
            "id":i,
            "id_endereco":endereco.get("id"),
            "nome":nome,
            "sobrenome":sobrenome,
            "dataNascimento": faker.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d-%m-%Y'),  # Formata a data
            "celular": fakerBR.cellphone_number(),
            "email":f"{remover_acentos(nome.lower())}{remover_acentos(sobrenome.lower())}{getDominioEmail()}" # Formata o e-mail com nome e sobrenome
        }
        clientes.append(cliente)
        enderecos.append(endereco)
    return clientes, enderecos

def showClients(clientes):
    for cliente in clientes:
        print(f'\n"id":{cliente.get("id")},\n"id_endereco":{cliente.get("id_endereco")},\n"nome":{cliente.get("nome")},\n"sobrenome":{cliente.get("sobrenome")},\n"dataNascimento":{cliente.get("dataNascimento")},\n"celular":{cliente.get("celular")},\n"email":{cliente.get("email")}')


def criarVendedores() -> list: # criar vendedores
    print("Criando vendedores...")
    for i in range(80000, 80011): # Definindo o range do id
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
    return vendedores


def criarProdutos():
    produtos = [
        {"id":303, "nome":"Violão Start Giannini", "preco":300, "categoria":"Música"},
        {"id":34, "nome":"Guaravita", "preco":5.50, "categoria":"Refrigerante"},
        {"id":398, "nome":"Piano", "preco":10000, "categoria":"Música"},
        {"id":234, "nome":"Playstation 5", "preco":3000, "categoria":"Entretenimento"},
        {"id":3, "nome":"Kwid", "preco":30000, "categoria":"Automóvel"},
        {"id":3032, "nome":"Sandália", "preco":50, "categoria":"Roupa"},
    ]
    return produtos

# def criarEnderecos():
#     pass

def criarVendas():
    for i in range(100000, 100011):
        preco_total:float = 0
        for x in range(1, random.randint(2, 4)): 
            item = criarItemVenda(i)
            preco_total += (float)(item[0].get("preco_produto"))

        id_vendedor = random.choice(vendedores)["id"]
        id_cliente = random.choice(clientes)["id"]
        venda = {"id":i,
                "id_vendedor":id_vendedor,
                "id_cliente":id_cliente,
                "preco_total":preco_total,
                "data_venda":faker.date_of_birth(minimum_age=0, maximum_age=15).strftime('%Y-%m-%d'),
                "comissao":round( preco_total * 0.04, 2)
                }
        print(venda)

def criarItemVenda(id:int):
    produto = random.choice(produtos) # ajustar quantidade através do preço
    item_venda = [
        {"id":random.randint(0, 999999999),
         "id_venda":id,
         "id_produto":produto.get("id"),
         "preco_produto":produto.get("preco"),
         "quantidade":random.randint(1, 5)}
    ]
    vendas.append(item_venda)
    return item_venda
    

clientes, enderecos = criarClientesEnderecos()
vendedores = criarVendedores()
produtos = criarProdutos()
vendas = criarVendas()

for i in produtos:
    print(i)