from tkinter import *
import random

class DiceRoller:
    def __init__(self, master):
        # It defines the background color to black
        # Define a cor de fundo para preto
        master.configure(bg="black")

        # Variable to store the number of dice to roll
        # Variável para armazenar o número de dados a serem rolados
        self.num_dice = IntVar()
        self.num_dice.set(1)  # default value is 1  # Valor padrão é 1

        # Creates the main frame
        # Cria o frame principal
        self.frame = Frame(master, bg="black")
        self.frame.pack(pady=20)

        # Creates the label to display the title
        # Cria o rótulo para exibir o título
        self.title_label = Label(self.frame, text="Rolador de Dados", font=("Helvetica", 30, "bold"), fg="white", bg="black")
        self.title_label.pack()

        # Creates the frame to display the dice
        # Cria o frame para exibir os dados
        self.dice_frame = Frame(self.frame, bg="black")
        self.dice_frame.pack(pady=20, expand=True, fill=BOTH)

        # Creates the labels to display the dice
        # Cria as labels para exibir os dados
        self.dice_labels = []
        for _ in range(10):
            label = Label(self.dice_frame, font=("Helvetica", 150), fg="white", bg="black")
            label.pack(side=LEFT, padx=20, fill=BOTH, expand=True)
            self.dice_labels.append(label)

        # Creates the frame for the menu and the button
        # Cria o frame para o menu de seleção e o botão
        self.button_frame = Frame(self.frame, bg="black")
        self.button_frame.pack()

        # Creates the label for the selection menu
        # Cria o rótulo para o menu de seleção
        self.num_dice_label = Label(self.button_frame, text="Quantos dados girar?", font=("Helvetica", 18), fg="white", bg="black")
        self.num_dice_label.pack(side=LEFT, padx=10)

        # Creates the menu for selecting the number of dice to roll
        # Cria o menu para selecionar o número de dados a serem rolados
        self.num_dice_menu = OptionMenu(self.button_frame, self.num_dice, *range(1, 11))
        self.num_dice_menu.config(font=("Helvetica", 18), bg="white", fg="black")
        self.num_dice_menu.pack(side=LEFT, padx=10)

        # Creates the button to roll the dice
        # Cria o botão para rolar os dados
        self.button = Button(self.button_frame, text="Rolar dados", font=("Helvetica", 18, "bold"), command=self.roll, bg="white", fg="black", padx=20, pady=10)
        self.button.pack(side=LEFT, padx=10)

        # Adds the cat ASCII art at the bottom
        # Adiciona o gato em ASCII art na parte inferior
        self.cat_label = Label(self.frame, text="""
  /\_/\\
 ( o.o )
  > ^ <
Alvin <3 (meu gato)
        """, font=("Monospace", 18), fg="white", bg="black")
        self.cat_label.pack(side=BOTTOM, anchor=CENTER, padx=10, pady=10)

        # Creates the label with my name (Henrique Jorge de Queiroz)
        # Cria a label com o meu nome (Henrique Jorge de Queiroz)
        self.creator_label = Label(self.frame, text="Criado por Henrique Jorge de Queiroz", font=("Helvetica", 18), fg="white", bg="black")
        self.creator_label.pack(side=BOTTOM, anchor=CENTER, padx=10, pady=5)

        # Creates the label with the message to press Esc to quit
        # Cria a label com a mensagem para pressionar Esc para sair
        self.quit_label = Label(self.frame, text="Pressione Esc para sair", font=("Helvetica", 18), fg="white", bg="black")
        self.quit_label.pack(side=BOTTOM, anchor=CENTER, padx=10, pady=5)

        # Bind the Esc key to the quit method
        # Liga a tecla Esc ao método quit
        master.bind('<Escape>', self.quit)

    def roll(self):
        # List of symbols to roll the dice with
        # Lista de símbolos para os dados
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

        # Number of dice to roll
        # Número de dados a serem rolados
        num_dice = self.num_dice.get()

        # Centralizes the dices on the screen
        # Centraliza os dados na tela
        for i in range(num_dice):
            self.dice_labels[i].config(text=random.choice(symbols))
            self.dice_labels[i].pack_configure(side=LEFT, padx=20, fill=BOTH, expand=True)
        for i in range(num_dice, 10):
            self.dice_labels[i].config(text="")
            self.dice_labels[i].pack_configure(side=LEFT, padx=20, fill=BOTH, expand=True)

    def quit(self, event):
        # Method to quit the program
        # Método para encerrar o programa
        root.quit()

# Creates the main window
# Cria a janela principal
root = Tk()

# Determinate the title of the window
# Define o título da janela
root.title("Rolador de Dados")

# Determine the background color to black
# Define a cor de fundo para preto
root.configure(bg="black")

# Determinate the window to open in fullscreen
# Define a janela para abrir em tela cheia
root.attributes('-fullscreen', True)

# Creates an instance of the DiceRoller class
# Cria uma instância da classe DiceRoller
DiceRoller(root)

# Initiates the events main loop
# Inicia o loop principal de eventos
root.mainloop()
