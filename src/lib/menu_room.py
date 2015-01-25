import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util

from .room import *
from .public_record import PublicRecord
from .game_obj import GameObj
from .base_npc import NPC
from .button import *

class MenuRoom(Room):
	def __init__(self, width, height, g_scale = 1.0, window = None, record = PublicRecord()):
		super().__init__(width, height, g_scale, window, record, room_name = "menu")
		
		# Set player range constraints
		self.player.x_range = (100, width-100)
		self.player.y_range = (0, 150)
		
		# Don't show player on the menu screen
		self.player.visible = False
		
		# Get background from file
		bg_img = pyglet.resource.image("HubScreenBackGround.png")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale
		
		self.get_resources()
		self.build_objects()
		
	def on_key_press(self, symbol, modifier):
		if symbol == key._2:
			self.room_changer.change_room("placeholder")
			return True

		super().on_key_press(symbol, modifier)
		
	def get_resources(self):
		pass
		
	def build_objects(self):
		pass
		# Create room objects
		self.add_object(ExitButton, layer_offset = 5, x = 1920-72, y = 1080-72, scale = 1)
		self.add_object(PlayButton, layer_offset = 5, x = 1920/2, y = 144, scale = 1)
