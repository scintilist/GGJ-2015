BYE = "Thank you."

GREET1 = "I am Angela Merkel."

class MerkelDialog:
	def __init__(self, record):
		self.record = record

	def merkel_1(self):
		return (GREET1, {
			GREET1: {
				BYE: ("", ""),
			},
		})
