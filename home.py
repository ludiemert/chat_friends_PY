import flet as ft

def main(page: ft.Page):
    page.title = "Chat_friends"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Popup
    popup = ft.AlertDialog(
        modal=True,
        title=ft.Text("Welcome to chat"),
        content=ft.TextField(label="Digite seu nome"),
        actions=[ft.ElevatedButton("Start Chat 🥳")]
    )

    def open_dlg(e):
        page.dialog = popup
        popup.open = True
        page.update()

    # Botão principal
    btn = ft.ElevatedButton(
        "Start Chat",
        on_click=open_dlg,
        style=ft.ButtonStyle(
            padding=20,
            bgcolor=ft.colors.BLACK,
            color=ft.colors.WHITE
        )
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Chat_friends", size=40, weight="bold"),
                btn
            ], alignment="center"),
            bgcolor=ft.colors.BLUE_100,
            padding=40,
            border_radius=20,
            width=600
        )
    )

#ft.app(target=main) Start via app e not browser
ft.app(target=main, port=8550, view=ft.WEB_BROWSER)