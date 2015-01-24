import pyglet
from pyglet.gl import *

from lib import game_obj
from lib import util
from lib import room

global_scale = 0.2

(abs_width, abs_height) = (1920, 1080)

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	# fullscreen=True, # Fullscreen
	width = int(abs_width * global_scale),
	height = int(abs_height * global_scale),
	resizable = False,
	)

# Background color
glClearColor(.8,.8,.8,1)

# Enable transparency / alpha blending
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# FPS counter display
counter = pyglet.clock.ClockDisplay()

# Load resources
pyglet.resource.path = ['../art']
pyglet.resource.reindex()

rooms = []
active_room = None
player_img = pyglet.resource.image("num01.png")
player = game_obj.Player(player_img, None, x = 50, y = 50, g_scale = global_scale)

r = room.GameRoom(abs_width, abs_height, player, g_scale = global_scale, window = window)

rooms.append(r)
active_room = r

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
