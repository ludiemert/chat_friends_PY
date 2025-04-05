# Importar a biblioteca Flet para criar a interface gráfica
import flet as ft

# Função principal que será executada quando o aplicativo iniciar
def main(pagina: ft.Page):
    # Configurações iniciais da página
    pagina.title = "Chat_friends"  # Título da janela
    # Alinhamento dos elementos na página (centralizado)
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criar o título principal da aplicação
    titulo = ft.Text(
        "Chat_friends",
        size=40,  # Tamanho da fonte
        weight=ft.FontWeight.BOLD,  # Texto em negrito
    )

    # ========== CONFIGURAÇÃO DO POPUP ==========
    # Elementos que compõem o popup:
    titulo_popup = ft.Text("Welcome to chat")  # Título do popup
    caixa_nome = ft.TextField(label="Dig Your name...")  # Campo para digitar o nome

    # Função que será executada quando clicar no botão do popup
    def entrar_chat(evento):
        nome = caixa_nome.value  # Pega o valor digitado no campo
        if nome:  # Verifica se o nome não está vazio
            print(f"User {nome} start chat")  # Exibe mensagem no console
            popup.open = False  # Fecha o popup
            pagina.update()  # Atualiza a página

    # Botão que aparece dentro do popup
    botao_popup = ft.ElevatedButton(
        "Start_chat🥳",  # Texto do botão com emoji
        on_click=entrar_chat  # Ação ao clicar
    )

    # Configuração completa do popup (AlertDialog)
    popup = ft.AlertDialog(
        open=False,  # Começa fechado
        modal=True,  # Impede clicar fora do popup
        title=titulo_popup,  # Título configurado acima
        content=caixa_nome,  # Campo de texto
        actions=[botao_popup]  # Lista de botões (só temos 1)
    )

    # ========== BOTÃO PRINCIPAL ==========
    # Função para abrir o popup quando clicar no botão principal
    def abrir_popup(evento):
        pagina.dialog = popup  # Associa o popup à página
        popup.open = True  # Abre o popup
        pagina.update()  # Atualiza a página

    # Botão principal da aplicação
    botao = ft.ElevatedButton(
        "Start_Chat",  # Texto do botão
        on_click=abrir_popup,  # Ação ao clicar
        width=200,  # Largura
        height=80  # Altura
    )

    # ========== LAYOUT DA PÁGINA ==========
    # Organiza os elementos em uma coluna centralizada
    coluna = ft.Column(
        [titulo, botao],  # Elementos na coluna (título e botão)
        alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal
        spacing=20,  # Espaço entre elementos
    )

    # Container que envolve a coluna para melhor estilização
    container = ft.Container(
        content=coluna,  # Conteúdo do container
        padding=40,  # Espaçamento interno
        bgcolor=ft.colors.BLUE_100,  # Cor de fundo azul claro
        border_radius=20,  # Bordas arredondadas
        width=600,  # Largura fixa
    )

    # Adiciona o container à página
    pagina.add(container)

# Inicia o aplicativo no navegador web
ft.app(target=main, view=ft.WEB_BROWSER)