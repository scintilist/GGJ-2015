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



rodman_1 = (N1, {
	N1: {
		K1: (N2, ""),
		K2: (N2, ""),
		K3: (N2, ""),
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

tiny_kim_1 = (N2, {
	N1: {
		K1: (N2, None),
		K2: (N2, None),
		K3: (N2, None),
	},

	N2: {
		K4: ("", None),
	}
})

