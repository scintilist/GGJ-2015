import pyglet

class RoomChangeDispatcher(pyglet.event.EventDispatcher):
	def change_room(self, room_name):
		self.dispatch_event('on_room_change', room_name)

	# def on_room_change(self, room_name):
	# 	print("default handler", room_name)

RoomChangeDispatcher.register_event_type("on_room_change")
