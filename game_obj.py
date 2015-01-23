from utilities import anim_sprite

class Game_Obj():
	''' Some game object containing a sprite, draw method, and things to do on update'''
	def __init__(self, image, x = 400, y = 300):
		self.sprite = anim_sprite.Anim_Sprite(image)

		# Scale and rotation
		self.scale = 1
		self.rot = 0
		
		# Coordinates
		self.x = x
		self.y = y
		
	def update(self, dt):
			pass
		
	def draw(self):
		# TODO:
		# Fix this so rotation, scale, and x/y are only done when changed
		# These are expensive updates
		self.sprite.rotation = self.rot
		self.sprite.scale = self.scale
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.sprite.draw()
	
class Rockstar(Game_Obj):
	''' Performs a sweet animated transform on the sprite contained within'''
	def __init__(self, image, x = 400, y = 300):
		super().__init__(image, x, y)

		self.scale_v = .1
		self.rot_v = 4
		
	def update(self, dt):
		self.scale += self.scale_v
		self.rot += self.rot_v

		if self.scale < .3 or self.scale > 2:
			self.scale_v *= -1
			self.rot_v *= -1