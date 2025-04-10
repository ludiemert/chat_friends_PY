# Chat_friends 🥰

Welcome to **Chat_friends**, a simple chat application built with **Flet**! This project allows users to start a chat and send messages to each other in real time. The application is easy to use and can be run in your web browser.

## Features

- **Centralized Interface**: The first page is beautifully centered with a welcoming message.
- **Real-time Chat**: Users can send messages in real time using the pubsub system.
- **User Name Input**: On the first page, users are prompted to enter their name before starting the chat.
- **Send Messages**: Once the chat is started, users can send messages, and they will appear in real time for all users.
  
## Screenshots

Here are some images showing the layout of the application:

________________________________________

<h4 align="center">Chat_friends 🥰 🚀</h4>

<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/1-Page_start_APP.png" style="width: 90%;" alt="01_1_codg de treino_com as variaveis">
                <p style="margin-top: 5px;">Page_start_APP</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/10 - tela_popup_event.bmp" style="width: 90%;" alt="01_codg de treino_x_y">
                <p style="margin-top: 5px;">Tela_popup_event</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>


________________________________________

<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/11 - button_line.bmp" style="width: 90%;" alt="X e Y">
                <p style="margin-top: 5px;">Button_line</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/12 - controls.append_text.bmp" style="width: 90%;" alt="x_y treino e teste">
                <p style="margin-top: 5px;">Controls.append_text</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>


________________________________________


<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/13 - msg and name user.bmp" style="width: 90%;" alt="01_1_codg de treino_com as variaveis">
                <p style="margin-top: 5px;">Msg and name user</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/14 - msg_user_start_chat.bmp" style="width: 90%;" alt="01_codg de treino_x_y">
                <p style="margin-top: 5px;">Msg_user_start_chat</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>

  ________________________________________


<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img/15 - tunnel_conumication.bmp" style="width: 90%;" alt="X e Y">
                <p style="margin-top: 5px;">Tunnel_conumication</p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img/9 - tela_popup.bmp" style="width: 90%;" alt="x_y treino e teste">
                <p style="margin-top: 5px;">Tela_popup</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>



________________________________________

## Code Explanation

Here is a brief breakdown of the core parts of the code:

### 1. **Main Page Layout**

The first page is centered using the following code:

```python
pagina.vertical_alignment = "center"
pagina.horizontal_alignment = "center"
The Text widget displays the title "Welcome to Chat_friends 🥰".


```

________________________________________

### 2. Popup for User Name Input
When the user clicks the "Start Chat" button, a popup appears, prompting them to enter their name:

```python
popup = ft.AlertDialog(
    title=ft.Text("Welcome to chat 🤩"),
    content=ft.TextField(label="Enter your name....  ✒"),
    actions=[ft.ElevatedButton("Start Chat", on_click=start_chat)]
)
```
________________________________________

### 3. Starting the Chat
Once the user enters their name, they can start the chat, which changes the layout and adds the message controls:

```python

def start_chat(evento):
    popup.open = False  # Close the popup
    pagina.controls.clear()  # Clear initial screen
    pagina.add(chat)  # Add chat to page
    pagina.add(line_send)  # Add message input line
```
________________________________________

### 4. Sending Messages
When the user sends a message, it will be broadcast to all users in the chat using the pubsub system:

```python

def send_message(evento):
    name_user = box_name_user.value
    text_camp_msg = camp_send_msg.value
    msg = f"{name_user} : {text_camp_msg}"
    pagina.pubsub.send_all(msg)  # Send the message to all users
```
________________________________________

### 5. Container for the First Screen
To center the first screen elements (title and button), we use a Container:

```python
container_inicial = ft.Container(
    content=ft.Column(
        controls=[titulo, button_start],
        alignment="center",  # Vertical alignment
        horizontal_alignment="center"  # Horizontal alignment
    ),
    alignment=ft.alignment.center,
    expand=True  # Expand the container to fill the screen
)
```
________________________________________

## Getting Started
To run this project locally, follow these steps:

________________________________________
## Clone the repository to your local machine:

```python
git clone [https://github.com/your-username/chat_friends.git](https://github.com/ludiemert/chat_friends_PY)
```
________________________________________

## Install the necessary dependencies:

```python
pip install flet
```

________________________________________
## Run the application:

