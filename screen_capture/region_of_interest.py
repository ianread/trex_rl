import pygame, sys
from pygame.locals import *

from PIL import ImageGrab
from PIL import Image

def reorder(x1, y1, x2, y2):

    low_x = x2 if (x1 > x2) else x1
    low_y = y2 if (y1 > y2) else y1
    high_x = x1 if (x1 > x2) else x2
    high_y = y1 if (y1 > y2) else y2

    width = high_x - low_x
    height = high_y - low_y

    return {"x": low_x, "y": low_y, "width": width, "height": height}

def select_region():
    image = ImageGrab.grab()

    mode = image.mode
    size = image.size
    data = image.tobytes()

    pygame.init()
    pygame.display.set_mode(image.size)

    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    py_image = pygame.image.fromstring(data, size, mode)

    mainLoop = True

    return_dict = {}

    while mainLoop:
        DISPLAYSURF.blit(py_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainLoop = False
                    continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if len(return_dict.keys()) == 0:
                   return_dict["x1"] =  pos[0]
                   return_dict["y1"] =  pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if len(return_dict.keys()) == 2:
                   return_dict["x2"] =  pos[0]
                   return_dict["y2"] =  pos[1]

        pos = pygame.mouse.get_pos()
        if len(return_dict.keys()) == 2:
            bb_dict = reorder(return_dict["x1"], return_dict["y1"], pos[0], pos[1])
            pygame.draw.rect(DISPLAYSURF, (0,0,255), (bb_dict["x"], bb_dict["y"], bb_dict["width"], bb_dict["height"]), 2)
            pygame.display.update()

        if len(return_dict.keys()) == 4:
            mainLoop = False
        pygame.display.update()

    pygame.quit()

    if(len(return_dict.keys()) == 4):
        return reorder(return_dict["x1"], return_dict["y1"], return_dict["x2"], return_dict["y2"])
    else:
        return return_dict


