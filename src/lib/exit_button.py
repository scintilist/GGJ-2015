import pyglet

from .game_obj import GameObj
from . import util
from .public_record import PublicRecord

class ExitButton(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)

		self.visible = False
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_click(self, x, y):
		self.visible = True

	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_release(self, x, y):
		self.visible = False
		if self.room.is_over_object(self, x, y):
			pyglet.app.exit()
