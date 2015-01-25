import pyglet

from .game_obj import GameObj
from . import util
from .public_record import PublicRecord

'''dialog_width = 600
dialog_height = 200
self.label = pyglet.text.Label("That's okay; I wouldn't expect anyone to recognize little ol' me anymore.",
	  font_name='Helvetica',
	  font_size=12,
	  x = (1920/2 - dialog_width/2) * g_scale, y = (1080/2 + dialog_height/2) * g_scale,
	  anchor_x='left', anchor_y='top', batch = self.batch, group = self.layers[self.player_layer+1],
	  multiline = True,
	  width = dialog_width * g_scale,
	  height = dialog_height * g_scale,
	)
self.label.set_style('background_color', (0, 0, 0, 255))'''

class NPCDialog(GameObj):
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		# Get the image here	
		image = pyglet.resource.image("npc_dialog.png")
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)

		self.label = pyglet.text.Label("That's okay; I wouldn't expect anyone to recognize little ol' me anymore.",
			  font_name='Helvetica',
			  font_size=12,
			  # x = self.x * g_scale, y = self.y * g_scale,
			  x = self.x * self.g_scale, y = self.y * self.g_scale,
			  anchor_x='left', anchor_y='bottom', batch = self.room.batch, group = self.room.layers[self.room.player_layer+3],
			  multiline = True,
			  width = 640 * self.g_scale,
			  height = 270 * self.g_scale,
			  color = (0, 0, 0, 255),
			)
		# self.label.set_style('background_color', (0, 0, 0, 255))'''

class KimDialog(GameObj):
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		# Get the image here	
		image = pyglet.resource.image("kim_dialog.png")
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)
