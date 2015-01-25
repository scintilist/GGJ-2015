BYE = "Goodbye!"

N1 = "Oh...hey."
N2 = "That's okay; I wouldn't expect anybody to recognize little ol' me anymore."

N3 = "You again?"
N4 = "You said you hated me!"

N5 = "Hey there!"
N6 = "You said you loved me!"

K1 = "Who are you?"
K2 = "James Franco!?! What are you doing on the moon?"
K3 = "So, Franco - we meet again."
K4 = "I hate you!"
K5 = "I love you!"

K6 = "What did I say?"

LOVE_RESP = "Thank you! Aw, you're embarrassing me!"
HATE_RESP = "Well fuck you too, you Gangnam ass piece of shit!"

class RodmanDialog:
	def __init__(self, record):
		self.record = record

	def rodman_1(self):
		return (N1, {
			N1: {
				K1: (N2, "rodman_spoken_to"),
				K2: (N2, "rodman_spoken_to"),
				K3: (N2, "rodman_spoken_to"),
			},

			N2: {
				K4: (HATE_RESP, "rodman_hate"),
				K5: (LOVE_RESP, "rodman_love"),
			},

			LOVE_RESP: {
				BYE: ("", ""),
			},

			HATE_RESP: {
				BYE: ("", ""),
			},
		})

	def rodman_followup(self):
		start = N3 if self.record["choices"]["rodman_hate"] else N5
		response = N4 if self.record["choices"]["rodman_hate"] else N6

		return (start, {
			start: {
				K6: (response, ""),
			},

			response: {
				BYE: ("", ""),
			},
		})

rodman_hate_convo = (N3, {
	N3: {
		K6: (N4, ""),
	},

	N4: {
		BYE: ("", ""),
	},
})

rodman_love_convo = (N5, {
	N5: {
		K6: (N6, ""),
	},

	N6: {
		BYE: ("", ""),
	},
})

