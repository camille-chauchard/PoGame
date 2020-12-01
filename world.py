import random

from constants import *


def create_world():
    world = []

    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if random.randint(0, 9) == 0 and (x, y) != (0, 0):
                world.append(["cookie"])
            if random.randint(0, (WORLD_HEIGHT*WORLD_WIDTH)/8) == 0 and (x, y) != (0, 0):
                world.append(["sac"])
            if random.randint(0, WORLD_HEIGHT*WORLD_WIDTH / 4) == 0 and (x, y) != (0, 0):
                world.append(["monstre"])
            else:
                world.append([])

    return world

def get_index(x, y):
    return y * WORLD_WIDTH + x

def get_room(world, x, y):
    index = get_index(x, y)
    return world[index]