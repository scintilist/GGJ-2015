import pyglet
from pyglet.gl import *
from pyglet.window import key

from lib import space_base

g_scale = .5
abs_width, abs_height = 1920, 1080

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	#fullscreen=True, # Fullscreen
	width = int(abs_width * g_scale),
	height = int(abs_height * g_scale),
	resizable = False,
	)
	
# Auto scale graphics to screen size
g_scale = min(window.width/abs_width, window.height/abs_height)

# Background color
glClearColor(.8,.8,.8,1)

# Enable transparency / alpha blending
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# FPS counter display
counter = pyglet.clock.ClockDisplay()

# Load resource path
pyglet.resource.path = [
		'../art',
		'../art/HubScreen',
		'../art/Backgrounds',
		'../art/KimIdelV2_',
		'../art/KimWalkV2_',
		'../art/RodmanIdel_',
		'../art/FrancoIdel_',
		'../art/MERKLE',
		'../art/Speech',
]
pyglet.resource.reindex()

# Build the entire space base
space_base = space_base.SpaceBase(abs_width, abs_height, g_scale, window)

@window.event
def on_draw():
	window.clear()
	space_base.draw()
	counter.draw()
	
def update(dt):
	space_base.update(dt)

pyglet.clock.schedule_interval(update, 1/120) # Game time step

pyglet.app.run() # Run pyglet
