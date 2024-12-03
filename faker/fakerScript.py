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
    if (random.random() <= 0.05):
        dominio_aleatorio = "null"
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
        dominioEmail = getDominioEmail(); # Retorna um domínio de email aleatório da lista( chance baixa de retornar null )
        cliente = { # Definindo corpo da entidade Cliente
            "id":id_cliente,
            "id_endereco":endereco.get("id"), # Pega o id do endereço criado
            "nome":nome,
            "sobrenome":sobrenome,
            "data_nascimento": faker.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),  # Gera uma data de no mínimo 18 anos e no máximo 80, no formato -> ano/mês/dia
            "celular": fakerBR.cellphone_number(), # Gera um número de telefone aleatório
            "email":f"{remover_acentos(nome.lower())}{remover_acentos(sobrenome.lower())}{dominioEmail}" if dominioEmail != "null" else dominioEmail # Formata o e-mail com nome e sobrenome sem acentos e um domínio aleatório ( linha 17 ), se dominio email diferente de null, ele pqgao nome e sobrenome e coloca um domínio aleatório, se não, email = null
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
                    "email":f"{remover_acentos(nomeCompleto[1].lower())}{remover_acentos(sobrenome.lower())}@rwcimportados.com", # Formata o e-mail com nome e sobrenome sem acentos.
                    "data_admissao":faker.date_of_birth(minimum_age=0, maximum_age=20).strftime('%Y-%m-%d'), # gera uma data entre 0 e 20 anos atrás no formatp ano/mes/dia
                    "cargo":getCargo() # Retorna um cargo ( linha 39 )
                }
        vendedores.append(vendedor) # adiciona o Vendedor na lista de todos os vendedores
    time.sleep(2) # Espera dois segundos
    return vendedores


