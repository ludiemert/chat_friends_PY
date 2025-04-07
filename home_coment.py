# Importar a biblioteca Flet para criar a interface gráfica
import flet as ft

# Função principal que será executada quando o aplicativo iniciar
def main(pagina: ft.Page):
    # Configurações iniciais da página
    pagina.title = "Chat_friends"  # Define o título da página (janela)
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinha os elementos horizontalmente ao centro
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinha os elementos verticalmente ao centro

    # Criar o título principal da aplicação
    titulo = ft.Text(
        "Chat_friends",  # Texto do título
        size=40,  # Tamanho da fonte
        weight=ft.FontWeight.BOLD,  # Define o peso da fonte como negrito
    )

    # Campo de texto para o usuário digitar seu nome
    caixa_nome = ft.TextField(label="Digite seu nome")

    # Texto exibido no popup de boas-vindas
    titulo_popup = ft.Text("Welcome to chat")

    # Botão que será exibido no popup para iniciar o chat
    botao = ft.ElevatedButton(text="Start_Chat")

    # ========== FUNÇÃO ENTRAR CHAT ==========
    # Função chamada quando o botão do popup é clicado
    def entrar_chat(evento):
        nome = caixa_nome.value  # Obtém o valor digitado no campo de texto (nome)
        if nome:  # Verifica se o nome foi preenchido
            print(f"User {nome} start chat")  # Exibe o nome do usuário no console
            popup.open = False  # Fecha o popup
            pagina.update()  # Atualiza a página

            # Limpa toda a tela (removendo os componentes atuais)
            pagina.controls.clear()
            pagina.update()

            # Novo título de boas-vindas no chat
            titulo_chat = ft.Text(f"Olá, {nome}! Bem-vindo ao Chat 🎉", size=24)

            # Campo de texto para digitar mensagens no chat
            campo_mensagem = ft.TextField(
                label="Digite sua mensagem",
                width=400
            )

            # Função para enviar a mensagem
            def enviar_mensagem(evento):
                print(f"{nome}: {campo_mensagem.value}")  # Exibe a mensagem no console
                campo_mensagem.value = ""  # Limpa o campo de mensagem
                pagina.update()  # Atualiza a página

            # Botão para enviar a mensagem
            botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

            # Linha que contém o campo de mensagem e o botão de enviar
            linha_envio = ft.Row(
                [campo_mensagem, botao_enviar],
                alignment=ft.MainAxisAlignment.CENTER  # Alinha os elementos ao centro
            )

            # Adiciona os componentes do chat na nova tela
            pagina.add(
                ft.Column(
                    [titulo_chat, linha_envio],  # Adiciona título e linha de envio de mensagem
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinha verticalmente ao centro
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha horizontalmente ao centro
                    spacing=20,  # Espaçamento entre os elementos
                )
            )
            pagina.update()  # Atualiza a página para exibir os novos elementos

    # Botão dentro do popup que aciona a função 'entrar_chat'
    botao_popup = ft.ElevatedButton("Start_chat🥳", on_click=entrar_chat)

    # Configuração do popup (diálogo de alerta)
    popup = ft.AlertDialog(
        open=False,  # Inicialmente o popup está fechado
        modal=True,  # Modal impede interação com o fundo enquanto o popup está aberto
        title=titulo_popup,  # Título do popup
        content=caixa_nome,  # Conteúdo do popup, que é o campo de nome
        actions=[botao_popup]  # Botões do popup
    )

    # Função para abrir o popup quando o botão principal da página for clicado
    def abrir_popup(evento):
        pagina.dialog = popup  # Associa o popup à página
        popup.open = True  # Abre o popup
        pagina.update()  # Atualiza a página

    # Botão principal da tela inicial
    botao = ft.ElevatedButton(
        "Start_Chat",  # Texto do botão
        on_click=abrir_popup,  # Função chamada ao clicar no botão
        width=200,  # Largura do botão
        height=80  # Altura do botão
    )

    # Layout da tela inicial
    coluna = ft.Column(
        [titulo, botao],  # Adiciona o título e o botão na coluna
        alignment=ft.MainAxisAlignment.CENTER,  # Alinha verticalmente ao centro
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha horizontalmente ao centro
        spacing=20,  # Espaçamento entre os elementos
    )

    # Container que envolve a coluna para melhor estilização
    container = ft.Container(
        content=coluna,  # Conteúdo do container (a coluna)
        padding=40,  # Espaçamento interno
        bgcolor=ft.colors.BLUE_100,  # Cor de fundo azul claro
        border_radius=20,  # Bordas arredondadas
        width=600,  # Largura do container
    )

    # Adiciona o container à página
    pagina.add(container)

# Inicia o aplicativo no navegador web
ft.app(target=main, view=ft.WEB_BROWSER)  # Executa a aplicação no navegador
