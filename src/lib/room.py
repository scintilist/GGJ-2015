import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from . import roomchangedispatcher
from .public_record import PublicRecord
from .game_obj import GameObj
from .base_npc import NPC
from .player import Player

STATE_FREEMOVE = 0
STATE_DIALOG = 1

class Room:
	def __init__(self, width = 1920, height = 1080, g_scale = 1.0, window = None, record = PublicRecord(), room_name = "default_room", start_x = 50, start_y = 50):
		self.g_scale = g_scale
		self.width = width
		self.height = height
		self.window = window
		self.record = record
		self.room_name = room_name

		self.room_changer = roomchangedispatcher.RoomChangeDispatcher()
		
		self.state = STATE_FREEMOVE

		# Batches ain't shit but groups and tricks
		self.batch = pyglet.graphics.Batch()

		self.layers = []
		self.player_layer = 5

		for i in range(-self.player_layer, self.player_layer+1):
			layer = pyglet.graphics.OrderedGroup(i)
			self.layers.append(layer)

		# Push Event handlers
		self.window.push_handlers(self.on_key_press, self.on_key_release, self.on_mouse_press, self.on_mouse_release)

		# List of game_obj; everything in the room that isn't bg
		self.objects = []
		
		# Add player here, player is a game object w/ event handlers
		# player_img = util.make_animation('KimWalkV2_.png', frame_count = 90, num_digits = 5, center_x = True, loop = True, duration = 1/30)
		player_img = util.make_animation('KimIdelV2_.png', frame_count = 47, num_digits = 5, center_x = True, loop = True, duration = 1/30)
		self.player = self.add_object(Player, player_img, layer_offset = 0, x = 600, y = 50, scale = 1)
		self.player.walk_right_anim = util.make_animation('KimWalkV2_.png', frame_count = 90, num_digits = 5, center_x = True, loop = True, duration = 1/30)
		self.player.walk_left_anim = self.player.walk_right_anim.get_transform(flip_x = True)
		
		if "player_pos" in self.record[self.room_name]:
			pos = self.record[self.room_name]["player_pos"]
			self.player.x = pos[0]
			self.player.y = pos[1]
		else:
			self.player.x = start_x
			self.player.y = start_y

	def get_resources(self):
		pass
		
	def build_objects(self):
		pass

	def add_object(self, obj_type, image = None, layer_offset = 0, x = 0, y = 0, scale = 1):
		obj = obj_type(image = image, group = self.layers[self.player_layer+layer_offset], x = x, y = y, scale = scale, room = self)
		self.objects.append(obj)
		return obj
	
	def update(self, dt):
		# Room updates here
		for obj in self.objects:
			obj.room = self
			obj.update(dt)

	def cleanup(self):
		# Remove Event handlers
		self.window.remove_handlers(self.on_key_press, self.on_key_release, self.on_mouse_press)
		# Store all necessary state
		self.record[self.room_name]["player_pos"] = (self.player.x, self.player.y)
	
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
			# Unscale mouse cords
			m_x, m_y = x / self.g_scale, y / self.g_scale
			objs = self.objects_at_location(m_x, m_y)
			# Try to call in layer order, then return True when handled
			for obj in objs:
				try:
					obj.mouse_click(m_x, m_y)
					self.pressed_object = obj
					return True
				except:
					pass
		return True # The buck stops here
		
	def on_mouse_release(self, x, y, button, modifiers):
		if button == mouse.LEFT:
			# Unscale mouse cords
			m_x, m_y = x / self.g_scale, y / self.g_scale
			try:
				self.pressed_object.mouse_release(m_x, m_y)
			except:
				pass
			self.pressed_object = None
		return True # The buck stops here
		
	def is_over_object(self, obj, x, y): # Takes unscaled coordinates
		try: # Try image directly
			img = obj.sprite.image
			
			left = obj.x - img.anchor_x * obj.scale
			bottom = obj.y - img.anchor_y * obj.scale
			
			right = left + img.width * obj.scale
			top = bottom + img.height * obj.scale
		except: # Assume animation
			img = obj.sprite._animation.frames[obj.sprite._frame_index].image
			
			left = obj.x - img.anchor_x * obj.scale
			bottom = obj.y - img.anchor_y * obj.scale
			
			right = left + img.width * obj.scale
			top = bottom + img.height * obj.scale
		
		if not (x < left or x > right or y < bottom or y > top):
			s_x = (x - left) / obj.scale
			s_y = (y - bottom) / obj.scale
			alpha_val = util.get_pixel_alpha(img, int(s_x), int(s_y))
			if alpha_val > 0:
				return True
		return False
		
	def objects_at_location(self, x, y):
		'''return sorted list of objects at the real mouse x y location'''
		# Get a list of objects mouse is over
		mouse_over_objs = []
		
		for obj  in self.objects:
			try: # Try image directly
				img = obj.sprite.image
				
				left = obj.x - img.anchor_x * obj.scale
				bottom = obj.y - img.anchor_y * obj.scale
				
				right = left + img.width * obj.scale
				top = bottom + img.height * obj.scale
			except: # Assume animation
				img = obj.sprite._animation.frames[obj.sprite._frame_index].image
				
				left = obj.x - img.anchor_x * obj.scale
				bottom = obj.y - img.anchor_y * obj.scale
				
				right = left + img.width * obj.scale
				top = bottom + img.height * obj.scale
			
			if not (x < left or x > right or y < bottom or y > top):
				s_x = (x - left) / obj.scale
				s_y = (y - bottom) / obj.scale
				alpha_val = util.get_pixel_alpha(img, int(s_x), int(s_y))
				if alpha_val > 0:
					mouse_over_objs.append(obj)
		
		# Sort by layer key
		return sorted(mouse_over_objs, key = lambda x: x.sprite.group, reverse = True)
