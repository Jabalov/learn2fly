import pygame

#Music
pygame.init()
file="Learn2Fly-Basic.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.mixer.music.rewind()


###################