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

STILL = 1
BOTH_DOWN = 2
WALK_LEFT = 3
WALK_RIGHT = 4
WALK_UP = 5
WALK_DOWN = 6

class Player(Game_Obj):
	''' Player character'''
	def __init__(self, image, batch = None, group = None, x = 400, y = 300, g_scale = 1.0, 
			scale = 1.0, rotation = 0, visible = True, opacity = 255):
		super().__init__(image, batch, group, x, y, g_scale, scale, rotation, visible, opacity)
		
		self.lr_state = STILL
		self.ud_state = STILL
		
	def update(self, dt):
		super().update_position(dt)
		
		# DO STUFF HERE
		
		self.update_sprite()
		
	def update_sprite(self):
		# Enable if you want the player to shrink as they walk up the screen
		z_scale = 1 #- .5*(self.y / 1080)
		
		self.sprite.x = self.x * self.g_scale
		self.sprite.y = self.y * self.g_scale
		self.sprite.scale = self.scale * self.g_scale * z_scale
		self.sprite.rotation = self.rotation
		self.sprite.visible = self.visible
		self.sprite.opacity = self.opacity
		
	def mouse_click(self, x, y):
		self.visible = not self.visible
	
	# Left and right movement
	def left_press(self):
		if self.lr_state == STILL:
			self.lr_state = WALK_LEFT
			self.vx = -5
		elif self.lr_state == WALK_RIGHT:
			self.lr_state = BOTH_DOWN
			self.vx = 0

	def right_press(self):
		if self.lr_state == STILL:
			self.lr_state = WALK_RIGHT
			self.vx = 5
		elif self.lr_state == WALK_LEFT:
			self.lr_state = BOTH_DOWN
			self.vx = 0

	def left_release(self):
		if self.lr_state == WALK_LEFT:
			self.lr_state = STILL
			self.vx = 0
		elif self.lr_state == BOTH_DOWN:
			self.lr_state = WALK_RIGHT
			self.vx = 5

	def right_release(self):
		if self.lr_state == WALK_RIGHT:
			self.lr_state = STILL
			self.vx = 0
		elif self.lr_state == BOTH_DOWN:
			self.lr_state = WALK_LEFT
			self.vx = -5
	
	# Up and down movement
	def down_press(self):
		if self.ud_state == STILL:
			self.ud_state = WALK_DOWN
			self.vy = -5
		elif self.ud_state == WALK_UP:
			self.ud_state = BOTH_DOWN
			self.vy = 0

	def up_press(self):
		if self.ud_state == STILL:
			self.ud_state = WALK_UP
			self.vy = 5
		elif self.ud_state == WALK_DOWN:
			self.ud_state = BOTH_DOWN
			self.vy = 0

	def down_release(self):
		if self.ud_state == WALK_DOWN:
			self.ud_state = STILL
			self.vy = 0
		elif self.ud_state == BOTH_DOWN:
			self.ud_state = WALK_UP
			self.vy = 5

	def up_release(self):
		if self.ud_state == WALK_UP:
			self.ud_state = STILL
			self.vy = 0
		elif self.ud_state == BOTH_DOWN:
			self.ud_state = WALK_DOWN
			self.vy = -5






















	
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
		
