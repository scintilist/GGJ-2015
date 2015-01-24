from . import anim_sprite

class Game_Obj():
	''' Some game object containing a sprite, draw method, and things to do on update'''
	def __init__(self, image, batch = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		self.sprite = anim_sprite.Anim_Sprite(image, x*g_scale, y*g_scale, batch = batch)
		
		self.x = x # pixel values based on 1920x1080
		self.y = y 
		self.scale = scale
		self.g_scale = g_scale
		self.rotation = rotation # degrees clockwise
		self.opacity = opacity # 0 -255
		self.visible = visible # True or False
		
		self.update_sprite() # save game object values to the sprite
		
	def update(self, dt):
		# DO STUFF
		self.update_sprite()
			
	def update_sprite(self):
		self.sprite.x = self.x * self.g_scale
		self.sprite.y = self.y * self.g_scale
		self.sprite.scale = self.scale * self.g_scale
		self.sprite.rotation = self.rotation
		self.sprite.visible = self.visible
		self.sprite.opacity = self.opacity
		
def Player(Game_Obj):
	''' Player character'''
	def __init__(self, image, batch = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, x, y, g_scale, scale, rotation, visible, opacity)
		
	def update(self, dt):
		pass
		
		super().update(dt)
		
		
# 
#	TEST OBJECTS DO NOT MODIFY
#		
	
class Rockstar(Game_Obj):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, x, y, g_scale, scale, rotation, visible, opacity)

		self.scale_v = .1
		self.rot_v = 4
		
		self.scale_max = 2
		self.scale_min = .3
		
	def update(self, dt):
		self.scale += self.scale_v
		self.rotation += self.rot_v

		if self.scale < self.scale_min or self.scale > self.scale_max:
			self.scale_v *= -1
			self.rot_v *= -1
			
		super().update(dt)
			
class Spinning_Nums(Rockstar):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, x, y, g_scale, scale, rotation, visible, opacity)
		
		self.scale_v = .03
		self.rot_v = 2
		
		self.scale_max = 2
		self.scale_min = -2
		
		self.rotation = 0
		self.scale = 0

		self.opacity = 128
		
