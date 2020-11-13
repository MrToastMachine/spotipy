import pygame
pygame.init()
from main import get_song_info
import cv2 as cv
import numpy as np

RES = (750,750)

win = pygame.display.set_mode(RES, pygame.RESIZABLE)
clock = pygame.time.Clock()

lowRes = (50,50)
albumArt = pygame.image.load("currently_playing.jpg")
bgColour = (0,128,128)
baubles = np.zeros([lowRes[0], lowRes[1], 3], dtype=np.uint8)


def drawFrame():
    # win.fill(getArtInfo())
    win.fill((0,0,0))
    # win.blit(albumArt, (10,10))
    text_colour = [(x+100)%255 for x in getArtInfo()]
    text = textFont.render(info, 1, text_colour)
    # win.blit(text, (10, 660))
    for i in range(len(baubles)):
        for j in range(len(baubles[0])):
            pos = (j*15+7, i*15+7)
            pygame.draw.circle(win, baubles[i,j], pos, 5)
    pygame.display.update()

def getArtInfo():
    dim = lowRes
    img = cv.imread("currently_playing.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    baubles[:,:] = img[:,:]
    col = img[0][0]
    return ([x for x in col])

textFont = pygame.font.SysFont('bahnschrift', 20, False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            getArtInfo()

    song, artist = get_song_info()
    info = f"{song} - {artist}"

    drawFrame()

    albumArt = pygame.image.load("currently_playing.jpg")