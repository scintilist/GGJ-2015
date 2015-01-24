import pyglet
from pyglet.gl import *
from pyglet.window import key

from . import util
from . import game_obj

STATE_FREEMOVE = 0
STATE_DIALOG = 1

class Room:
	
	def __init__(self, width = 1920, height = 1080, player = None, g_scale = 1.0, window = None):
		self.g_scale = g_scale
		self.width = width
		self.height = height
		self.window = window
		
		self.state = STATE_FREEMOVE
		
		# Player is a game object w/ event handlers
		self.player = player

		# Batches ain't shit but groups and tricks
		self.batch = pyglet.graphics.Batch()

		self.layers = []
		self.player_layer = 5

		for i in range(-self.player_layer, self.player_layer+1):
			layer = pyglet.graphics.OrderedGroup(i)
			self.layers.append(layer)

		self.player.sprite.batch = self.batch
		self.player.sprite.group = self.layers[self.player_layer]

		self.bottom_left = util.Point(0, 0)
		self.top_right = util.Point(width, height)

		# List of game_obj; everything in the room that isn't player or bg
		self.objects = [player]
		
	def get_resources(self):
		pass
		
	def build_objects(self):
		pass
		
	def update(self, dt):
		# Room updates here
		
		for obj in self.objects:
			obj.update(dt)
			
			
class GameRoom(Room):
	def __init__(self, width, height, player, g_scale = 1.0, window = None):
		super().__init__(width, height, player, g_scale, window)
		
		self.window.push_handlers(self.on_key_press, self.on_key_release)
		
		# Get background from file
		bg_img = pyglet.resource.image("rockstarguy.jpg")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale
		
		self.get_resources()
		self.build_objects()
		
	def get_resources(self):
		# Create animation from file
		self.nums_animation = util.make_animation('num.png', frame_count = 9, num_digits = 2, center = True, loop = True, duration = .2)
		
	def build_objects(self):
		# Create animated room object from animation
		self.objects.append(game_obj.Game_Obj(self.nums_animation, batch = self.batch, group = self.layers[1], 
			x = self.width/2, y = self.height/2, g_scale = self.g_scale, scale = 2))
			
	# EVENT HANDLERS		
	def on_key_press(self, symbol, modifier):
		if symbol == key.LEFT:
			if self.state == STATE_FREEMOVE:
				self.player.left_press()
		
		elif symbol == key.RIGHT:
			if self.state == STATE_FREEMOVE:
				self.player.right_press()
				
		elif symbol == key.UP:
			if self.state == STATE_FREEMOVE:
				self.player.up_press()
				
		elif symbol == key.DOWN:
			if self.state == STATE_FREEMOVE:
				self.player.down_press()
				
		return True # The buck stops here
		
	def on_key_release(self, symbol, modifier):
		if symbol == key.LEFT:
			if self.state == STATE_FREEMOVE:
				self.player.left_release()
		
		elif symbol == key.RIGHT:
			if self.state == STATE_FREEMOVE:
				self.player.right_release()
				
		elif symbol == key.UP:
			if self.state == STATE_FREEMOVE:
				self.player.up_release()
				
		elif symbol == key.DOWN:
			if self.state == STATE_FREEMOVE:
				self.player.down_release()
				
		return True # The buck stops here
	

class TestRoom(Room):
	def __init__(self, width, height, player, g_scale = 1.0, window = None):
		super().__init__(width, height, player, g_scale, window)

		# Get background from file
		bg_img = pyglet.resource.image("rockstarguy.jpg")
		self.bg_sprite = pyglet.sprite.Sprite(bg_img, x = 0, y = 0, batch = self.batch, group = self.layers[0])
		self.bg_sprite.scale = self.g_scale

		# fg_img = pyglet.resource.image("rockstarguy.jpg")
		# self.fg_sprite = pyglet.sprite.Sprite(fg_img, x = 0, y = 0, batch = self.batch, group = self.layers[-1])
		# self.fg_sprite.scale = self.g_scale
		
		self.get_resources()
		self.build_objects()
		
	def get_resources(self):
		# Create animation from file
		self.nums_animation = util.make_animation('num.png', frame_count = 9, num_digits = 2, center = True, loop = True, duration = .2)
		
	def build_objects(self):
		# Create animated room object from animation
		self.objects.append(game_obj.Game_Obj(self.nums_animation, batch = self.batch, group = self.layers[1], 
			x = self.width/2, y = self.height/2, g_scale = self.g_scale, scale = 2))

			
	