import pygame

from constants import *
from world import get_room
from code_image_exemple import *

img_monstre = pygame.image.load('Image_cruella.jpg')

def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    screen = pygame.display.set_mode((board_width, board_height + 40))
    pygame.display.set_caption("Sauvez 10 oiseaux pour gagner")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if bool(x % 2) == bool(y % 2):

                color = (200, 200, 200)
            else:
                color = (250, 250, 250)

            pygame.draw.rect(
                background,
                color,
                [
                    x * ROOM_SIZE,
                    y * ROOM_SIZE,
                    ROOM_SIZE,
                    ROOM_SIZE,
                ],
            )

    return screen, background


def update_screen(screen, background, world, player, inventory):
    player_x, player_y = player
    screen.blit(background, (0, 0))

    # couleur (red, green, blue)
    personnage=pygame.image.load('image_personnage_redimensionnee.jpg')
    screen.blit(
        personnage,
            (player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2)
    )

    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "cookie" in get_room(world, x, y):
                #pygame.draw.circle(
                    #screen,
                    #(250, 180, 40),
                    #(
                        #x * ROOM_SIZE + ROOM_SIZE - COOKIE_RADIUS * 2,
                        #y * ROOM_SIZE + ROOM_SIZE - COOKIE_RADIUS * 2,
                    #),
                    #COOKIE_RADIUS,
                #)
                cookie=pygame.image.load('image_cookie_redimensionnee.jpg')
                screen.blit(
                    cookie,
                        (x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
                        y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2)
                )
    
    #for y in range(WORLD_HEIGHT):
        #for x in range(WORLD_WIDTH):
            #if "sac" in get_room(world, x, y):
                #pygame.draw.rect(
                    #screen,
                    #(25, 94, 131),
                    #[
                        #x * ROOM_SIZE + ROOM_SIZE - BAG_SIZE * 2,
                        #y * ROOM_SIZE + ROOM_SIZE - BAG_SIZE * 2,
                        #BAG_SIZE,
                        #BAG_SIZE,
                    #],
                #)
    
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "monstre" in get_room(world, x, y):
                monstre=pygame.image.load('image_monstre_redimensionnee.jpg')
                screen.blit(
                    monstre,
                        (x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
                        y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2)
                )
                #pygame.draw.rect(
                    #screen,
                    #(0, 0, 0),
                    #[
                        #x * ROOM_SIZE + ROOM_SIZE - BAG_SIZE * 2,
                        #y * ROOM_SIZE + ROOM_SIZE - BAG_SIZE * 2,
                        #MONSTER_SIZE,
                        #MONSTER_SIZE,
                    #],
                #)
        
    x = 10
    for item in inventory:
        y = WORLD_HEIGHT * ROOM_SIZE + COOKIE_RADIUS * 2
        #if item=="sac":
            #pygame.draw.rect(
                #screen,
                #(25, 94, 131),
                #(x,y,BAG_SIZE,BAG_SIZE),
            #)
        if item=="cookie" :
            cookie=pygame.image.load('image_cookie_redimensionnee.jpg')
            screen.blit(
                cookie,
                    (x,
                    y)
            )
            #pygame.draw.circle(
                #screen,
                #(0, 0, 0),
                #(x, y),
                #COOKIE_RADIUS,
            #)       

        x += 30
    
    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
