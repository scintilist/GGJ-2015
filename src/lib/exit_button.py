from .game_obj import GameObj

class ExitButton(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)

		self.visible = False

	def mouse_click(self, x, y):
		self.visible = True

	def mouse_release(self, x, y):
		self.visible = False
		pyglet.app.exit()
