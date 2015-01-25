from .game_obj import GameObj
from . import util
from .dialog_data import rodman_1

class Rodman(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		# Get object initial image
		room.rodman_idle = util.make_animation('RodmanIdel_.png', num_digits = 5, center_x = True, loop = True, duration = 1/30)
		image = room.rodman_idle
		
		self.convo = rodman_1
		
		self.what_im_saying = ""
		
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
	
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_click(self, x, y):
		self.room.set_active_npc(self)

	def start_conversation(self):
		self.room.npc_dialog_box.show()
		self.room.npc_dialog_box.set_text_string(self.convo[0])
		self.what_im_saying = self.convo[0]
		
		i = 0
		for msg in self.convo[1][self.what_im_saying]:
			print(msg)
			kb = self.room.kim_boxes[i]
			kb.show()
			kb.set_text_string(msg)
			i += 1
			
	def box_clicked(self, text):
		# Hide dialog options
		for kb in self.room.kim_boxes:
			kb.hide()
			
		my_current = self.convo[1][self.what_im_saying]
		my_response = my_current[text][0]
		
		if my_response == "":
			# End the dialog
			self.room.npc_dialog_box.hide()
			self.room.active_npc = None
		else:
			i = 0
			for msg in self.convo[1][my_response]:
				print(msg)
				kb = self.room.kim_boxes[i]
				kb.show()
				kb.set_text_string(msg)
				i += 1
			
			self.what_im_saying = my_response
			self.room.npc_dialog_box.set_text_string(my_response)