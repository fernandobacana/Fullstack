import os

# criar arquivos
lista_arquivos = ['usuarios.txt', 'videos.txt', 'favoritos.txt']

for arq in lista_arquivos:

    if os.path.exists(arq) == False:
        open(arq, 'w', encoding='utf-8').close()

# videos padrao
def colocar_videos():

    with open('videos.txt', 'r', encoding='utf-8') as arquivo:
        txt = arquivo.read().strip()

    if txt == '':

        lista_videos = [
            'Minecraft Survival|Gameplay de sobrevivencia',
            'Curso Python|Curso basico',
            'Valorant Ranked|Gameplay competitiva',
            'CS Highlights|Jogadas legais',
            'Fernando Risseto|Valorant plays',
            'Pedrinho labubu|Videos engracados'
        ]

        with open('videos.txt', 'w', encoding='utf-8') as arquivo:

            for item in lista_videos:
                arquivo.write(item + '\n')

colocar_videos()

# cadastrar
def cadastro():

    nome = input('Digite seu usuario: ')
    senha = input('Digite sua senha: ')

    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == nome:

            print('\nUsuario ja existe!')
            return

    with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome}|{senha}\n')

    print('\nCadastro realizado com sucesso!')

# login
def entrar():

    nome = input('Usuario: ')
    senha = input('Senha: ')

    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == nome and dados[1] == senha:

            print('\nLogin realizado!')
            menu(nome)
            return

    print('\nUsuario ou senha incorretos!')

# buscar video
# buscar video
def procurar_video():

    pesquisa = input('Digite o nome do video: ').lower()

    encontrou = False

    with open('videos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    print('\n========== BUSCA ==========')

    for item in linhas:

        dados = item.strip().split('|')

        nome_video = dados[0]
        desc = dados[1]

        if pesquisa in nome_video.lower():

            encontrou = True

            print('\nVIDEO ENCONTRADO!')
            print(f'Nome: {nome_video}')
            print(f'Descricao: {desc}')
            print('==========================')

    if encontrou == False:

        print('\nVIDEO INEXISTENTE!')
        print('Nenhum resultado encontrado.')
        print('==========================')
# criar lista
def criar_lista(user):

    nome_lista = input('Nome da lista: ')

    with open('favoritos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{user}|{nome_lista}|vazio\n')

    print('\nLista criada!')

# ver favoritos
def ver_favoritos(user):

    with open('favoritos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    achou = False

    print('\n===== FAVORITOS =====\n')

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == user:

            achou = True

            print(f'Lista: {dados[1]}')
            print(f'Video: {dados[2]}')
            print()

    if achou == False:
        print('Nenhum favorito salvo!')

# adicionar favorito
def add_favorito(user):

    lista_nome = input('Nome da lista: ')
    video = input('Nome do video: ')

    with open('favoritos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{user}|{lista_nome}|{video}\n')

    print('\nVideo salvo nos favoritos!')

# remover favorito
def remover_video(user):

    video = input('Video para remover: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    nova = []

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == user and dados[2] == video:
            pass

        else:
            nova.append(item)

    with open('favoritos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(nova)

    print('\nVideo removido!')

# editar lista
def editar(user):

    velha = input('Nome da lista antiga: ')
    nova_lista = input('Novo nome da lista: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    nova = []

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == user and dados[1] == velha:

            linha_nova = f'{dados[0]}|{nova_lista}|{dados[2]}\n'
            nova.append(linha_nova)

        else:
            nova.append(item)

    with open('favoritos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(nova)

    print('\nLista editada!')

# excluir lista
def apagar_lista(user):

    nome_lista = input('Nome da lista: ')

    with open('favoritos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    nova = []

    for item in linhas:

        dados = item.strip().split('|')

        if dados[0] == user and dados[1] == nome_lista:
            pass

        else:
            nova.append(item)

    with open('favoritos.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(nova)

    print('\nLista apagada!')

# menu usuario
def menu(user):

    while True:

        print('\n==========================')
        print('          FEITV')
        print('==========================')
        print(f'Conta logada: {user}')
        print('==========================')
        print('1 - Buscar video')
        print('2 - Criar lista')
        print('3 - Ver favoritos')
        print('4 - Adicionar favorito')
        print('5 - Remover favorito')
        print('6 - Editar lista')
        print('7 - Apagar lista')
        print('0 - Logout')
        print('==========================')

        op = input('Escolha: ')

        if op == '1':
            procurar_video()

        elif op == '2':
            criar_lista(user)

        elif op == '3':
            ver_favoritos(user)

        elif op == '4':
            add_favorito(user)

        elif op == '5':
            remover_video(user)

        elif op == '6':
            editar(user)

        elif op == '7':
            apagar_lista(user)

        elif op == '0':

            print('\nLogout realizado!')
            break

        else:
            print('\nOpcao invalida!')

# menu principal
while True:

    print('\n======================')
    print('         FEITV')
    print('======================')
    print('1 - Cadastrar')
    print('2 - Login')
    print('0 - Fechar')
    print('======================')

    escolha = input('Escolha: ')

    if escolha == '1':
        cadastro()

    elif escolha == '2':
        entrar()

    elif escolha == '0':

        print('\nPrograma fechado!')
        break

    else:
        print('\nOpcao invalida!')