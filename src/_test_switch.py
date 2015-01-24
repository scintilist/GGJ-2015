import pyglet
from pyglet.gl import *
from pyglet.window import key

from lib import game_obj
from lib import util
from lib import room
from lib import placeholder_room
from lib import roomchangedispatcher

global_scale = .5
abs_width, abs_height = 1920, 1080

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	#fullscreen=True, # Fullscreen
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

# Register new event handlers
# roomchangedispatcher.RoomChangeDispatcher.register_event_type('on_room_change')
window.register_event_type('on_room_change')

# Load resources
pyglet.resource.path = ['../art']
pyglet.resource.reindex()

player_img = pyglet.resource.image("num01.png")
player = game_obj.Player(player_img, None, x = 50, y = 50, g_scale = global_scale)

active_room_idx = 0
active_room = None

# r = room.GameRoom(abs_width, abs_height, player, g_scale = global_scale, window = window)
# r2 = placeholder_room.PlaceholderRoom(abs_width, abs_height, player, g_scale = global_scale, window = window)

# active_room.activate_room()

# rooms = [r, r2]
rooms = {
	"rockstar": room.GameRoom,
	"maddie":   placeholder_room.PlaceholderRoom,
}

active_room = rooms["rockstar"](abs_width, abs_height, player, g_scale = global_scale, window = window)

# Set up room switch handle
def on_room_change(self, room_name):
	print("hey")
	global rooms
	global active_room

	if room_name in rooms:
		active_room = rooms[room_name](abs_width, abs_height, player, g_scale = global_scale, window = window)
		player.x = 50
		player.y = 50
# window.push_handlers(on_room_change)
roomchangedispatcher.RoomChangeDispatcher.on_room_change = on_room_change


# Must do this after room creation to hit top of stack
# window.push_handlers(on_key_press)

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

#window.push_handlers()
pyglet.app.run() # Run pyglet
