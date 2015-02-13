import pyglet

from .game_obj import GameObj
from . import util

class ExitButton(GameObj):
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get the image here	
		image = pyglet.resource.image("HubScreenExitBut_Dark.png")
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
		self.visible = False
		
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_press(self, x, y):
		self.visible = True

	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_release(self, x, y):
		self.visible = False
		if self.room.is_over_object(self, x, y):
			pyglet.app.exit()


class PlayButton(GameObj):
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get the image here
		image = pyglet.resource.image("HubScreenPlayBut_Dark.png")
		image.anchor_x = image.width/2
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
		self.visible = False
		
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_press(self, x, y):
		self.visible = True

	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_release(self, x, y):
		self.visible = False
		if self.room.is_over_object(self, x, y):
			self.room.space_base.change_room("placeholder")
