from . import anim_sprite

from .game_obj import GameObj
from . import util

STILL = 1
BOTH_DOWN = 2
WALK_LEFT = 3
WALK_RIGHT = 4
WALK_UP = 5
WALK_DOWN = 6

class Player(GameObj):
	''' Player character'''
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.kim_idle_right = util.make_animation('KimIdelV2_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		room.kim_idle_left = room.kim_idle_right.get_transform(flip_x = True)
		room.kim_walk_right = util.make_animation('KimWalkV2_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		room.kim_walk_left = room.kim_walk_right.get_transform(flip_x = True)
		super().__init__(room.kim_idle_right, group, x, y, scale, rotation, visible, opacity, room)

		# Push the animation end event handler to the sprite
		self.sprite.push_handlers(self.on_animation_end)
		
		# Set the image to transition to on animation completion
		self.next_image = room.kim_idle_right
		
		self.lr_state = STILL
		self.ud_state = STILL

		self.speed = 2
		self.frozen = False
		
	def update(self, dt):
		super().update_position(dt)

		# Shrink player with perspective to center point in screen
		self.scale = 1 - self.y / self.room.height
		
		self.update_sprite()
		
	def mouse_click(self, x, y):
		# Do somthing real when you click on the player
		print('player clicked on')
	
	def on_animation_end(self):
		self.sprite.image = self.next_image
		
	def set_image_now(self, new_image):
		'''Set the image and set frame to 0 if different'''
		if self.sprite.image is not new_image:
			self.sprite.image = new_image
			self.sprite.set_frame(0)
		self.next_image = new_image
		
	def freeze(self):
		self.frozen = True
		self.vx = 0
		self.vy = 0
		if self.lr_state == WALK_LEFT:
			self.next_image = self.room.kim_idle_left
		elif self.lr_state == WALK_RIGHT:
			self.next_image = self.room.kim_idle_right
	
	def unfreeze(self):
		self.frozen = False
		self.enter_lr_state(self.lr_state)
		self.enter_ud_state(self.ud_state)
	
	# Left and right movement
	def enter_lr_state(self, state):
		if not self.frozen:
			if state == WALK_LEFT:
				self.vx = -self.speed
				self.set_image_now(self.room.kim_walk_left)
			elif state == WALK_RIGHT:
				self.vx = self.speed
				self.set_image_now(self.room.kim_walk_right)
			elif state == STILL or state == BOTH_DOWN:
				self.vx = 0
				if self.lr_state == WALK_LEFT:
					self.next_image = self.room.kim_idle_left
				elif self.lr_state == WALK_RIGHT:
					self.next_image = self.room.kim_idle_right
		self.lr_state = state

	def left_press(self):
		if self.lr_state == STILL:
			self.enter_lr_state(WALK_LEFT)
		elif self.lr_state == WALK_RIGHT:
			self.enter_lr_state(BOTH_DOWN)
	def right_press(self):
		if self.lr_state == STILL:
			self.enter_lr_state(WALK_RIGHT)
		elif self.lr_state == WALK_LEFT:
			self.enter_lr_state(BOTH_DOWN)
	def left_release(self):
		if self.lr_state == WALK_LEFT:
			self.enter_lr_state(STILL)
		elif self.lr_state == BOTH_DOWN:
			self.enter_lr_state(WALK_RIGHT)
	def right_release(self):
		if self.lr_state == WALK_RIGHT:
			self.enter_lr_state(STILL)
		elif self.lr_state == BOTH_DOWN:
			self.enter_lr_state(WALK_LEFT)
	
	# Up and down movement
	def enter_ud_state(self, state):
		if not self.frozen:
			if state == WALK_UP:
				self.vy = self.speed
			elif state == WALK_DOWN:
				self.vy = -self.speed
			elif state == STILL or state == BOTH_DOWN:
				self.vy = 0
		self.ud_state = state
		
	def down_press(self):
		if self.ud_state == STILL:
			self.enter_ud_state(WALK_DOWN)
		elif self.ud_state == WALK_UP:
			self.enter_ud_state(BOTH_DOWN)
	def up_press(self):
		if self.ud_state == STILL:
			self.enter_ud_state(WALK_UP)
		elif self.ud_state == WALK_DOWN:
			self.enter_ud_state(BOTH_DOWN)
	def down_release(self):
		if self.ud_state == WALK_DOWN:
			self.enter_ud_state(STILL)
		elif self.ud_state == BOTH_DOWN:
			self.enter_ud_state(WALK_UP)
	def up_release(self):
		if self.ud_state == WALK_UP:
			self.enter_ud_state(STILL)
		elif self.ud_state == BOTH_DOWN:
			self.enter_ud_state(WALK_DOWN)
