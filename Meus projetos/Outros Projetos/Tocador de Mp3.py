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
