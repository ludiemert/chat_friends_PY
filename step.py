# criar um sistema, anota todas as telas do projeto

# Versoes:
# 1 Trocar para Python 3.10 → Versão mais estável para o Flet.
# 2 Ambiente virtual limpo → Sem conflitos de pacotes.
# 3 Flet 0.22.0 → Versão testada e aprovada.

# Tela inicial
  # Titulo: Pag inicial
  # Botao: Start chat
    # quando clicar no botao:
    # abrir um popup/modal/alert
      #  titulo (ola bem vindo)
      # caixa de texto: escreva um texto
      # botao: entrar no chat
        # quando clicar no botao
        # sumir com o titulo
        # sumir com o botao de iniciar chat
          # carregar o chat
          # carregar o campo de enviar msg: Digite a sua msg
          # botao Enviar
            # quando clicar no botao enviar
            # enviar a msg
            # limpar a cx de msg

# Podemos usar algumas ferramentas : Flask e Django (pacote de codigos do py feitos para criar sites, sistemas e aplicativos, cria site py), kivy(cria aplicativo), tkinter (cria telas p seu prog)
# nesse projeto vamos usar o Flet => faz front e back => no py cria site, aplicativo e prog no computador.
# nele voce cria oque o usuario ve e a logica por tras do codigo = vc cria o front e o back , com o mesmo prog vc cria um site um prog de comp e um aplicavo

# vamos instalar o flet no notebook
# pip install flet

# sempre que quiser usar o flet fazer 3 passos
#  1 importar o flet
import flet as ft

# 2 - criar uma funcao principal para rodar o seu aplicativo
# def  nome_da_funcao(parametro):
#      o que essa funcao vai fazer
#      passo 1
#      passo 2
#      passo 3
#      passo 4

# def vc cria a funcao parametro que ela precisa funcionar e parametro p ela func (:) oque essa funcao vai fazer (passo 1, passo 2, passo 3 ....)
# essa funcao e para que sempre que o usuario entrar no site vai acontecer algo no site
# o usuario executa essa funcao passo a passo, uma logica de passo a passo
# dentro da main se cria toda a funcionalidade do site

#def main():
  # colocar oque essa funcao vai fazer

# 3 - executar essa funcao com o flet
# ft.app(main)  # passa a funcao principal q ele vai executar

# toda vez que for construir um projeto no Flet tem que ter essas 3 linhas
# 1 - import flet as ft
# 2 - def main():
# 3 - ft.app(main)  # passa a funcao principal q ele vai executar

# uma funcao eh um objeto no PY = tudo no py tem caracteristica e atributo
# ex: ft(obj) suas funcoes sao suas caract, qdo abre as opcoes

