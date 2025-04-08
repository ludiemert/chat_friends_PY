# Flet
# importar o flet
import flet as ft

#criar a funcao principal para rodar a aplicacao
def main(pagina):  #costuma dar nome main para a funcao principal, Obrigatoriamente recebe pagina
  #colocar oque a funcao vai fazer

    # titulo
    titulo = ft.Text("Welcome to Chat_friends 🥰", color="purple", size=18) #ft.FERRAMENTA
    pagina.add(titulo) # codig coloca esse elemento na pagina, ou colocar tudo no final da pagina

    # criar o popup, no flet o popup eh chamado de AlertDialog, precisa configurar coisas oque voce quer que aconteca dentro do popup
    titulo_poup = ft.Text("Welcome to chat") # titulo popup
    box_name_user = ft.TextField() # campo de texto que o usuario preenche
    button_start_Chat = ft.ElevatedButton("Start Chat")

    #colocar dentro do popup oque criou
    popup = ft.AlertDialog(
        title=titulo_poup,
        content=box_name_user, ) # acoes usa o actions exemp como botao, vem no plural para voce ter mais de um botao


    # botao inicial
    #funcao do botao (on_click= open_popup) a funcao vai dizer oque vai acontecer qdo o usuario clicar no botao
    def open_popup(evento): # ele obrigatoriamente recebe o evento do botao, evento de click, tem que ter o evento para nao dar erro
        print("clicou no botao") # sempre que clicar no botao sera um botao e um evento

    button_start = ft.ElevatedButton("Start_Chat🥳", color="blue", on_click=open_popup)  #acao (funcao) do botao on_click,
    pagina.add(button_start) # codig coloca esse elemento na pagina, ou colocar tudo no final da pagina

    # exemplo colocar os elementos que vai ter na pagina
    #pagina.add(titulo)
    #paginaadd(botao)


# executar essa funcao com o flet
ft.app(main, view=ft.WEB_BROWSER) #abre formato web

