from .game_obj import GameObj
from . import util

class TinyKim(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.kim_idle_right = util.make_animation('KimIdelV2_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		room.kim_idle_left = room.kim_idle_right.get_transform(flip_x = True)
		image = room.kim_idle_left
		
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
	
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_click(self, x, y):
		self.room.set_active_npc(self)
