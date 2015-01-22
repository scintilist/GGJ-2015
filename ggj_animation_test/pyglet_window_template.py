import pyglet
from pyglet.gl import *

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	height=800, width=600, # Windowed
	fullscreen=True, # Fullscreen
	#resizable=True
	)

# Background color
glClearColor(.8,.8,.8,1)

# Enable transparency / alpha blending
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# FPS counter display
counter = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
	window.clear()
	
	#
	# DRAW GRAPHICS HERE
	#
	
	counter.draw()
	
def update(realtime_dt):

	#
	# RUN GAME UPDATE LOOP HERE
	#
	
	pass

#
# Initialize game environment here
#

pyglet.clock.schedule_interval(update, 1/120) # Game time step

window.push_handlers(event_handlers.EventHandlers())
pyglet.app.run() # Run pyglet