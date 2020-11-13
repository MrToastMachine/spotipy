import pygame
pygame.init()
from main import get_song_info
import cv2 as cv
import numpy as np 

RES = (660,750)

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

albumArt = pygame.image.load("currently_playing.jpg")
bgColour = (0,128,128)

def drawFrame():
    win.fill(getAvgColour())
    win.blit(albumArt, (10,10))
    text_colour = [(x+100)%255 for x in getAvgColour()]
    text = textFont.render(info, 1, text_colour)
    win.blit(text, (10, 660))
    pygame.display.update()

def getAvgColour():
    dim = (500, 300)
    img = cv.imread("currently_playing.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    img_temp = img.copy()
    img_temp[:,:,0], img_temp[:,:,1], img_temp[:,:,2] = np.average(img, axis=(0,1))
    col = img_temp[0][0]
    return ([x for x in col])

textFont = pygame.font.SysFont('bahnschrift', 20, False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            getAvgColour()

    song, artist = get_song_info()
    info = f"{song} - {artist}"

    drawFrame()

    albumArt = pygame.image.load("currently_playing.jpg")