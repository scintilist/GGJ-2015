import pyglet

from .game_obj import GameObj
from . import util

class NPCDialog(GameObj):
	
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None, text_string = ''):
		# Get the image here	
		image = pyglet.resource.image("NPCSpeechBubble.png")
		image.anchor_x = image.width/2
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
		
		self.label = None
		
		self.set_text_string(text_string)
		
	def __del__(self):
		try:
			self.label.delete()
		except:
			pass

	def set_text_string(self, new_string):
		self.text_string = new_string
		if self.label:
			self.label.delete()
		if self.visible:
			self.label = pyglet.text.Label(new_string,
			  font_name='Helvetica',
			  font_size=14,
			  x = self.x * self.g_scale, y = (self.y + self.scale * self.sprite.image.height/2) * self.g_scale,
			  anchor_x='center', anchor_y='center', batch = self.room.batch, group = self.room.layers[self.room.player_layer+3],
			  multiline = True,
			  width = 600 * self.g_scale,
			  height = 230 * self.g_scale,
			  color = (0, 0, 0, 255),
			  align = "center",
			)
			self.label.content_valign = "center"

	def hide(self):
		if self.label:
			self.label.delete()
		self.visible = False

	def show(self):
		self.visible = True
		self.set_text_string(self.text_string)


class KimDialog(GameObj):
	def __init__(self, image = None, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None, text_string = ''):
		# Get the image here	
		self.unpressed_image = pyglet.resource.image("KimSpeechBubbleGreen.png")
		self.unpressed_image.anchor_x = self.unpressed_image.width/2
		self.pressed_image = pyglet.resource.image("KimSpeechBubbleGreen_Dark.png")
		self.pressed_image.anchor_x = self.pressed_image.width/2
		
		super().__init__(self.unpressed_image, group, x, y, scale, rotation, visible, opacity, room)

		self.label = None

		self.set_text_string(text_string)
		
	def __del__(self):
		try:
			self.label.delete()
		except:
			pass
		
	def set_text_string(self, new_string):
		self.text_string = new_string
		if self.label:
			self.label.delete()
		if self.visible:
			self.label = pyglet.text.Label(new_string,
			  font_name='Helvetica',
			  font_size=14,
			  x = self.x * self.g_scale, y = (self.y + self.scale * self.sprite.image.height/2) * self.g_scale,
			  anchor_x='center', anchor_y='center', batch = self.room.batch, group = self.room.layers[self.room.player_layer+3],
			  multiline = True,
			  width = 600 * self.g_scale,
			  height = 70 * self.g_scale,
			  color = (0, 0, 0, 255),
			  align = "center",
			)
			self.label.content_valign = "center"

	def hide(self):
		if self.label:
			self.label.delete()
		self.visible = False

	def show(self):
		self.visible = True
		self.set_text_string(self.text_string)
		
	def mouse_press(self, x, y):
		self.sprite.image = self.pressed_image

	def mouse_release(self, x, y):
		self.sprite.image = self.unpressed_image
		if self.room.is_over_object(self, x, y):
			self.room.active_npc.box_clicked(self.text_string)
