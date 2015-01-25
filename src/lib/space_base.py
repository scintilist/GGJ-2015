import sys

from . import public_record
from . import placeholder_room
from . import menu_room

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
		}

		self.active_room = self.room_dict["menu"](self, room_name = "menu")

	def draw(self):
		self.active_room.batch.draw()
		
	def update(self, dt):
		self.active_room.update(dt)
		
	def change_room(self, next_room_name):
		try:
			if next_room_name in self.room_dict:
				self.active_room.cleanup()
				self.active_room = self.room_dict[next_room_name](self, room_name = next_room_name)
		except:
			print(sys.exc_info())
	