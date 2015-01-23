from utilities import anim_sprite

class Game_Obj():
	''' Some game object containing a sprite, draw method, and things to do on update'''
	def __init__(self, image, batch = None, x = 400, y = 300):
		self.sprite = anim_sprite.Anim_Sprite(image, x, y, batch = batch)
		
		# image or animation contained, can be changed at any time
		#self.sprite.image = None

		# Scale as a multiplier and rotation in degrees
		self.sprite.rotation = 0
		self.sprite.scale = 1
		
		# Coordinates: cartesian pixels
		self.sprite.x = x
		self.sprite.y = y
		
		# Visibility: True/False
		self.sprite.visible = True
		
		# Opacity: range 0 - 255
		self.sprite.opacity = 255
		
	def update(self, dt):
			pass
		
	def draw(self):
		# Only call this method if the sprite is not part of a batch already
		self.sprite.draw()
	
class Rockstar(Game_Obj):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, x = 400, y = 300):
		super().__init__(image, batch, x, y)

		self.scale_v = .1
		self.rot_v = 4
		
		self.scale_max = 2
		self.scale_min = .3
		
	def update(self, dt):
		self.sprite.scale += self.scale_v
		self.sprite.rotation += self.rot_v

		if self.sprite.scale < self.scale_min or self.sprite.scale > self.scale_max:
			self.scale_v *= -1
			self.rot_v *= -1
			
class Spinning_Nums(Rockstar):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, batch = None, x = 400, y = 300):
		super().__init__(image, batch, x, y)
		
		self.scale_v = .03
		self.rot_v = 2
		
		self.scale_max = 2
		self.scale_min = -2
		
		self.sprite.rotation = 0
		self.sprite.scale = 0

		self.sprite.opacity = 128