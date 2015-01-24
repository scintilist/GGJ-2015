import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from . import game_obj
from .room import *
from .public_record import PublicRecord

class PlaceholderRoom(Room):
	def __init__(self, width, height, g_scale = 1.0, window = None, record = PublicRecord()):
		super().__init__(width, height, g_scale, window, record, room_name = "maddie")
		
		# Set player range constraints
		self.player.x_range = (100, width-100)
		self.player.y_range = (80, 200)
		
		# Get background from file
		bg_img = pyglet.resource.image("PlaceHolderRoomBackground01.png")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale
		
		self.get_resources()
		self.build_objects()
		
	def get_resources(self):
		# Create animation from file
		# self.place_animation = util.make_animation('num.png', frame_count = 6, num_digits = 2, center = True, loop = True, duration = .4)
		self.place_animation = util.make_animation('num.png', frame_count = 9, num_digits = 2, center = True, loop = True, duration = .2)
		
	def build_objects(self):
		# Create animated room object from animation
		obj = game_obj.Game_Obj(self.place_animation, batch = self.batch, group = self.layers[1], 
			x = 100, y = 200, g_scale = self.g_scale, scale = 2)

		self.objects.append(obj)
		

		
