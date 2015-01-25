BYE = "Later!"
CONT = "<Let Tiny Kim continue>"

TK_GREET = "Hello, Big Kim!"
GREET_R1 = "Hello, Tiny Kim!"
GREET_R2 = "Get away from me, you little freak."

TK_INFO1_SAD = "I can see we won't be getting along. Still, you need some info."
TK_INFO1_HAPPY = "Hey, I've got a status update for you on the status of Space Korea."

TK_INFO2 = "It's been four days since the meteors hit back home. Our people are starting to get a little restless."
TK_INFO3 = "They don't know what to do with this new home. There are barely any jobs to occupy them. Even the work camps are a little lax."
TK_INFO4 = "Dennis Rodman came with us, as well. Maybe you could consult with him on matters of morale. He's in the room to the right."
TK_INFO5 = "What do we do now, Big Supreme Leader?"

BYE_CONFIDENT = "I'll take care of this."
BYE_APPREHENSIVE = "I'm not really sure, myself...."

REMINDER = "Remember, Rodman is to the right."
REMINDER_OK = "Got it."

PR_START = "Have you talked to Dennis Rodman yet?"

PR_YES_NICE = "Yeah! Really nice guy, D-Rod!"
PR_YES_RUDE = "Yeah; fuck that guy."

PR_1 = "Well, hopefully whatever you said will convince him to help us restore morale."
PR_2 = "Lots of people still need food, and the moon rocks we're giving them don't actually have any protein."
# PR_3 = "You should look around the station to find ways to help."
PR_3 = "Unfortunately, the game isn't programmed past this point. Bye!"

class TinyKimDialog:
	def __init__(self, record):
		self.record = record

	def info1(self):
		return (TK_GREET, {
			TK_GREET: {
				GREET_R1: (TK_INFO1_HAPPY, ""),
				GREET_R2: (TK_INFO1_SAD, ""),
			},

			TK_INFO1_SAD: {
				CONT: (TK_INFO2, ""),
			},

			TK_INFO1_HAPPY: {
				CONT: (TK_INFO2, ""),
			},

			TK_INFO2: {
				CONT: (TK_INFO3, ""),
			},

			TK_INFO3: {
				CONT: (TK_INFO4, ""),
			},

			TK_INFO4: {
				CONT: (TK_INFO5, ""),
			},

			TK_INFO5: {
				BYE_CONFIDENT: ("", "tinykim_info_done"),
				BYE_APPREHENSIVE: ("", "tinykim_info_done"),
			},
		})

	def nag(self):
		return (REMINDER, {
			REMINDER: {
				REMINDER_OK: ("", ""),
			}
		})

	def post_rodman(self):
		return (PR_START, {
			PR_START: {
				PR_YES_NICE: (PR_1, ""),
				PR_YES_RUDE: (PR_1, ""),
			},

			PR_1: {
				CONT: (PR_2, ""),
			},

			PR_2: {
				CONT: (PR_3, ""),
			},

			PR_3: {
				BYE: ("", ""),
			},
		})


