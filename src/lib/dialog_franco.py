BYE = "Goodbye!"

N1 = "Oh...hey."
N2 = "That's okay; I wouldn't expect anybody to recognize little ol' me anymore."

N3 = "You again?"
N4 = "You said you hated me!"

N5 = "Hey there!"
N6 = "You said you loved me!"

K1 = "Who are you?"
K2 = "James Franco!?! What are you doing on the moon?"
K4 = "I hate you!"
K5 = "I love you!"

K6 = "What did I say?"

LOVE_RESP = "Thank you! Aw, you're embarrassing me!"
HATE_RESP = "Well fuck you too, you Gangnam ass piece of shit!"

WHY_MOON = "Why are you on the moon?"
SETH_DIED = "It's just that...Seth was killed by the meteors. I miss him so much. I had nowhere else to go."

SORRY = "I'm so sorry, sir! I am Kim Jong Un. Who might you be?"
ITS_OKAY = "That's alright. I'm just kiddin' around. I'm James Franco."

PROPOSE = "Maybe...maybe I could be your new Seth."
PROPOSE_ACCEPT = "You have a way with words, my short, pudgy, Asian friend. Stop by my cabin later tonight."

SEE_YOU_TONIGHT = "See you tonight, Kim!"
BUSY = "Sorry, Kim, I'm a little busy right now. See you around?"


class FrancoDialog:
	def __init__(self, record):
		self.record = record

	def franco_1(self):
		return (N1, {
			N1: {
				K1: (N2, "franco_spoken_to"),
				K2: (SETH_DIED, "franco_spoken_to"),
			},

			N2: {
				SORRY: (ITS_OKAY, ""),
				BYE: ("", ""),
			},

			ITS_OKAY: {
				WHY_MOON: (SETH_DIED, ""),
				BYE: ("", ""),
			},

			SETH_DIED: {
				PROPOSE: (PROPOSE_ACCEPT, "franco_romance"),
				BYE: ("", ""),
			},

			PROPOSE_ACCEPT: {
				BYE: ("", ""),
			},
		})

	def franco_followup(self):
		start = SEE_YOU_TONIGHT if "franco_romance" in self.record["choices"] else BUSY

		return (start, {
			start: {
				BYE: ("", ""),
			},
		})

