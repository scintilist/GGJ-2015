import gc
import pyglet

from . import public_record
from . import placeholder_room
from . import placeholder2
from . import menu_room

from . import room

class SpaceBase():
	def __init__(self, abs_width, abs_height, g_scale, window):
		# Save all the important global things
		self.abs_width = abs_width
		self.abs_height = abs_height
		self.g_scale = g_scale
		self.window = window
	
		# Make the public record
		self.record = public_record.PublicRecord()
		
		# Names of all the rooms
		self.room_dict = {
			"menu": menu_room.MenuRoom,
			"placeholder": placeholder_room.PlaceholderRoom,
			"placeholder2": placeholder2.PlaceholderRoom2,
		}
		
		# Make the game batch
		self.batch = pyglet.graphics.Batch()

		self.active_room = self.room_dict["menu"](self, room_name = "menu")
		self.active_room.first = True

		
	def draw(self):
		self.active_room.batch.draw()
		
	def update(self, dt):
		self.active_room.update(dt)
		
	def change_room(self, next_room_name):
		#try:
		if next_room_name in self.room_dict:
			self.active_room.cleanup()
			self.active_room = self.room_dict[next_room_name](self, room_name = next_room_name)
		gc.collect()
		print('gc.get_objects(): ' + str(len(gc.get_objects())) )


		
