'''EN: WARNING: When importing your song, you'll need the archive mp3 in your computer and put his name in the parenthesis below, in this case, I utilized a music that I like and I put 
there. If you try to execute this program without the song installed in your computer the program will fail, try with another song or download this song below "Ladyfingers" and name it, 
the name should stay inside of the parenthesis (line 16) and it has to be exacly the name of your archive.

BR: AVISO: Quando for importar sua música, você vai precisar do arquivo mp3 em seu computador e colocar o nome dele entre parênteses abaixo, neste caso, utilizei uma música que gosto e 
coloquei lá. Se você tentar executar este programa sem a música baixada em seu computador o programa irá falhar, tente com outra música ou baixe esta música abaixo "Ladyfingers" e
nomeie-o, o nome deve ficar entre parênteses (na linha 16) e deve ser exatamente o nome do seu arquivo.'''

''' EN: importing the pygame library, which is aimed at games but you can use it to play music too
BR: importando a biblioteca pygame, que é voltada para jogos mas você consegue usar ela para tocar músicas também'''
import pygame
pygame.init()

'''EN: Importing the song
BR: Importando a música'''
pygame.mixer.music.load('ladyfingers.mp3')

'''EN: Initiating the song
BR: Iniciando a música'''
pygame.mixer.music.play()

'''EN: Putting how long this song will be played (in miliseconds, that are 50 seconds playing the music)
BR: Colocando por quanto tempo essa música vai ser tocada (em milisegundos, que são 50 segundos de música) '''
pygame.time.wait (50000)