def criarProdutos():
    print("Criando os Produtos . . .")
    produtos = [ # Criando produtos de sua preferência
        {"id":303, "nome":"Violão Start Giannini", "preco":300, "categoria":"Música"},
        {"id":34, "nome":"Guaravita", "preco":5.50, "categoria":"Consumível"},
        {"id":398, "nome":"Piano", "preco":2500, "categoria":"Música"},
        {"id":234, "nome":"Playstation 5", "preco":3000, "categoria":"Entretenimento"},
        {"id":30, "nome":"Fila de Prova", "preco":25, "categoria":"Ilegal"},
        {"id":32, "nome":"Jogo do tigrinho (desperte a fera em você)", "preco":55, "categoria":"Ilegal"},
        {"id":31, "nome":"Dolly Guaraná", "preco":2, "categoria":"Consumível"},
        {"id":101, "nome":"Chinelo Havaianas", "preco":20, "categoria":"Vestimenta"},
        {"id":402, "nome":"Teclado Mecânico RGB", "preco":350, "categoria":"Tecnologia"},
        {"id":76, "nome":"Como ser pago apresentando SEMIT", "preco":150, "categoria":"Desabafo"},
        {"id":222, "nome":"Curso de como ficar rico rápido (não funciona)", "preco":199, "categoria":"Ilegal"},
        {"id":98, "nome":"Travesseiro Nuvem", "preco":80, "categoria":"Casa"},
        {"id":55, "nome":"Kit de Piadas (Cairam os preços da loja...)", "preco":35, "categoria":"Entretenimento"},
        {"id":112, "nome":"Efeitos Sonoros (Rodrigo Faro)", "preco":15, "categoria":"Entretenimento"},
        {"id":404, "nome":"Pão de Queijo Imaginário", "preco":1000, "categoria":"Ilusão"},
        {"id":1010, "nome":"Treinador de Pokémon", "preco":499, "categoria":"Jogos"},
        {"id":89, "nome":"Roupa do Neymar (autenticada pelo primo dele)", "preco":1000, "categoria":"Colecionáveis"},
        {"id":17, "nome":"Jogo da Vida versão hardcore (Você já esta jogando)", "preco":49, "categoria":"Jogos"},
        {"id":99, "nome":"Pneu recondicionado (meio quadrado)", "preco":120, "categoria":"Automóvel"},
        {"id":1234, "nome":"O molho", "preco":250, "categoria":"Entretenimento"},
        {"id":56, "nome":"Microondas do Futuro (ainda não chegou)", "preco":1500, "categoria":"Tecnologia"},
        {"id":33, "nome":"Relógio que só funciona aos sábados", "preco":300, "categoria":"Acessório"},
        {"id":801, "nome":"Moto usada com adesivo 'Vai na Fé'", "preco":5000, "categoria":"Automóvel"},
        {"id":802, "nome":"Carro de controle remoto turbo", "preco":200, "categoria":"Automóvel"},
        {"id":901, "nome":"Camiseta com frase motivacional reversa", "preco":45, "categoria":"Vestimenta"},
        {"id":902, "nome":"Boné Invisível (altamente funcional)", "preco":60, "categoria":"Vestimenta"},
        {"id":1301, "nome":"Fone (que não enrola)", "preco":100, "categoria":"Tecnologia"},
        {"id":1302, "nome":"Carregador solar para celulares noturnos", "preco":300, "categoria":"Tecnologia"},
        {"id":1401, "nome":"Suco Gummy Bear", "preco":4.99, "categoria":"Consumível"},
        {"id":1402, "nome":"Coca-cola", "preco":6.50, "categoria":"Consumível"},
        {"id":1403, "nome":"Fanta sabor esperança pelo dia de amanhã", "preco":5.00, "categoria":"Consumível"},
        {"id":1601, "nome":"Pulseira da Sorte (não testada), boa sorte ao testar", "preco":50, "categoria":"Acessório"},
        {"id":1602, "nome":"Cinto Multifuncional (com abridor de garrafa)", "preco":120, "categoria":"Acessório"},
        {"id":1603, "nome":"O Jogo", "preco":300, "categoria":"Jogos"},
        {"id":1701, "nome":"Guia para lidar com o estresse de reuniões intermináveis, EU NÃO TÔ ESTRESSADO", "preco":99.99, "categoria":"Desabafo"},
        {"id":2101, "nome":"Miniatura do Titanic (já quebrada)", "preco":500, "categoria":"Colecionáveis"},
        {"id":2201, "nome":"Óculos", "preco":150, "categoria":"Acessório"},
        {"id":2301, "nome":"Fanta Uvas", "preco":3.50, "categoria":"Consumível"},
        {"id":2302, "nome":"Action-Figure do Mario Abrindo o ...", "preco":120, "categoria":"Colecionáveis"},
        {"id":2303, "nome":"Colar mágico (não garante poderes)", "preco":200, "categoria":"Acessório"},
        {"id":2304, "nome":"Fanta Laranja", "preco":4.99, "categoria":"Consumível"},
        {"id":2305, "nome":"Relógio vintage com despertador sonoro", "preco":800, "categoria":"Colecionáveis"},
        {"id":2306, "nome":"Chaveiro com abridor de garrafas", "preco":10, "categoria":"Acessório"},
        {"id":2307, "nome":"Refrigerante com gás extra (muito gaseificado)", "preco":5.50, "categoria":"Consumível"},
        {"id":2308, "nome":"Quadro", "preco":125, "categoria":"Colecionáveis"},
        {"id":2309, "nome":"Anel de compromisso com você mesmo", "preco":150, "categoria":"Acessório"},
        {"id":2801, "nome":"Jaqueta de Couro de Largatixa", "preco":250, "categoria":"Vestimenta"},
        {"id":2802, "nome":"Calça Jeans", "preco":150, "categoria":"Vestimenta"},
        {"id":2803, "nome":"Meias Esportivas (kit com 3 pares)", "preco":40, "categoria":"Vestimenta"},
        {"id":2901, "nome":"Receita de Sonegação de Imposto", "preco":299, "categoria":"Ilegal"},
        {"id":2902, "nome":"Clonagem de Cartão (insira os dados do seu cartão)", "preco":500, "categoria":"Ilegal"},
        {"id":2903, "nome":"Curso de Como Hackear suas Senhas (é só anota-las)", "preco":350, "categoria":"Ilegal"},
        {"id":3001, "nome":"Cabo HDMI sem o I", "preco":50, "categoria":"Tecnologia"},
        {"id":3002, "nome":"Carregador Portátil (00.000mAh)", "preco":150, "categoria":"Tecnologia"},
        {"id":3003, "nome":"Mouse Sem Fio", "preco":100, "categoria":"Tecnologia"},
        {"id":3201, "nome":"Panela Antiaderente", "preco":120, "categoria":"Casa"},
        {"id":3202, "nome":"Toalha de Mesa", "preco":50, "categoria":"Casa"},
        {"id":3203, "nome":"Almofada", "preco":70, "categoria":"Casa"},
        {"id":3301, "nome":"Espelho Mágico (não muda nada)", "preco":150, "categoria":"Ilusão"},
        {"id":3401, "nome":"Baralho Padrão", "preco":20, "categoria":"Jogos"},
        {"id":3402, "nome":"Dados de RPG (kit com 7 peças)", "preco":50, "categoria":"Jogos"},
        {"id":3403, "nome":"UNO para jogar no patio da faculdade", "preco":100, "categoria":"Jogos"},
        {"id":3501, "nome":"Moeda de Coleção Comemorativa", "preco":300, "categoria":"Colecionáveis"},
        {"id":3502, "nome":"Caneca com autógrafo surpresa", "preco":120, "categoria":"Colecionáveis"},
        {"id":3503, "nome":"Boneco Action-Figure Clássico", "preco":200, "categoria":"Colecionáveis"},
        {"id":3601, "nome":"Brincos de Prata", "preco":100, "categoria":"Acessório"},
        {"id":3602, "nome":"Pequena Grande Bolsa de Couro", "preco":250, "categoria":"Acessório"},
        {"id":3603, "nome":"Óculos de Sol", "preco":150, "categoria":"Acessório"},
        {"id":3604, "nome":"Óculos de Chuva", "preco":150, "categoria":"Acessório"},
        {"id":3701, "nome":"Mouse Gamer RGB", "preco":120, "categoria":"Tecnologia"},
        {"id":3702, "nome":"Teclado Mecânico com Luzes", "preco":250, "categoria":"Tecnologia"},
        {"id":3703, "nome":"Monitor UltraWide 29''", "preco":1200, "categoria":"Tecnologia"},
        {"id":3704, "nome":"Fone de Ouvido Bluetooth", "preco":350, "categoria":"Tecnologia"},
        {"id":3705, "nome":"Carregador Rápido USB-C", "preco":100, "categoria":"Tecnologia"},
        {"id":3706, "nome":"Câmera de Segurança Inteligente", "preco":500, "categoria":"Tecnologia"},
        {"id":3707, "nome":"Smartwatch Fitness", "preco":700, "categoria":"Tecnologia"},
        {"id":3708, "nome":"Tablet Compacto 8''", "preco":950, "categoria":"Tecnologia"},
        {"id":3709, "nome":"Power Bank de Alta Capacidade", "preco":150, "categoria":"Tecnologia"},
        {"id":3710, "nome":"Drone com Câmera 4K", "preco":2500, "categoria":"Tecnologia"},
        {"id":3711, "nome":"Smartphone com Tela Dobrável", "preco":5000, "categoria":"Tecnologia"},
        {"id":3712, "nome":"Impressora Multifuncional", "preco":800, "categoria":"Tecnologia"},
        {"id":3713, "nome":"Placa de Vídeo RTX 4060", "preco":3000, "categoria":"Tecnologia"},
        {"id":3714, "nome":"HD Externo 2TB", "preco":500, "categoria":"Tecnologia"},
        {"id":3715, "nome":"SSD NVMe 1TB", "preco":800, "categoria":"Tecnologia"},
        {"id":3716, "nome":"Roteador Wi-Fi 6", "preco":350, "categoria":"Tecnologia"},
        {"id":3717, "nome":"Caixa de Som Bluetooth", "preco":400, "categoria":"Tecnologia"},
        {"id":3718, "nome":"Adaptador HDMI para USB-C", "preco":80, "categoria":"Tecnologia"},
        {"id":3719, "nome":"Gamepad Universal", "preco":200, "categoria":"Tecnologia"},
        {"id":3720, "nome":"Webcam Full HD com Microfone", "preco":250, "categoria":"Tecnologia"},
        {"id":3801, "nome":"Mistérios do Cosmos", "preco":80, "categoria":"Livro"},
        {"id":3802, "nome":"Guia do Programador Moderno", "preco":120, "categoria":"Livro"},
        {"id":3803, "nome":"Histórias para Inspirar", "preco":45, "categoria":"Livro"},
        {"id":3804, "nome":"Manual de Sobrevivência Urbana", "preco":70, "categoria":"Livro"},
        {"id":3805, "nome":"Ficção e Realidade", "preco":60, "categoria":"Livro"},
        {"id":3806, "nome":"Culinária Internacional para Iniciantes", "preco":85, "categoria":"Livro"},
        {"id":3807, "nome":"Biografias de Grandes Cientistas", "preco":100, "categoria":"Livro"},
        {"id":3808, "nome":"Romance nas Terras do Norte", "preco":55, "categoria":"Livro"},
        {"id":3809, "nome":"Segredos da Liderança", "preco":90, "categoria":"Livro"},
        {"id":3810, "nome":"Coleção de Contos Fantásticos", "preco":50, "categoria":"Livro"},
        {"id":3811, "nome":"História da Arte Moderna", "preco":110, "categoria":"Livro"},
        {"id":3812, "nome":"Viagens e Aventuras pelo Mundo", "preco":95, "categoria":"Livro"},
        {"id":3813, "nome":"Técnicas Avançadas de Fotografia", "preco":120, "categoria":"Livro"},
        {"id":3814, "nome":"O Universo da Matemática", "preco":75, "categoria":"Livro"},
        {"id":3815, "nome":"Segredos da Psicologia Aplicada", "preco":85, "categoria":"Livro"},
        {"id":3816, "nome":"Como Pensar como um Filósofo", "preco":90, "categoria":"Livro"},
        {"id":3817, "nome":"A História do Cinema Mundial", "preco":150, "categoria":"Livro"},
        {"id":3818, "nome":"Jogos de Estratégia: Teoria e Prática", "preco":110, "categoria":"Livro"},
        {"id":3819, "nome":"Guias para uma Vida Minimalista", "preco":65, "categoria":"Livro"},
        {"id":3820, "nome":"Enciclopédia dos Animais Extintos", "preco":140, "categoria":"Livro"},
        {"id":3721, "nome":"Cadeira Gamer Ergonômica", "preco":950, "categoria":"Tecnologia"},
        {"id":3722, "nome":"Controle Remoto Universal", "preco":120, "categoria":"Tecnologia"},
        {"id":3821, "nome":"A Ciência por Trás dos Mistérios", "preco":85, "categoria":"Livro"},
        {"id":3822, "nome":"O Guia do Entusiasta de Música Clássica", "preco":100, "categoria":"Livro"},
        {"id":3823, "nome":"Manual de Robótica para Iniciantes", "preco":150, "categoria":"Livro"}
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
    if( precoProduto <= 250 ): quantidadeMaxima = 7 # Quanto maior o valor do produto, menor é a quantidade que ele pode comprar do mesmo
    elif( precoProduto <= 500 ): quantidadeMaxima = 4
    elif( precoProduto <= 750 ): quantidadeMaxima = 3
    elif ( precoProduto <= 2000): quantidadeMaxima = 2
    else: quantidadeMaxima = 1
    quantidade = random.randint(1, quantidadeMaxima) # Gera um número de 1 a 7, que é a quantidade de produto comprada
    item_pedido = {
        "id":random.randint(0, 99999999999999), # número alto para evitar replicação de id
         "id_pedido":id,
         "id_produto":produto.get("id"), # Pega o id do pedido
         "preco_produto":precoProduto, # Pega o preco do produto
         "quantidade":quantidade, # Define a quantidade de itens
         "preco_itens":(precoProduto*quantidade) # Calcula o preco total desse item
    }
    itensPedido.append(item_pedido) # Adiciona o item pedido na lista de todos os itens pedido
    return item_pedido
    
produtos = criarProdutos()
clientes, enderecos = criarClientesEnderecos()
vendedores = criarVendedores()
pedidos = criarPedidos()
print("Base de Dados Criada!!!!!")


def criar_arquivo_csv(nome_arquivo, lista_objeto):
    with open("tabelasResultadoFaker/" + nome_arquivo, mode="w", newline="", encoding="UTF-8") as arquivo: 
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


