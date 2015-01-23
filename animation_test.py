import pyglet
from pyglet.gl import *

import game_obj
from utilities import util

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
	animated_sprite_obj.draw()
	
	counter.draw()
	
def update(dt):
	#
	# UPDATE HERE
	#
	animated_sprite_obj.update(dt)

# Load resources
pyglet.resource.path = ['./art']
pyglet.resource.reindex()

frame_list = util.get_frame_list('sprite.png', frame_count = 3, num_digits = 2, center = True)
animated_sprite = pyglet.image.Animation.from_image_sequence(frame_list, .5, loop=True)

# Create game object from sprite
animated_sprite_obj = game_obj.Game_Obj(animated_sprite, window.width/2, window.height/2)

pyglet.clock.schedule_interval(update, 1/120) # Game time step


def first(dt):
	animated_sprite_obj.sprite.pause()

def second(dt):
	animated_sprite_obj.sprite.set_frame(0)
	
def third(dt):
	animated_sprite_obj.sprite.play()

pyglet.clock.schedule_once(first, 1)
pyglet.clock.schedule_once(second, 2)
pyglet.clock.schedule_once(third, 5)

#window.push_handlers()
pyglet.app.run() # Run pyglet