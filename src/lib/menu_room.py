import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from .room import *
from .button import *

class MenuRoom(Room):
	def __init__(self, space_base = None, room_name = 'menu', start_x = 0, start_y = 0):
		super().__init__(space_base, room_name, start_x, start_y)
		
		# Don't show player on the menu screen
		self.player.visible = False
		
		# Get background from file
		bg_img = pyglet.resource.image("HubScreenBackGround.png")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale
		
		self.build_objects()
		
	def on_key_press(self, symbol, modifier):
		# MenuRoom captured keys here
	
		#if symbol == key._2:
		#	self.room_changer.change_room("placeholder")
		#	return True

		super().on_key_press(symbol, modifier)
		
	def build_objects(self):
		pass
		# Create room objects
		self.add_object(ExitButton, layer_offset = 5, x = 1920-73, y = 1080-72, scale = 1)
		self.add_object(PlayButton, layer_offset = 5, x = 1920/2, y = 144, scale = 1)
