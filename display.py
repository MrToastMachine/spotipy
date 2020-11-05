import pygame
pygame.init()
from main import get_song_info

RES = (660,750)

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

albumArt = pygame.image.load("currently_playing.jpg")
bgColour = (0,128,128)

def drawFrame():
    win.fill(bgColour)
    win.blit(albumArt, (10,10))
    text = textFont.render(info, 1, (250,250,250))
    win.blit(text, (10, 660))
    pygame.display.update()

textFont = pygame.font.SysFont('bahnschrift', 20, False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    song, artist = get_song_info()
    info = f"{song} - {artist}"

    drawFrame()

    albumArt = pygame.image.load("currently_playing.jpg")