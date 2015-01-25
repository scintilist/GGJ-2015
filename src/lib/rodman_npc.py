from .base_npc import NPC
from . import util
from .dialog_data import rodman_1, rodman_hate_convo, rodman_love_convo

class Rodman(NPC):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.rodman_idle = util.make_animation('RodmanIdel_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		image = room.rodman_idle
		
		# Build base NPC
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
		
		self.convo = rodman_1
		self.what_im_saying = ""
		
	def start_converstion(self):
		self.convo = rodman_1
		if "rodman_hate" in self.record["choices"]:
			self.convo = rodman_hate_convo
		elif "rodman_love" in self.record["choices"]:
			self.convo = rodman_love_convo

		super().start_conversation()