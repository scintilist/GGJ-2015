from .game_obj import Game_Obj

class NPC(Game_Obj):
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255, room = None):
		super().__init__(image, batch, group, x, y, g_scale, scale, rotation, visible, opacity, room = room)
	
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
