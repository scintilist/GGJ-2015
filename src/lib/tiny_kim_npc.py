from .base_npc import NPC
from . import util
from .dialog_tinykim import *

import sys

class TinyKim(NPC):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.kim_idle_right = util.make_animation('KimIdelV2_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		room.kim_idle_left = room.kim_idle_right.get_transform(flip_x = True)
		image = room.kim_idle_left
		
		# Build base NPC
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)

		self.dialog_manager = TinyKimDialog(self.record)
		
		self.convo = self.dialog_manager.info1()
		self.what_im_saying = ""

	def start_conversation(self):
		if "tinykim_info_done" in self.record["choices"]:
			if "rodman_spoken_to" in self.record["choices"]:
				self.convo = self.dialog_manager.post_rodman()
			else:
				self.convo = self.dialog_manager.nag()
		else:
			print(self.record["choices"])
		super().start_conversation()
