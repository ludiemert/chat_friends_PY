import flet as ft

def main(page: ft.Page):
    page.title = "Chat Funcional"
    page.window_width = 400
    page.vertical_alignment = "center"

    dlg = ft.AlertDialog(
        title=ft.Text("SUCESSO!"),
        content=ft.Text("Popup funcionando no Python 3.10"),
        actions=[ft.TextButton("OK")]
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton(
            "Clique Aqui",
            on_click=open_dlg,
            width=150,
            height=50
        )
    )

# Execute com Python 3.10
ft.app(target=main, view=ft.WEB_BROWSER)