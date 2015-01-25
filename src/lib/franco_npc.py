from .base_npc import NPC
from . import util
from .dialog_franco import *

class Franco(NPC):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		try:
			# Get object initial image
			room.franco_idle = util.make_animation('franco_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
			image = room.franco_idle
			
			# Build base NPC
			super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)

			self.dialog_manager = FrancoDialog(self.record)
			
			self.convo = self.dialog_manager.franco_1()
			self.what_im_saying = ""
		except:
			import sys, traceback
			traceback.print_tb(sys.exc_info()[2])
		
	def start_conversation(self):
		import sys, traceback
		try:
			if "franco_hate" in self.record["choices"] or "franco_love" in self.record["choices"]:
				self.convo = self.dialog_manager.franco_followup()

			super().start_conversation()
		except:
			# pass
			traceback.print_tb(sys.exc_info()[2])
			print(sys.exc_info())

