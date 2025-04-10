# Flet
# Importar o flet
import flet as ft

# Criar a função principal para rodar a aplicação
def main(pagina):  # Costuma dar nome 'main' para a função principal. Obrigatoriamente recebe 'pagina'
    # Título
    titulo = ft.Text("Welcome to Chat_friends  🥰", color="purple", size=18)
    pagina.add(titulo)  # Código coloca esse elemento na página, ou colocar tudo no final da página

    # funcao completa para enviar a msg
    def send_message(evento): # uma funcao que recebe um evento
        #preencher texto campo msg e nome do user
        name_user = box_name_user.value # pega o valor do nome do usuario
        text_camp_msg = camp_send_msg.value # pega valores campo da msg
        text = ft.Text(f"{name_user} : {text_camp_msg}") #colocar valores dinamicos no PY colocar entre f{} # text = ft.Text(camp_send_msg.value) #pega o valor que esta no campo enviar msg, eh o texto que o usuario escreveu. # cria texto dinamico
        chat.controls.append(text) # adicionar um elemento no chat, controls.append() isso adiciona um item no final, sempre add item no final
        # esse codigo pode ser  ou como acima
        # text = camp_send_msg.value #pega o valor que esta no campo enviar msg, eh o texto que o usuario escreveu
        # chat.controls.append(ft.Text(text)) # adicionar um elemento no chat, controls.append() isso adiciona um item no final, sempre add item no final
        camp_send_msg.value = ""  # limpa a caixa de mensagem
        pagina.update() #sempre atualizar a pagina, e aparece a msg


    # criar campo enviar ms
    camp_send_msg = ft.TextField(label="Enter your msg .... 👍", on_submit=send_message) # on_submit=send_message => ao dar enter a msg eh enviada sem preciar precionar o enter

    #button enviar
    button_send = ft.ElevatedButton("Send  💌", on_click=send_message) # dar funcionalidade ao botao com a opcao on_click

    # no flet temos colunas e linhas de uma tabela ft.Column(uma inf em baixo da outra) e ft.Row(linha da tabela uma do lado da outra)
    line_send = ft.Row([camp_send_msg, button_send]) # linha uma inf do lado da outra

    # criar a coluna de chat
    chat = ft.Column() # tem que ser coluna porque eh uma conversa em baixo da outra



    # Criar a função para on_click="start_chat"
    def start_chat(evento):  # Função que executa algo
        popup.open = False  # Fechar o popup
        pagina.remove(titulo)  # Sumir com o título
        pagina.remove(button_start)  # Sumir com o botão iniciar o chat

        pagina.add(chat)   # Carregar o chat
        # Carregar o campo de enviar mensagem e Carregar o botão enviar
        pagina.add(line_send)  # adicionar elemento na tela

        # aparecer no chat a msg "Name....entrou no chat"
        name_user = box_name_user.value
        text_msg = ft.Text( f"{name_user} start chat 🧐" )
        chat.controls.append(text_msg) # add text no chat sempre que user entrar no chat

        pagina.update()  # Sempre que fizer algo visual na tela, sempre colocar esse comando

    # Criar o popup (No Flet o popup é chamado de AlertDialog, precisa configurar o que você quer que aconteça dentro do popup)
    titulo_poup = ft.Text("Welcome to chat  🤩")  # Título do popup
    box_name_user = ft.TextField(label="Enter your name....  ✒")  # Campo de texto que o usuário preenche, 'label' é uma orientação para o usuário
    button_start_Chat = ft.ElevatedButton("Start Chat", on_click=start_chat)

    # Colocar dentro do popup o que você criou
    popup = ft.AlertDialog(
        title=titulo_poup,
        content=box_name_user,
        actions=[button_start_Chat]  # Ações usa o 'actions', exemplo como botão, vem no plural para você ter mais de um botão
    )

    # Função do botão (on_click=open_popup) a função vai dizer o que vai acontecer quando o usuário clicar no botão
    def open_popup(evento):  # Ele obrigatoriamente recebe o evento do botão, evento de clique, tem que ter o evento para não dar erro
        pagina.dialog = popup  # Colocar elementos de popup na tela, aparecer na frente da tela, caixa de diálogo
        popup.open = True  # Abrir o popup, exibir o popup. A nossa página só pode ter um popup por vez
        pagina.update()  # Sempre que você add alguma coisa na sua página tem que dar 'update' nela, sem apertar F5 para atualizar a página
        print("Clicou no botão")  # Sempre que clicar no botão será um botão e um evento

    # Botão inicial
    button_start = ft.ElevatedButton("Start_Chat🥳", color="blue", on_click=open_popup)  # Ação (função) do botão on_click
    pagina.add(button_start)  # Código coloca esse elemento na página, ou colocar tudo no final da página

# Executar essa função com o Flet
ft.app(main, view=ft.WEB_BROWSER)  # Abre o formato web

# toda funcao que um botao executa ela tem que existir antes de voce criar o botao
# sempre cria a funcao depois cria o botao
