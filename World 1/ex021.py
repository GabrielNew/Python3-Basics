import pygame

# ex021 -> Programa para tocar uma música.

pygame.init()
pygame.mixer.music.load('nomedamusica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
