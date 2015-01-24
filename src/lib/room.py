import pyglet
from pyglet.gl import *

from . import util

class Room:
	def __init__(self, width = 1920, height = 1080, player = None, g_scale = 1.0):
		self.room_batch = pyglet.graphics.Batch()

		self.bottom_left = util.Point(0, 0)
		self.top_right = util.Point(width, height)

		# Background is a game object w/ associated sprite
		self.background = None

		# Player is a game object w/ event handlers
		self.player = player

		# List of game_obj; everything in the room that isn't player or bg
		self.objects = [player]

class TestRoom(Room):
	def __init__(self, width, height, player):
		super().__init__(width, height, player)

