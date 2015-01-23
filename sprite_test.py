import pyglet
from pyglet.gl import *

import game_obj

# Set up graphical window
config = Config(double_buffer=True, depth_size=0, sample_buffers=1, samples=8)

window = pyglet.window.Window(config=config, 
	#height=600, width=800, # Windowed
	fullscreen=True, # Fullscreen
	resizable=True
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
	rockstar_guy_obj.draw()
	
	counter.draw()
	
def update(dt):
	#
	# UPDATE HERE
	#
	rockstar_guy_obj.update(dt)

# Load resource
pyglet.resource.path = ['./silliness']
pyglet.resource.reindex()

rockstar_guy_img = pyglet.resource.image("rockstarguy.jpg")

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(rockstar_guy_img)

# Create game object from image
rockstar_guy_obj = game_obj.Rockstar(rockstar_guy_img, None, window.width/2, window.height/2)

pyglet.clock.schedule_interval(update, 1/120) # Game time step

#window.push_handlers()
pyglet.app.run() # Run pyglet
