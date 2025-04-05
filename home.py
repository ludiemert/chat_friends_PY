import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Chat_friends"
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text(
        "Chat_friends",
        size=40,
        weight=ft.FontWeight.BOLD,
    )

    # Elementos do popup
    titulo_popup = ft.Text("Welcome to chat")
    caixa_nome = ft.TextField(label="Dig Your name...")

    def entrar_chat(evento):
        nome = caixa_nome.value
        if nome:
            print(f"User {nome} start chat")
            popup.open = False
            pagina.update()

    # Botão dentro do popup
    botao_popup = ft.ElevatedButton("Start_chat🥳", on_click=entrar_chat)

    # Configuração do popup
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão inicial
    botao = ft.ElevatedButton(
        "Start_Chat",
        on_click=abrir_popup,
        width=200,
        height=80
    )

    coluna = ft.Column(
        [titulo, botao],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    container = ft.Container(
        content=coluna,
        padding=40,
        bgcolor=ft.colors.BLUE_100,
        border_radius=20,
        width=600,
    )

    pagina.add(container)

ft.app(target=main, view=ft.WEB_BROWSER)