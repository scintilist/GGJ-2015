import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from . import game_obj
from . import roomchangedispatcher
from .public_record import PublicRecord

STATE_FREEMOVE = 0
STATE_DIALOG = 1

class Room:
	def __init__(self, width = 1920, height = 1080, g_scale = 1.0, window = None, public_record = PublicRecord()):
		self.g_scale = g_scale
		self.width = width
		self.height = height
		self.window = window

		self.public_record = public_record

		self.room_changer = roomchangedispatcher.RoomChangeDispatcher()
		
		self.state = STATE_FREEMOVE
		
		# Player is a game object w/ event handlers
		player_img = util.make_animation('KimWalk_.png', frame_count = 90, num_digits = 5, center = True, loop = True, duration = .02)
		self.player = game_obj.Player(player_img, None, x = 100, y = 50, g_scale = g_scale)

		# Batches ain't shit but groups and tricks
		self.batch = pyglet.graphics.Batch()

		self.layers = []
		self.player_layer = 5

		for i in range(-self.player_layer, self.player_layer+1):
			layer = pyglet.graphics.OrderedGroup(i)
			self.layers.append(layer)

		'''self.player.sprite.batch = self.batch
		self.player.sprite.group = self.layers[self.player_layer]'''

		self.bottom_left = util.Point(0, 0)
		self.top_right = util.Point(width, height)

		# List of game_obj; everything in the room that isn't bg
		self.objects = [self.player]
		
		# Event handlers
		self.window.push_handlers(self.on_key_press, self.on_key_release, self.on_mouse_press)

		# Set player to be rendered here
		self.player.sprite.batch = self.batch
		self.player.sprite.group = self.layers[self.player_layer]

		# Do we need this? Maybe do this if it's slow to load
		'''for obj in objects:
			try:
				obj.sprite.set_frame(0)
			except:
				print("caught OK")
				pass'''

	def get_resources(self):
		pass
		
	def build_objects(self):
		pass
		
	def update(self, dt):
		# Room updates here
		
		for obj in self.objects:
			obj.update(dt)
	
	# EVENT HANDLERS
	# Keyboard
	def on_key_press(self, symbol, modifier):
		if symbol == key.A:
			if self.state == STATE_FREEMOVE:
				self.player.left_press()
		
		elif symbol == key.D:
			if self.state == STATE_FREEMOVE:
				self.player.right_press()
				
		elif symbol == key.W:
			if self.state == STATE_FREEMOVE:
				self.player.up_press()
				
		elif symbol == key.S:
			if self.state == STATE_FREEMOVE:
				self.player.down_press()

		elif symbol == key._1:
			self.room_changer.change_room("maddie")

		elif symbol == key._2:
			self.room_changer.change_room("rockstar")
		
		elif symbol == key.ESCAPE:
			pyglet.app.exit()
			
		return True # The buck stops here
		
	def on_key_release(self, symbol, modifier):
		if symbol == key.A:
			if self.state == STATE_FREEMOVE:
				self.player.left_release()
		
		elif symbol == key.D:
			if self.state == STATE_FREEMOVE:
				self.player.right_release()
				
		elif symbol == key.W:
			if self.state == STATE_FREEMOVE:
				self.player.up_release()
				
		elif symbol == key.S:
			if self.state == STATE_FREEMOVE:
				self.player.down_release()
				
		return True # The buck stops here
		
	# Mouse
	def on_mouse_press(self, x, y, button, modifiers):
		if button == mouse.LEFT:
			# Get a list of objects mouse is over

			# Unscaled mouse cords
			m_x = x / self.g_scale
			m_y = y / self.g_scale
			
			mouse_over_objs = []
			
			for obj  in self.objects:
				try: # Try image directly
					img = obj.sprite.image
					
					left = obj.x - img.anchor_x
					bottom = obj.y - img.anchor_y
					
					right = obj.x - img.anchor_x + img.width
					top = obj.y - img.anchor_y + img.height
				except: # Assume animation
					img = obj.sprite._animation.frames[obj.sprite._frame_index].image
					
					left = obj.x - img.anchor_x
					bottom = obj.y - img.anchor_y
					
					right = obj.x - img.anchor_x + img.width
					top = obj.y - img.anchor_y + img.height
				
				if not (m_x < left or m_x > right or m_y < bottom or m_y > top):
					x = m_x - left
					y = m_y - bottom
					alpha_val = util.get_pixel_alpha(img, int(x), int(y))
					if alpha_val > 0:
						mouse_over_objs.append(obj)
			
			# Sort by layer key
			mouse_over_objs.sort(key = lambda x: x.sprite.group, reverse = True)
			
			# Try to call in layer order, then return True
			for obj in mouse_over_objs:
				try:
					obj.mouse_click(m_x, m_y)
					return True
				except:
					pass
					
		return True # The buck stops here

		
		
		
		
		
		
		
		
#	
# TEST ROOMS PLEASE IGNORE		
#		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

		
		
		
		
class GameRoom(Room):
	def __init__(self, width, height, g_scale = 1.0, window = None, public_record = PublicRecord()):
		super().__init__(width, height, g_scale, window, public_record)
		
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

class TestRoom(Room):
	def __init__(self, width, height, g_scale = 1.0, window = None, public_record = PublicRecord()):
		super().__init__(width, height, g_scale, window, public_record)

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

			
	
