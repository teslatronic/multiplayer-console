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


class Player(MoveableObject):
"""Player object. Might add another Entity class that this would inherit from."""
	pass


class Layer():
"""Each layer contains a 2D-array."""
	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.contents = [[None for x in range(sizeX)] for y in range(sizeY)] # Lists comprehensions are yummy. :3

class EnvironmentLayer(BaseState):
"""Stores  all environment objects in the game, plus an array with a background."""
	def __init__(self, sizeX, sizeY):
		super().__init__(sizeX, sizeY):
			self.background = [[None for x in range(self.sizeX)] for y in range(self.sizeY)]

			self.fillBackground(Tile('#'))

	def fillBackground(tile):
		for y in self.background:
			for x in self.background[y]:
				self.background[y][x] = tile


class EntityLayer(BaseState):
"""Stores all Entity objects, and contains an update() function to keep track of their positions."""
	def __init__(self, sizeX, sizeY):
		super().__init__(sizeX, sizeY)

	def update():
		# for each object in self.contents, read their positions. If changed, update contens accordingly.


def mainLoop():

	mainLoop()


def main(stdscr):
	# Argument parsing
	parser = argparse.ArgumentParser()
	args = parser.parse_args()

	stdscr.addstr(args.test)
	stdscr.getch()

if __name__ == "__main__":
	curses.wrapper(main) # Curses initialization