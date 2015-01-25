import pyglet

class RoomChangeDispatcher(pyglet.event.EventDispatcher):
	def change_room(self, room_name):
		self.dispatch_event('on_room_change', room_name)

RoomChangeDispatcher.register_event_type("on_room_change")
