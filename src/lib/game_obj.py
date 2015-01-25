from . import anim_sprite
from .public_record import PublicRecord
from . import util

class GameObj():
	''' Some game object containing a sprite, draw method, and things to do on update'''
	def __init__(self, image, group = None, x = 400, y = 300, scale = 1.0, 
			rotation = 0, visible = True, opacity = 255, record = PublicRecord(), room = None,
			x_range = (float('-inf'), float('+inf')), y_range = (float('-inf'), float('+inf'))):
		self.sprite = anim_sprite.Anim_Sprite(image, x*room.g_scale, y*room.g_scale, batch = room.batch, group = group)
		
		self.room = room
		
		# Sprite stuff
		self.x = x # pixel values based on 1920x1080
		self.y = y 
		self.scale = scale
		self.g_scale = room.g_scale
		self.rotation = rotation # degrees clockwise
		self.opacity = opacity # 0 -255
		self.visible = visible # True or False

		self.record = record
		
		self.update_sprite() # save game object values to the sprite
		
		# Non-sprite stuff
		self.theta = 0
		self.vx = 0
		self.vy = 0
		
		self.x_range = x_range
		self.y_range = y_range
		
	def update(self, dt):
		self.update_position(dt)
		self.update_sprite()
		
	def update_position(self, dt):
		# update object posistion
		self.x += self.vx
		self.y += self.vy
		self.rotation += self.theta
		
		# Constrain object to range rectangle
		self.x = util.constrain(self.x, *self.x_range)
		self.y = util.constrain(self.y, *self.y_range)
			
	def update_sprite(self):
		self.sprite.x = self.x * self.g_scale
		self.sprite.y = self.y * self.g_scale
		self.sprite.scale = self.scale * self.g_scale
		self.sprite.rotation = self.rotation
		self.sprite.visible = self.visible
		self.sprite.opacity = self.opacity