```python
python app.py
```
________________________________________
## Open your browser and visit the URL shown in the terminal.

### Technologies Used
Flet: A framework for building interactive web apps in Python.

________________________________________
####  Portugues: 

Claro! Aqui está o Markdown em português para o seu repositório no GitHub:

markdown
Copiar
Editar
# Chat_friends 🥰

Bem-vindo ao **Chat_friends**, um aplicativo de chat simples criado com **Flet**! Este projeto permite que os usuários iniciem um chat e enviem mensagens em tempo real. A aplicação é fácil de usar e pode ser executada diretamente no seu navegador.

## Funcionalidades

- **Interface Centralizada**: A primeira página é centralizada com uma mensagem de boas-vindas.
- **Chat em Tempo Real**: Os usuários podem enviar mensagens em tempo real utilizando o sistema pubsub.
- **Entrada de Nome de Usuário**: Na primeira tela, os usuários são solicitados a inserir seu nome antes de iniciar o chat.
- **Envio de Mensagens**: Após iniciar o chat, os usuários podem enviar mensagens, que aparecerão em tempo real para todos os usuários.

## Explicação do Código

#### 1. **Layout da Página Principal**

A primeira página é centralizada utilizando o seguinte código:

```python
pagina.vertical_alignment = "center"
pagina.horizontal_alignment = "center"
O widget Text exibe o título "Welcome to Chat_friends 🥰".
```

#### 2. Popup para Inserir o Nome do Usuário
Quando o usuário clica no botão "Start Chat", um popup aparece pedindo para inserir seu nome:

```python
popup = ft.AlertDialog(
    title=ft.Text("Welcome to chat 🤩"),
    content=ft.TextField(label="Enter your name....  ✒"),
    actions=[ft.ElevatedButton("Start Chat", on_click=start_chat)]
)
```

#### 3. Iniciando o Chat
Depois que o usuário insere seu nome, ele pode começar o chat, o que muda o layout e adiciona os controles de mensagem:

```python
def start_chat(evento):
    popup.open = False  # Fecha o popup
    pagina.controls.clear()  # Limpa a tela inicial
    pagina.add(chat)  # Adiciona o chat à página
    pagina.add(line_send)  # Adiciona a linha de entrada de mensagem
```

#### 4. Enviando Mensagens
Quando o usuário envia uma mensagem, ela será transmitida para todos os usuários do chat usando o sistema pubsub:

```python
def send_message(evento):
    name_user = box_name_user.value
    text_camp_msg = camp_send_msg.value
    msg = f"{name_user} : {text_camp_msg}"
    pagina.pubsub.send_all(msg)  # Envia a mensagem para todos os usuários
```

#### 5. Container para a Primeira Tela
Para centralizar os elementos da primeira tela (título e botão), utilizamos um Container:

```python
container_inicial = ft.Container(
    content=ft.Column(
        controls=[titulo, button_start],
        alignment="center",  # Alinhamento vertical
        horizontal_alignment="center"  # Alinhamento horizontal
    ),
    alignment=ft.alignment.center,
    expand=True  # Expande o container para preencher a tela
)
```

#### 6. Estrutura do Layout
A estrutura do layout é gerenciada com pagina.add(container_inicial) para a primeira tela e com a adição do chat e linha de envio na segunda tela.

#### Como Começar
Para rodar este projeto localmente, siga estes passos:

#### Clone o repositório para sua máquina local:

```python
git clone [https://github.com/seu-usuario/chat_friends.git](https://github.com/ludiemert/chat_friends_PY)
```

#### Instale as dependências necessárias:

```python
pip install flet
```

Execute o aplicativo:

```python
python app.py
```

#### Abra seu navegador e visite a URL que será mostrada no terminal.

#### Tecnologias Usadas
Flet: Framework para construir aplicativos interativos em Python.

Python: Linguagem principal utilizada para desenvolver o app.

________________________________________
### Python: The main programming language used to build the app.

#### 🤝 Contributing
If you would like to contribute to this project, feel free to open an issue or submit a pull request! 🚀
________________________________________
#### 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
👩💻 Developed with 💙 by [[LuDiemert](https://www.linkedin.com/in/lucianadiemert/)]

________________________________________
- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

________________________________________
## 🌐 **Contact**
<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

---
Developed with ❤ by [ludiemert](https://github.com/ludiemert).

