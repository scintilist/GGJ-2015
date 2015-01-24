from . import anim_sprite

class Game_Obj():
	''' Some game object containing a sprite, draw method, and things to do on update'''
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		self.sprite = anim_sprite.Anim_Sprite(image, x*g_scale, y*g_scale, batch = batch, group = group)
		
		# Sprite stuff
		self.x = x # pixel values based on 1920x1080
		self.y = y 
		self.scale = scale
		self.g_scale = g_scale
		self.rotation = rotation # degrees clockwise
		self.opacity = opacity # 0 -255
		self.visible = visible # True or False
		
		self.update_sprite() # save game object values to the sprite
		
		# Non-sprite stuff
		self.theta = 0
		self.vx = 0
		self.vy = 0
		
	def update(self, dt):
		self.update_position(dt)
		self.update_sprite()
		
	def update_position(self, dt):
		# update object posistion
		self.x += self.vx
		self.y += self.vy
		self.rotation += self.theta
			
	def update_sprite(self):
		self.sprite.x = self.x * self.g_scale
		self.sprite.y = self.y * self.g_scale
		self.sprite.scale = self.scale * self.g_scale
		self.sprite.rotation = self.rotation
		self.sprite.visible = self.visible
		self.sprite.opacity = self.opacity
		
class Player(Game_Obj):
	''' Player character'''
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, group, x, y, g_scale, scale, rotation, visible, opacity)
		pass
		
	def update(self, dt):
		super().update_position(dt)
		
		# DO STUFF HERE
		
		super().update_sprite()
		
# 
#	TEST OBJECT PLEASE IGNORE
#		
	
class Rockstar(Game_Obj):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, group, x, y, g_scale, scale, rotation, visible, opacity)

		self.scale_v = .1
		self.rot_v = 4
		
		self.scale_max = 2
		self.scale_min = .3
		
	def update(self, dt):
		super().update_position(dt)
		
		self.scale += self.scale_v
		self.rotation += self.rot_v

		if self.scale < self.scale_min or self.scale > self.scale_max:
			self.scale_v *= -1
			self.rot_v *= -1
			
		super().update_sprite()
			
class Spinning_Nums(Rockstar):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, group, x, y, g_scale, scale, rotation, visible, opacity)
		
		self.scale_v = .03
		self.rot_v = 2
		
		self.scale_max = 2
		self.scale_min = -2
		
		self.rotation = 0
		self.scale = 0

		self.opacity = 128
		
