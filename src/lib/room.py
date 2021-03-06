import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from .player import Player
from .dialog_boxes import *

import gc
import traceback
import sys

class Room:
	def __init__(self, space_base = None, room_name = 'default_room', start_x = 50, start_y = 50):
		self.space_base = space_base
		
		self.g_scale = space_base.g_scale
		self.width = space_base.abs_width
		self.height = space_base.abs_height
		self.window = space_base.window
		self.record = space_base.record
		self.room_name = room_name

		self.active_npc = None

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
		self.player = self.add_object(Player, layer_offset = 0, x = 600, y = 50, scale = 1)
		
		if "player_pos" in self.record[self.room_name]:
			pos = self.record[self.room_name]["player_pos"]
			self.player.x = pos[0]
			self.player.y = pos[1]
		else:
			self.player.x = start_x
			self.player.y = start_y
		
	def build_objects(self):
		pass

	def add_object(self, obj_type, image = None, layer_offset = 0, x = 0, y = 0, scale = 1, **kwargs):
		obj = obj_type(image = image, group = self.layers[self.player_layer+layer_offset], x = x, y = y, scale = scale, room = self, **kwargs)
		self.objects.append(obj)
		return obj
	
	def set_active_npc(self, new_active_npc):
		if new_active_npc is not self.active_npc:
			try:
				self.active_npc.clear_dialog()
			except:
				pass
			self.active_npc = new_active_npc
			self.active_npc.start_conversation()
			self.player.freeze()
			
	def end_dialog(self):
		self.active_npc = None
		self.player.unfreeze()
	
	def update(self, dt):
		# Room updates here
		for obj in self.objects:
			obj.room = self
			obj.update(dt)

	def cleanup(self):
		"""
		print('All referrers to the player sprite')
		refs = gc.get_referrers(self.player.sprite)
		for referrer in refs:
			print(type(referrer), '\n', referrer, '\n')
		"""
		# Try to remove references to self from all objects
		for obj in self.objects:
			try:
				obj.sprite.delete()
			except:
				print('SPRITE NOT DELETED')
				exc_type, exc_value, exc_traceback = sys.exc_info()
				if exc_type:
					traceback.print_exception(exc_type, exc_value, exc_traceback)
					sys.exit()
			if type(obj) is Player:
				try:
					obj.room = None
					print(obj)
				except:
					pass
		# Remove Event handlers
		self.window.remove_handlers(self.on_key_press, self.on_key_release, self.on_mouse_press, self.on_mouse_release)
		# Store all necessary state
		self.record[self.room_name]["player_pos"] = (self.player.x, self.player.y)
	
	# EVENT HANDLERS
	# Keyboard
	def on_key_press(self, symbol, modifier):
		if symbol == key.A:
				self.player.left_press()
		elif symbol == key.D:
				self.player.right_press()			
		elif symbol == key.W:
				self.player.up_press()
		elif symbol == key.S:
				self.player.down_press()
		elif symbol == key.ESCAPE:
			self.space_base.change_room("menu")
			return True
		return True # The buck stops here
		
	def on_key_release(self, symbol, modifier):
		if symbol == key.A:
				self.player.left_release()
		elif symbol == key.D:
				self.player.right_release()		
		elif symbol == key.W:
				self.player.up_release()
		elif symbol == key.S:
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
					obj.mouse_press(m_x, m_y)
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
		s1 = sorted(mouse_over_objs, key = lambda x: x.sprite.group, reverse = True)
		return sorted(s1, key = lambda x: x.visible, reverse = True)
		
