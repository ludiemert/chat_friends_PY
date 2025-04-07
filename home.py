# Flet
# importar o flet
import flet as ft

#criar a funcao principal para rodar a aplicacao
def main(pagina):  #costuma dar nome main para a funcao principal, Obrigatoriamente recebe pagina
  #colocar oque a funcao vai fazer

    # titulo
    titulo = ft.Text("Welcome to Chat_friends 🥰", color="purple", size=18) #ft.FERRAMENTA
    pagina.add(titulo)


    # botao inicial
    botao = ft.ElevatedButton("Start_Chat🥳", color="blue")
    pagina.add(botao)

# executar essa funcao com o flet
ft.app(main)

