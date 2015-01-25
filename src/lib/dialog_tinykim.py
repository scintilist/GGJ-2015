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



tiny_kim_1 = (TK_GREET, {
	TK_GREET: {
		GREET_R1: (TK_INFO1_HAPPY, None),
		GREET_R2: (TK_INFO1_SAD, None),
	},

	TK_INFO1_SAD: {
		CONT: (TK_INFO2, None),
	},

	TK_INFO1_HAPPY: {
		CONT: (TK_INFO2, None),
	},

	TK_INFO2: {
		CONT: (TK_INFO3, None),
	},

	TK_INFO3: {
		CONT: (TK_INFO4, None),
	},

	TK_INFO4: {
		CONT: (TK_INFO5, None),
	},

	TK_INFO5: {
		BYE_CONFIDENT: ("", "tinykim_info_done"),
		BYE_APPREHENSIVE: ("", "tinykim_info_done"),
	},
})

tiny_kim_nag = (REMINDER, {
	REMINDER: {
		REMINDER_OK: ("", None),
	}
})
