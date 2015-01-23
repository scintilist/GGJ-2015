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
	
	game_batch.draw()
	
	#for obj in objs:
	#	obj.draw()
	
	
	counter.draw()
	
def update(dt):
	#
	# UPDATE HERE
	#
	for obj in objs:
		obj.update(dt)

# Create main grpahics batch
game_batch = pyglet.graphics.Batch()
				
# Load resources
pyglet.resource.path = ['./art']
pyglet.resource.reindex()

frame_list = util.get_frame_list('num.png', frame_count = 9, num_digits = 2, center = True)
nums_sprite = pyglet.image.Animation.from_image_sequence(frame_list, .2, loop=True)

# Create list of game objects from sprite
objs = []
for x in range(100, window.width, 150):
	for y in range(100, window.height, 150):
		objs.append(game_obj.Spinning_Nums(nums_sprite, batch = game_batch, x = x, y = y))

pyglet.clock.schedule_interval(update, 1/120) # Game time step

i = 0

def pause(dt):
	global i
	if i < len(objs):
		objs[i].sprite.pause()
		objs[i].sprite.visible = False
		i += 1
	else:
		pyglet.clock.unschedule(pause)
		i = 0
		pyglet.clock.schedule_interval(play, .05) # Pause 1 sprite per cycle
		
def play(dt):
	global i
	if i < len(objs):
		objs[i].sprite.play()
		objs[i].sprite.visible = True
		i += 1
	else:
		pyglet.clock.unschedule(play)
		i = 0
		pyglet.clock.schedule_interval(pause, .05) # Pause 1 sprite per cycle
		
#pyglet.clock.schedule_interval(pause, .05) # Pause 1 sprite per cycle

#window.push_handlers()
pyglet.app.run() # Run pyglet