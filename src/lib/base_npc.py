from .game_obj import GameObj
from . import util

class NPC(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.tiny_kim = util.make_animation('KimWalkV2_.png', frame_count = 90, num_digits = 5, center_x = True, loop = True, duration = 1/30)
		image = room.tiny_kim
		
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
	
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_click(self, x, y):
		print("npc mouse click was called")
		if self.room is None:
			print("no room")
		if self.room.player is None:
			print("no player")
		if util._dist(self.x, self.y, self.room.player.x, self.room.player.y) < 300:
			print("DIALOG")
		else:
			print("NO DIALOG")
