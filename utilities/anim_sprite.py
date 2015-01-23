import pyglet

class Anim_Sprite(pyglet.sprite.Sprite):

	def __init__(self,
			img, x=0, y=0,
			blend_src=pyglet.gl.GL_SRC_ALPHA,
			blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA,
			batch=None,
			group=None,
			usage='dynamic'):
		pyglet.sprite.Sprite.__init__(self, img, x, y, blend_src, blend_dest, batch, group, usage)

		self._paused = False

	def _animate(self, dt): # dt = time since last function call
		self._frame_index += 1
		if self._frame_index >= len(self._animation.frames):
			self._frame_index = 0
			self.dispatch_event('on_animation_end')
			if self._vertex_list is None:
				return # Deleted in event handler.

		frame = self._animation.frames[self._frame_index]
		self._set_texture(frame.image.get_texture())

		if frame.duration is not None:
			pyglet.clock.schedule_once(self._animate, frame.duration)
			
		else:
			self.dispatch_event('on_animation_end')

	def set_frame(self, i):
		''' Seek to the specified frame '''
		self._frame_index = min(max(i, 0), len(self._animation.frames) - 1)
		frame = self._animation.frames[self._frame_index]
		if self._paused:
			self._set_texture(frame.image.get_texture())
		else:
			self._set_texture(frame.image.get_texture())
			pyglet.clock.unschedule(self._animate)
			pyglet.clock.schedule_once(self._animate, frame.duration)

	def pause(self):
		''' pause animation playback on current image'''
		if not self._paused:
			pyglet.clock.unschedule(self._animate)
			self._paused = True

	def play(self):
		''' immediately resume animation playback with the next image '''
		if self._paused:
			self._animate(0)
			self._paused = False
		