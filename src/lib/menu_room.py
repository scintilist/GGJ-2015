import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util

from .room import *
from .public_record import PublicRecord
from .game_obj import GameObj
from .base_npc import NPC

class MenuRoom(Room):
	def __init__(self, width, height, g_scale = 1.0, window = None, record = PublicRecord()):
		super().__init__(width, height, g_scale, window, record, room_name = "menu")
		
		# Set player range constraints
		self.player.x_range = (100, width-100)
		self.player.y_range = (80, 200)
		
		# Get background from file
		bg_img = pyglet.resource.image("rockstarguy.jpg")
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
		# Create animation from file
		
		self.npc_animation = util.make_animation('KimWalkV2_.png', frame_count = 90, num_digits = 5, center_x = True, loop = True, duration = 1/30)
		
	def build_objects(self):
		# Create animated room object from animation

		self.add_object(NPC, self.npc_animation, layer_offset = 1, x = 600, y = 50, scale = .4)
