# EN: Importing the frameworks
# BR: Importando as bibliotecas
import pyautogui
import time
import pandas

# EN: Defining the pause of every command in pyautogui
# BR: Definindo a pausa de cada comando do pyautogui
pyautogui.PAUSE = 0.5

# Step 1: Entying on the company's website
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Open the navigator
# abrir o navegador
pyautogui.press('win')
# My navigator it's Brave, if your's be diferent, you should switch for 'Chrome' or something 
# Meu navegador é o Brave, se for outro, aconselho mudar para "Chrome", ou algo do tipo
pyautogui.write('Brave')
pyautogui.press('enter')

# Entry in the site
# Entrar no site
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1.5)

# Step 2: Login
# Passo 2: Fazer login
# Select the email's place
# Selecionar o campo de email
pyautogui.click(x=742, y=345)
pyautogui.write('qualqueremail@gmail.com')
# Write the password
# Escrever a senha
pyautogui.press('tab')
pyautogui.write('Qualquersenha123')
# Click on the button of the login
# Clicar no botão de logar
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1.5)

# Step 3: Import the database
# Passo 3: Importar a base de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Step 4: Register one product
# Passo 4: Cadastrar um produto
# For every line in my schedule
# Para cada linha da minha tabela
for linha in tabela.index:
    # Click on the 1st camp
    # Clicar no 1° campo
    pyautogui.click(x=737, y=245)


    # Code of the product
    # Código do produto
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    # Brand of the product
    # Marca do produto
    
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # Type of product
    # Tipo do produto
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # Category of product
    # Categoria do produto
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # Price
    # Preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # Cost
    # Custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # Obs
    obs = (tabela.loc[linha, 'obs'])
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    # Go
    # Enviar
    pyautogui.press('enter')
