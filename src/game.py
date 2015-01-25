import pyglet
from pyglet.gl import *
from pyglet.window import key

from lib import placeholder_room
from lib import menu_room
from lib import roomchangedispatcher
from lib import public_record

global_scale = .5
abs_width, abs_height = 1920, 1080

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	# fullscreen=True, # Fullscreen
	width = int(abs_width * global_scale),
	height = int(abs_height * global_scale),
	resizable = False,
	)
	
# Auto scale graphics to screen size
global_scale = min(window.width/abs_width, window.height/abs_height)

# Background color
glClearColor(.8,.8,.8,1)

# Enable transparency / alpha blending
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# FPS counter display
counter = pyglet.clock.ClockDisplay()

# Load resources
pyglet.resource.path = [
		'../art',
		'../art/HubScreen',
		'../art/Backgrounds',
		'../art/KimIdelV2_',
		'../art/KimWalkV2_',
		'../art/dialog',
]

pyglet.resource.reindex()

record = public_record.PublicRecord()

rooms = {
	"menu": menu_room.MenuRoom,
	"placeholder": placeholder_room.PlaceholderRoom,
}

active_room = rooms["menu"](abs_width, abs_height, g_scale = global_scale, window = window, record = record)

# Set up room switch handle
def on_room_change(self, room_name):
	global rooms
	global active_room

	if room_name in rooms:
		active_room.cleanup()
		active_room = rooms[room_name](abs_width, abs_height, g_scale = global_scale, window = window, record = record)
roomchangedispatcher.RoomChangeDispatcher.on_room_change = on_room_change

@window.event
def on_draw():
	window.clear()
	
	if active_room is not None:
		active_room.batch.draw()
	
	counter.draw()
	
def update(dt):
	
	if active_room is not None:
		active_room.update(dt)

pyglet.clock.schedule_interval(update, 1/120) # Game time step

pyglet.app.run() # Run pyglet
