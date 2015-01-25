import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from .room import *
from .tiny_kim_npc import TinyKim
from .rodman_npc import Rodman
from .franco_npc import Franco
from .dialog_boxes import *

class PlaceholderRoom(Room):
	def __init__(self, space_base = None, room_name = 'placeholder', start_x = 400, start_y = 0):
		super().__init__(space_base, room_name, start_x, start_y)
		
		# Set player range constraints
		self.player.x_range = (200, self.width-200)
		self.player.y_range = (0, 150)
		
		# Get background from file
		bg_img = pyglet.resource.image("PlaceHolderRoomBackground01.png")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale
		
		self.build_objects()
		
	def on_key_press(self, symbol, modifier):
		if symbol == key.M or symbol == key.H or symbol == key.F1:
			self.space_base.change_room("menu")
			return True

		super().on_key_press(symbol, modifier)
		
	def build_objects(self):
		# Create room objects
		self.add_object(Rodman, layer_offset = 1, x = 1600, y = 50, scale = 1.0)
		self.add_object(TinyKim, layer_offset = 1, x = 1000, y = 50, scale = .4)
		self.add_object(Franco, layer_offset = 1, x = 1300, y = 50, scale = 1.0)
