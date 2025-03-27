# Importar o Flet
import flet as ft

# Criar a função principal para rodar o aplicativo
def main(pagina: ft.Page):
    # Definir o título da janela
    pagina.title = "Chat_friends"

    # Definir alinhamento da página (centro)
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Definir o texto do título com tamanho maior e negrito
    titulo = ft.Text(
        "Chat_friends",
        size=40,
        weight=ft.FontWeight.BOLD,
    )

    # Botão inicial (corrigido)
    botao = ft.ElevatedButton(
        "StartChat",
        style=ft.ButtonStyle(
            bgcolor="black",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color="white",
                size=40,
            ),
        ),
    )

    # Criar um layout de coluna e adicionar os elementos
    coluna = ft.Column(
        [titulo, botao],  # Adiciona os componentes na coluna
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
        spacing=20,  # Espaçamento entre os elementos
    )

    # Criar container colorido
    container = ft.Container(
        content=coluna,
        padding=40, # espaco interno
        bgcolor=ft.colors.BLUE_100, # or de fundo azul claro
        border_radius=20, #bordar arredondadas
        width=600, # largura container

    )


    # Adicionar o layout à página
    pagina.add(container)

# Executar a aplicação no navegador
ft.app(target=main, view=ft.WEB_BROWSER)