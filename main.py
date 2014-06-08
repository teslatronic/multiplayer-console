import sys
import argparse
import curses


class 2DList():
	def __init__(self, sX, sY):
		self.list = [[None for x in range(sX)] for y in range(sY)]
		self.size = (sX, sY)

	def fill(obj):
		for y in self.list:
			for x in y:
				x = obj

	def setPos(x, y, obj):
		self.list[y][x] = obj

	def layer(otherList):
	"""Layers another 2DList on top of this list and returns the result."""
		if self.size != otherList.size:
			raise IndexError("2D Lists must be same size.")

		result = 2DList(self.size[0], self.size[1])

		for y in range(len(self.list)):
			for x in range(len(self.list[y])):
				if otherList[y][x] == None:
					result.setPos(x, y, self.list[y][x])
				else:
					result.setPos(x, y, otherList[y][x])

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
	def __init__(self):
		super().__init__()


class EntityObject(GameObject):
"""For all objects that move, and/or interact with the environment."""
	def __init__(self):
		super().__init__()
	
	def move(dX, dY):
		self.posX += dX
		self.posY += dY


class Player(EntityObject):
"""Player object. Inherits from Entity."""
	def __init__(self):
		super().__init__()


class Environment():
"""Stores  all environment objects in the game, plus a list with a background."""
	def __init__(self):
		super().__init__()
		self.contents = 2DList(sizeX, sizeY)
		self.background = 2DList(sizeX, sizeY)
		self.background.fill('0')

	def layered():
		return self.contents.list


def handleInput(ent):
	pass


def handleDraw(env, ent):
	screen = list(env.layered())


def mainLoop(env, ent):
	running = True
	while running:
		handleInput(ent)
		handleDraw(env, ent)

		
def startGame():
	environment = Environment(curses.COLS, curses.LINES)
	entities = []

	localPlayer = Player()
	entities.append(localPlayer)

	mainLoop(environment, entities)


def main(stdscr):
	# Argument parsing
	parser = argparse.ArgumentParser()
	args = parser.parse_args()

	stdscr.addstr(args.test)
	stdscr.getch()

	startGame()

if __name__ == "__main__":
	curses.wrapper(main) # Curses initialization
