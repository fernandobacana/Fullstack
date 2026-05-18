import os

# arquivos que armazenam os dados do cod
arquivos = ['usuarios.txt', 'videos.txt', 'favoritos.txt', 'likes.txt']

for arq in arquivos:
    if not os.path.exists(arq):
        open(arq, 'w', encoding='utf-8').close()

# Lista dos videos 
def colocar_videos():

    with open('videos.txt', 'r', encoding='utf-8') as f:
        txt = f.read().strip()

    if txt == '':
        videos = [
            'Minecraft Survival|Gameplay de sobrevivencia',
            'Aula de python | Aprendendo a fazer a feitv',
            'Valorant Ranked|Gameplay competitiva',
            'CS Highlights|Jogadas legais',
            'Fernando Risseto|Valorant plays',
            'Pedrinho labubu|Videos engracados',
            'GTA RP|Momento hilario',
            'Free Fire|But calça angelical',
            'Roblox|Obby divertido',
            'Victor Varela |Pentakill no cs insano',
            'Rocket League|Jogos insanos',
            'Among Us|Trollagem do yuri 22',
            'FIFA 24| Jogo antigo ainda é podre?',
            'Rainbow Six Siege|Clutch 1v5',
            'Overwatch 2|Highlights',
            'Fortnite|Vitoria real',
            'Fxz não choraxx |Campeonato intenso',
            'Terraria|Modo aventura',
            'The Sims 4|Construindo mansao',
            'Mc Ryan foi preso?|Voadora fatal',
            'God of War|Batalha com Baldur',
            'Spider-Man 2|Filme peter jordan',
            'Elden Ring|Bosses difíceis',
            'Cyberpunk 2077|Missões insanas',
            'Red Dead Redemption 2|Caçada no oeste'
        ]

        with open('videos.txt', 'w', encoding='utf-8') as f:
            for v in videos:
                f.write(v + '\n')

colocar_videos()

# Parte das funções , cadastro login buscar os videos etc
def cadastro():
    nome = input('Usuario: ')
    senha = input('Senha: ')

    with open('usuarios.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    for l in linhas:
        dados = l.strip().split('|')
        if dados[0] == nome:
            print('\nEsse usuario ja existe!')
            return

    with open('usuarios.txt', 'a', encoding='utf-8') as f:
        f.write(f'{nome}|{senha}\n')

    print('\nCadastro feito!')

def login():
    nome = input('Usuario: ')
    senha = input('Senha: ')

    with open('usuarios.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    for l in linhas:
        dados = l.strip().split('|')
        if dados[0] == nome and dados[1] == senha:
            print('\nLogin realizado!')
            menu_usuario(nome)
            return

    print('\nUsuario ou senha incorretos!')

def carregar_likes():
    likes = {}
    with open('likes.txt', 'r', encoding='utf-8') as f:
        for l in f.readlines():
            nome, qtd = l.strip().split('|')
            likes[nome] = int(qtd)
    return likes

def salvar_likes(likes):
    with open('likes.txt', 'w', encoding='utf-8') as f:
        for nome in likes:
            f.write(f'{nome}|{likes[nome]}\n')

def curtir_video():
    nome = input('Nome do video: ')

    likes = carregar_likes()

    if nome not in likes:
        likes[nome] = 0

    likes[nome] += 1

    salvar_likes(likes)

    print(f'\nVoce curtiu o video "{nome}"! Total: {likes[nome]}')


def descurtir_video():
    nome = input('Nome do video: ')

    likes = carregar_likes()

    if nome not in likes:
        likes[nome] = 0

    if likes[nome] > 0:
        likes[nome] -= 1

    salvar_likes(likes)

    print(f'\nVoce removeu um like de "{nome}". Agora o video tem : {likes[nome]}')

def buscar_video():
    termo = input('Nome do video: ').lower()
    achou = False

    with open('videos.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    print('\n----- RESULTADOS -----')

    for l in linhas:
        nome, desc = l.strip().split('|')

        if termo in nome.lower():
            achou = True
            print(f'\nVIDEO ENCONTRADO ({nome})')
            print(f'Descricao: {desc}')

    if not achou:
        print('\nNenhum video encontrado!')

def criar_lista(usuario):
    nome_lista = input('Nome da lista: ')
    with open('favoritos.txt', 'a', encoding='utf-8') as f:
        f.write(f'{usuario}|{nome_lista}|vazio\n')
    print('\nLista criada!')

def ver_favoritos(usuario):

    with open('favoritos.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    achou = False

    print('\n----- FAVORITOS -----')
    for l in linhas:
        user, lista, video = l.strip().split('|')
        if user == usuario:
            achou = True
            print(f'Lista: {lista} | Video: {video}')

    if not achou:
        print('Nenhum favorito salvo!')

def adicionar_favorito(usuario):
    lista = input('Nome da lista: ')
    video = input('Video: ')
    with open('favoritos.txt', 'a', encoding='utf-8') as f:
        f.write(f'{usuario}|{lista}|{video}\n')
    print('\nVideo adicionado!')

def remover_favorito(usuario):
    video = input('Video para remover: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    novo = []
    for l in linhas:
        dados = l.strip().split('|')
        if not (dados[0] == usuario and dados[2] == video):
            novo.append(l)

    with open('favoritos.txt', 'w', encoding='utf-8') as f:
        f.writelines(novo)

    print('\nVideo removido!')

def editar_lista(usuario):
    antiga = input('Nome da lista antiga: ')
    nova = input('Novo nome: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    novo = []
    for l in linhas:
        dados = l.strip().split('|')
        if dados[0] == usuario and dados[1] == antiga:
            novo.append(f'{usuario}|{nova}|{dados[2]}\n')
        else:
            novo.append(l)

    with open('favoritos.txt', 'w', encoding='utf-8') as f:
        f.writelines(novo)

    print('\nLista editada!')


def apagar_lista(usuario):
    nome = input('Nome da lista: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    novo = []
    for l in linhas:
        dados = l.strip().split('|')
        if not (dados[0] == usuario and dados[1] == nome):
            novo.append(l)

    with open('favoritos.txt', 'w', encoding='utf-8') as f:
        f.writelines(novo)

    print('\nLista apagada!')

# 2 menu 
def menu_usuario(usuario):

    while True:
        print(f'''
------------------
      FEITV
------------------
Logado como: {usuario}
1 - Buscar video
2 - Criar lista
3 - Ver favoritos
4 - Adicionar favorito
5 - Remover favorito
6 - Editar lista
7 - Apagar lista
8 - Curtir video
9 - Descurtir video
0 - Logout
------------------
''')

# IF da escolha ( segundo menu )

        opcao = input('Escolha: ')

        if opcao == '1': buscar_video()
        elif opcao == '2': criar_lista(usuario)
        elif opcao == '3': ver_favoritos(usuario)
        elif opcao == '4': adicionar_favorito(usuario)
        elif opcao == '5': remover_favorito(usuario)
        elif opcao == '6': editar_lista(usuario)
        elif opcao == '7': apagar_lista(usuario)
        elif opcao == '8': curtir_video()
        elif opcao == '9': descurtir_video()
        elif opcao == '0':
            print('\nLogout feito!')
            break
        else:
            print('\nOpcao invalida!')

# Primeiro menu do cod
while True:
    print('''
--------------------
      FEITV
--------------------
1 - Cadastrar
2 - Login
0 - Sair
--------------------
''')

    esc = input('Escolha: ')

    if esc == '1': cadastro()
    elif esc == '2': login()
    elif esc == '0':
        print('\nPrograma encerrado!')
        break
    else:
        print('\nOpcao invalida!')
