from .game_obj import GameObj
from . import util
from .public_record import PublicRecord

STILL = 1
BOTH_DOWN = 2
WALK_LEFT = 3
WALK_RIGHT = 4
WALK_UP = 5
WALK_DOWN = 6

class Player(GameObj):
	''' Player character'''
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, record = PublicRecord(), room = None):
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, record, room)

		self.idle_right_anim = image
		self.idle_left_anim = image.get_transform(flip_x = True)

		# Create & init idle anims for room to load
		self.walk_left_anim = self.idle_left_anim
		self.walk_right_anim = self.idle_right_anim
		
		self.lr_state = STILL
		self.ud_state = STILL

		self.speed = 2
		
	def update(self, dt):
		super().update_position(dt)

		# Shrink player with perspective to center point in screen
		self.scale = 1 - self.y / self.room.height
		
		self.update_sprite()
		
	def mouse_click(self, x, y):
		# Do somthing real when you click on the player
		print('player clicked on')
	
	# Left and right movement
	def left_press(self):
		if self.lr_state == STILL:
			self.lr_state = WALK_LEFT
			self.sprite.image = self.walk_left_anim
			self.vx = -self.speed
		elif self.lr_state == WALK_RIGHT:
			self.lr_state = BOTH_DOWN
			self.sprite.image = self.idle_left_anim
			self.vx = 0

	def right_press(self):
		if self.lr_state == STILL:
			self.sprite.image = self.walk_right_anim
			self.lr_state = WALK_RIGHT
			self.vx = self.speed
		elif self.lr_state == WALK_LEFT:
			self.lr_state = BOTH_DOWN
			self.sprite.image = self.idle_right_anim
			self.vx = 0

	def left_release(self):
		if self.lr_state == WALK_LEFT:
			self.lr_state = STILL
			self.sprite.image = self.idle_left_anim
			self.vx = 0
		elif self.lr_state == BOTH_DOWN:
			self.lr_state = WALK_RIGHT
			self.sprite.anim = self.walk_right_anim
			self.vx = self.speed

	def right_release(self):
		if self.lr_state == WALK_RIGHT:
			self.lr_state = STILL
			self.sprite.image = self.idle_right_anim
			self.vx = 0
		elif self.lr_state == BOTH_DOWN:
			self.lr_state = WALK_LEFT
			self.sprite.image = self.walk_left_anim
			self.vx = -self.speed
	
	# Up and down movement
	def down_press(self):
		left = False
		if self.lr_state == WALK_LEFT or self.sprite.image == self.idle_left_anim:
			left = True
		elif self.lr_state == WALK_RIGHT or self.sprite.image == self.idle_right_anim:
			left = False

		idle = self.idle_left_anim if left else self.idle_right_anim
		walk = self.walk_left_anim if left else self.walk_right_anim

		if self.ud_state == STILL:
			self.ud_state = WALK_DOWN
			self.vy = -self.speed
			self.sprite.image = walk
		elif self.ud_state == WALK_UP:
			self.ud_state = BOTH_DOWN
			self.vy = 0
			self.sprite.image = idle

	def up_press(self):
		left = False
		if self.lr_state == WALK_LEFT or self.sprite.image == self.idle_left_anim:
			left = True
		elif self.lr_state == WALK_RIGHT or self.sprite.image == self.idle_right_anim:
			left = False

		idle = self.idle_left_anim if left else self.idle_right_anim
		walk = self.walk_left_anim if left else self.walk_right_anim

		if self.ud_state == STILL:
			self.ud_state = WALK_UP
			self.vy = self.speed
			self.sprite.image = walk
		elif self.ud_state == WALK_DOWN:
			self.ud_state = BOTH_DOWN
			self.vy = 0
			self.sprite.image = idle

	def down_release(self):
		left = False
		if self.lr_state == WALK_LEFT or self.sprite.image == self.idle_left_anim:
			left = True
		elif self.lr_state == WALK_RIGHT or self.sprite.image == self.idle_right_anim:
			left = False

		idle = self.idle_left_anim if left else self.idle_right_anim
		walk = self.walk_left_anim if left else self.walk_right_anim

		if self.ud_state == WALK_DOWN:
			self.ud_state = STILL
			self.vy = 0
			self.sprite.image = idle
		elif self.ud_state == BOTH_DOWN:
			self.ud_state = WALK_UP
			self.vy = self.speed
			self.sprite.image = walk

	def up_release(self):
		left = False
		if self.lr_state == WALK_LEFT or self.sprite.image == self.idle_left_anim:
			left = True
		elif self.lr_state == WALK_RIGHT or self.sprite.image == self.idle_right_anim:
			left = False

		idle = self.idle_left_anim if left else self.idle_right_anim
		walk = self.walk_left_anim if left else self.walk_right_anim

		if self.ud_state == WALK_UP:
			self.ud_state = STILL
			self.vy = 0
			self.sprite.image = idle
		elif self.ud_state == BOTH_DOWN:
			self.ud_state = WALK_DOWN
			self.vy = -self.speed
			self.sprite.image = walk
