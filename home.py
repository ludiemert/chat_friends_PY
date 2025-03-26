# Flet criate page

# importar o flet
import flet as ft

# cria a funcao principal para rodar o seu aplicativo
def main(pagina):
  # titulo
  titulo = ft.Text("Chat_friends")
  pagina.add(titulo)

  # botao inicial
  botao = ft.ElevatedButton("Start Chat")
  pagina.add(botao)

# executar essa funcao com o flet
ft.app(target=main) # target= em ft.app(target=main) é usado para indicar qual função será chamada para inicializar a aplicação no Flet.