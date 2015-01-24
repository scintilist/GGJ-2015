from .game_obj import Game_Obj
from . import util
from .public_record import PublicRecord

class NPC(Game_Obj):
	def __init__(self, image, group = None, x = 400, y = 300, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)
	
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
