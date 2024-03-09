# Title: Rickzap
# Button of start chatting
    # Clicked on the button
    # open up the popup
    # Title: Welcome to Rickzap
    # field: Write your name
    # button: Entry in the chat
# chat
    # under the chat
    # Write your message field
    # Button to send message

# Título: Rickzap
# Botão de iniciar chat
    # clicou no botão
    # abriu um pop up
        # Título: Bem vindo ao Rickzap
        # campo: escreva seu nome no chat
        # botão: entrar no chat
# chat
    # embaixo do chat
        # campo de digite a sua mensagem
        # botão de enviar a mensagem

import flet as ft

# Create the principal/main function 
# Criar a função principal/main
def main(pagina):
    
    # Create the aplicattion's name
    # Criando o nome do aplicativo
    nome_aplicativo = ft.Text('RICKZAP')
    
    
    # Create the message tunnel, for every user stay connected
    # Criando o túnel de mensagens, para todos os usuários ficarem conectados
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        
        
    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f'{nome_usuario.value}: {campo_mensagem.value}')
        # clean the message field
        # limpe o campo mensagem
        campo_mensagem.value = ''
        pagina.update()
    
    # Creating the chat
    # Criando o chat
    chat = ft.Column()
    
    # Creating the message field
    # Criando o campo de mensagem
    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    # Criando o botão de enviar a mensagem
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem) 
    # Juntando os 2 em uma linha só
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    
    
    # Creating the function of entrying the chat
    # Criando a função de entrar no chat
    def entrar_chat(evento):
        # Close the popup
        # Fechar o popup
        popup.open = False
        # remove the initiate chat button
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Adding the chat
        # adicionando o chat
        pagina.add(chat)
        # Creating the entry's text
        # criando o texto de entrada
        # putting the send_all, for show every users who entry the chat
        # colocando o send_all, para mostrar para todos os usuários quem entrou no chat
        pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')
        # write your message and send it field
        # campo de digite a sua mensagem e o de enviar
        pagina.add(linha_enviar) # A linha_enviar já tem o campo_mensagem e o botao_enviar embutidos juntos em 1 só linha
        pagina.update()
    
    # Creating the funcion of opening the popup window
    # Criando a função de abrir o popup
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    # Creating the entry at the chat button (popup)
    # Criando o botão de entrar no chat (popup)
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    
    # WHEN USER CLICK ON THE BUTTON TO OPEN THE CHAT
    # QUANDO O USUÁRIO CLICAR NO BOTÃO DE ABRIR O CHAT
    # Creating the popup's title
    # Criando o título do popup
    titulo_popup = ft.Text('Bem vindo ao Rickzap')
    
    # Creating the text box for the user write his username when the popup is opened
    # Criando a caixa de texto para o usuário digitar o nome dele quando o popup se abrir
    nome_usuario = ft.TextField(label='Escreva seu nome no chat') # Label é a caixa de texto que tem uma animaçãozinha toda vez que o usuário clicar na caixa de texto
    # Defining the chat's popup
    # Definindo o popup do chat
    popup = ft.AlertDialog(
    open=False, # Não precisa adicionar isso, mas eu adiciono para garantir que não vai abrir um popup do nada
    modal=True, 
    title=titulo_popup, 
    content=nome_usuario, 
    actions=[botao_entrar] # Independente se é só 1 botão, por padrão, o framework pede para ser uma lista de botões, então colocamos em []
    )
        
    # Initiate the chat's button
    # Botão de Iniciar o Chat
    ''' O abrir_popup ele não tem () porque se ele tivesse, a função se executaria imediatamente quando o programa fosse executado, eu não quero isso, eu quero que 
    o popup seja exibido quando o usuário clicar no botão de iniciar chat, então é sem parêntesis'''
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    
    # Adding the page's components
    # Adicionando componentes na página
    pagina.add(nome_aplicativo) # Adiciona o texto na página
    pagina.add(botao_iniciar) # Adiciona o botão iniciar
    
    # Creating the app that calls the main function
ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a função principal