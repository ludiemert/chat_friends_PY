import flet as ft

def main(pagina):
    # ✅ Alinha vertical e horizontalmente o conteúdo da primeira tela ao centro
    pagina.vertical_alignment = "center"
    pagina.horizontal_alignment = "center"

    # Título da página inicial
    titulo = ft.Text("Welcome to Chat_friends  🥰", color="purple", size=18)

    # Função que será chamada sempre que uma nova mensagem for enviada no chat (via pubsub)
    def send_msg_tunnel(msg):
        text = ft.Text(msg)
        chat.controls.append(text)
        pagina.update()

    # Inscreve a função acima ao sistema de mensagens pubsub
    pagina.pubsub.subscribe(send_msg_tunnel)

    # Enviar mensagem no chat
    def send_message(evento):
        name_user = box_name_user.value
        text_camp_msg = camp_send_msg.value
        msg = f"{name_user} : {text_camp_msg}"
        pagina.pubsub.send_all(msg)  # Envia a mensagem para todos
        camp_send_msg.value = ""     # Limpa campo de mensagem após envio
        pagina.update()

    # Campo de texto para digitar mensagem
    camp_send_msg = ft.TextField(label="Enter your msg .... 👍", on_submit=send_message)
    # Botão de envio
    button_send = ft.ElevatedButton("Send  💌", on_click=send_message)
    # Linha com input + botão
    line_send = ft.Row([camp_send_msg, button_send])
    # Coluna onde as mensagens aparecerão
    chat = ft.Column()

    # Função chamada ao iniciar o chat
    def start_chat(evento):
        popup.open = False  # Fecha o popup
        pagina.controls.clear()  # Limpa os elementos da primeira tela

        # ✅ Remove centralização para a tela do chat (segunda tela)
        pagina.vertical_alignment = None
        pagina.horizontal_alignment = None

        # Adiciona elementos do chat
        pagina.add(chat)
        pagina.add(line_send)

        # Envia mensagem inicial informando entrada no chat
        name_user = box_name_user.value
        msg = f"{name_user} start chat 🧐"
        pagina.pubsub.send_all(msg)

        pagina.update()

    # Elementos do popup para digitar nome
    titulo_poup = ft.Text("Welcome to chat  🤩")
    box_name_user = ft.TextField(label="Enter your name....  ✒")
    button_start_Chat = ft.ElevatedButton("Start Chat", on_click=start_chat)

    # Janela popup de boas-vindas
    popup = ft.AlertDialog(
        title=titulo_poup,
        content=box_name_user,
        actions=[button_start_Chat]
    )

    # Função para abrir o popup
    def open_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão da primeira tela
    button_start = ft.ElevatedButton("Start_Chat🥳", color="blue", on_click=open_popup)

    # ✅ Container centralizado da primeira tela com título e botão
    container_inicial = ft.Container(
        content=ft.Column(
            controls=[titulo, button_start],
            alignment="center",  # Centraliza verticalmente
            horizontal_alignment="center"  # Centraliza horizontalmente
        ),
        alignment=ft.alignment.center,
        expand=True  # Ocupa toda a tela
    )

    # Adiciona o container à página
    pagina.add(container_inicial)

# Roda o app no navegador
ft.app(main, view=ft.WEB_BROWSER)
