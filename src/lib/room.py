import pyglet
from pyglet.gl import *

from . import util

class Room:
	def __init__(self, width = 1920, height = 1080, player = None, g_scale = 1.0):
		# Player is a game object w/ event handlers
		self.player = player

		# Batches ain't shit but groups and tricks
		self.room_batch = pyglet.graphics.Batch()

		self.layers = []
		self.player_layer = 5

		for i in range(-self.player_layer, self.player_layer+1):
			layer = pyglet.graphics.OrderedGroup(i)
			self.layers.append(layer)

		self.player.sprite.batch = self.room_batch
		self.player.sprite.group = self.layers[self.player_layer]

		self.bottom_left = util.Point(0, 0)
		self.top_right = util.Point(width, height)

		# List of game_obj; everything in the room that isn't player or bg
		self.objects = [player]

class TestRoom(Room):
	def __init__(self, width, height, player):
		super().__init__(width, height, player)

		bg_img = pyglet.resource.image("rockstarguy.jpg")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.room_batch, group = self.layers[0])

		# fg_img = pyglet.resource.image("rockstarguy.jpg")
		# self.fg_sprite = pyglet.sprite.Sprite(fg_img, x = 0, y = 0, batch = self.room_batch, group = self.layers[-1])

		

