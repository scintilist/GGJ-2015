BYE = "Goodbye!"

N1 = "Hey there, little man!"
K1 = "Dennis! My main man! How did you get up here?!"
K2 = "Oh, great. How did you get into my nation?"

N2_HAPPY = "Y'know, I don't really know, myself! I was chillin' in Pyongyang and some guys just pushed me on a rocket."
N2_SAD = "Aw, I'm sorry, dude. I thought you might've wanted me here. Not like I can go back now, though."

HELP_1 = "My people are suffering, Dennis. We are alone and confused. We need purpose."
HELP_2 = "Tiny Kim's on my ass about all the people who came up here. Do something."

class RodmanDialog:
	def __init__(self, record):
		self.record = record

	def rodman_1(self):
		return (N1, {
			N1: {
				K1: (N2_HAPPY, "rodman_spoken_to"),
				K2: (N2_SAD, "rodman_spoken_to"),
			},

			N2_SAD: {
				HELP_1: ("", ""),
				HELP_2: ("", ""),
			},
			N2_HAPPY: {
				HELP_1: ("", ""),
				HELP_2: ("", ""),
			},
		})

	'''def rodman_followup(self):
		start = N3 if self.record["choices"]["rodman_hate"] else N5
		response = N4 if self.record["choices"]["rodman_hate"] else N6

		return (start, {
			start: {
				K6: (response, ""),
			},

			response: {
				BYE: ("", ""),
			},
		})'''

