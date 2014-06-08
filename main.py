import sys
import argparse
import curses

class Tile():
"""Simple class for 1-char objects. Might expand for larger, tileable shapes."""
	def __init__(self, char):
		self.char = char


class GameObject():
"""Base class for all objects in the game grid."""
	def __init__(self, posX, posY, tile):
		self.posX = posX
		self.posY = posY
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
	def __init__(self, sizeX, sizeY):
		super().__init__(sizeX, sizeY):
			self.sizeX = sizeX
			self.sizeY = sizeY
			self.contents = 2DList(sizeX, sizeY)
			self.background = 2DList(sizeX, sizeY)

			self.background.fill('0')


class 2DList():
	def __init__(self, sX, sY):
		self.list = [[None for x in range(sX)] for y in range(sY)]
		self.size = (sX, sY)

	def fill(obj):
		for y in self.list:
			for x in self.list[y]:
				self.list[y][x] = obj

	def set(x, y, obj):
		self.list[y][x] = obj


def handleInput(ent):
	pass


def handleDraw(ent):
	screen = 2DList(curses.COLS, curses.LINES)


def mainLoop(env, ent):
	running = True
	while running:
		handleInput(ent)
		handleDraw(ent)

		
def startGame():
	environment = Environment(curses.COLS, curses.LINES)
	entities = []

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
