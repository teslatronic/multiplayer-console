import sys
import argparse
import curses


class List2D():
    def __init__(self, sX, sY):
        self.list = [[None for x in range(sX)] for y in range(sY)]
        self.size = (sX, sY)

    def __getitem__(self, key):  # Makes the list accessible like a normal list
        return self.list[key]

    def __setitem__(self, key, value):  # Also allows editing
        self.list[key] = value

    def fill(self, obj):
        for y in self.list:
            for x in y:
                x = obj

    def set_position(self, x, y, obj):
        self.list[y][x] = obj

    def layer(self, otherList):
        """Layers another List2D on top of this list and returns the result."""
        if self.size != otherList.size:
            raise IndexError("2D Lists must be same size.")

        result = List2D(self.size[0], self.size[1])

        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                if otherList[y][x] is None:
                    result[y][x] = self[y][x]
                else:
                    result[y][x] = otherList[y][x]

        return result


class Tile():
    """Simple class for 1-char objects. Might expand for larger, tileable shapes."""
    def __init__(self, char):
        self.char = char


class GameObject():
    """Base class for all objects in the game grid."""
    def __init__(self, posX, posY, tile):
        self.posX = posX
        self.posY = posY
        self.pos = (posX, posY)
        self.tile = tile


class EnvironmentObject(GameObject):
    """An object that represents a part of the environment. """
    def __init__(self, posX, posY, tile):
        super().__init__(posX, posY, tile)


class EntityObject(GameObject):
    """For all objects that move, and/or interact with the environment."""
    def __init__(self, posX, posY, tile):
        super().__init__(posX, posY, tile)
    
    def move(self, dX, dY):
        self.posX += dX
        self.posY += dY


class Player(EntityObject):
    """Player object. Inherits from EntityObject."""
    def __init__(self, posX, posY, tile):
        super().__init__(posX, posY, tile)


class Environment():
    """Stores  all environment objects in the game, plus a list with a background."""
    def __init__(self, sizeX, sizeY):
        self.contents = List2D(sizeX, sizeY)
        self.background = List2D(sizeX, sizeY)
        self.background.fill('0')

    def layered(self):
        return self.background.layer(self.contents)


def handle_input(stdscr, localPlayer):
    key = stdscr.getch()
    
    if key == curses.KEY_UP:
        localPlayer.move(0, 1)
    if key == curses.KEY_DOWN:
        localPlayer.move(0, -1)
    if key == curses.KEY_RIGHT:
        localPlayer.move(1, 0)
    if key == curses.KEY_LEFT:
        localPlayer.move(-1, 0)


def handle_draw(stdscr, environment, entities):
    screen = list(environment.layered())

    for entity in entities:
        screen[entity.posX][entity.posX] = entity.tile.char

    for y in range(len(screen)):
        for x in range(len(screen[y])):
            stdscr.addstr(y, x, str(screen[y][x]))

    stdscr.refresh()


def main_loop(stdscr):
    environment = Environment(curses.COLS, curses.LINES)
    entities = set()

    localPlayer = Player(10, 10, Tile('P'))
    entities.add(localPlayer)

    running = True
    while running:
        handle_input(stdscr, localPlayer)
        handle_draw(stdscr, environment, entities)


def main(stdscr):
    # Argument parsing
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    stdscr.clear()

    main_loop(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)  # Curses initialization
