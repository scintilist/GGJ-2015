from .game_obj import GameObj
from . import util
from .dialog_boxes import *

class NPC(GameObj):
	def __init__(self, image, group = None, x = 0, y = 0, scale = 1.0, rotation = 0, 
			visible = True, opacity = 255, room = None):
		super().__init__(image, group, x, y, scale, rotation, visible, opacity, room)
		
		self.convo = None
		self.what_im_saying = ""
		
		self.kb = []
		self.npc_dialog_box = None
			
	# EXCEPTIONS CAUGHT SILENTLY HERE BY PYGLET
	def mouse_click(self, x, y):
		self.room.set_active_npc(self)
		
	def draw_dialog(self):
		self.clear_dialog()
		# Add an NPC dialog box and three Kim dialog boxes
		self.npc_dialog_box = self.room.add_object(NPCDialog, layer_offset = 2, x = self.room.width/2, y = self.room.height/2 + 200,
			scale = 1.0, text_string = self.what_im_saying)
		i = 0
		for msg in self.convo[1][self.what_im_saying]:
			new_kb = self.room.add_object(KimDialog, layer_offset = 2, x = self.room.width/2, y = self.npc_dialog_box.y - 90*(len(self.kb)+1),
				scale = 1.0, text_string = msg)
			self.kb.append(new_kb)
			i += 1
			
	def clear_dialog(self):
		try:
			self.room.objects.remove(self.npc_dialog_box)
		except:
			pass
		self.npc_dialog_box = None
		
		for i, box in enumerate(self.kb):
			try:
				self.room.objects.remove(box)
			except:
				pass
		self.kb = []

	def start_conversation(self):
		self.what_im_saying = self.convo[0]
		self.draw_dialog()
			
	def box_clicked(self, text):
			
		my_current = self.convo[1][self.what_im_saying]
		my_response = my_current[text][0]
		record_choice = my_current[text][1]
		
		if record_choice and record_choice != "":
			# Put Kim's choice in the public record
			self.record["choices"][record_choice] = True
		if my_response == "":
			self.clear_dialog()
			self.room.end_dialog()
		else:
			self.what_im_saying = my_response
			self.draw_dialog()
