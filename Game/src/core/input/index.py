import pygame

class Index(object):
	"""
	Index class goes through keyboard and maps it's keys.
	Theese keys are stored in a dictionary to be used as reference later.

	# TODO Gamepad Support.

	# TODO Windows/Mac Support.

	Attributes:
		keys: dictionary, stores all keyboard keys.
	"""

	def __init__(self):
		"""
		Inits Index Object
		"""

		super(Index, self).__init__()

		self.__keyboard_keys()

	def __keyboard_keys(self):
		"""
		Fill the dictionary with all keyboard keys.

		After I finished this dictionary I felt really dumb.
		But... It is done now... I don' want to remove it because it works...
		"""
		self._keys = {
		"unknown key"		: pygame.K_F15, # FAIL SAFE
		"backspace" 		: pygame.K_BACKSPACE,
		"tab" 				: pygame.K_TAB,
		" "					: pygame.K_CLEAR,
		"return" 			: pygame.K_RETURN,
		"pause" 			: pygame.K_PAUSE,
		"escape"	 		: pygame.K_ESCAPE,
		"space"	 			: pygame.K_SPACE,
		"!"				 	: pygame.K_EXCLAIM,
		"\"" 				: pygame.K_QUOTEDBL,
		"#"					: pygame.K_HASH,
		"$"					: pygame.K_DOLLAR,
		"&" 				: pygame.K_AMPERSAND,
		"\'" 				: pygame.K_QUOTE,
		"(" 				: pygame.K_LEFTPAREN,
		")" 				: pygame.K_RIGHTPAREN,
		"*"					: pygame.K_ASTERISK,  
		"+" 				: pygame.K_PLUS,
		#","					: pygame.K_COMA,
		"-"					: pygame.K_MINUS,
		"." 				: pygame.K_PERIOD,
		"/"					: pygame.K_SLASH,
		"0"					: pygame.K_0,
		"1"					: pygame.K_1,
		"2"					: pygame.K_2,
		"3"					: pygame.K_3,
		"4"					: pygame.K_4,
		"5"					: pygame.K_5,
		"6"					: pygame.K_6,
		"7"					: pygame.K_7,
		"8"					: pygame.K_8,
		"9"					: pygame.K_9,
		":"					: pygame.K_COLON,
		";"					: pygame.K_SEMICOLON,
		","					: pygame.K_LESS,
		"="					: pygame.K_EQUALS,
		">"					: pygame.K_GREATER,
		"?"					: pygame.K_QUESTION,
		"@"					: pygame.K_AT,
		"["					: pygame.K_LEFTBRACKET,
		"\\"				: pygame.K_BACKSLASH,
		"]"					: pygame.K_RIGHTBRACKET,
		"world 71"	 		: pygame.K_CARET,
		"_"					: pygame.K_UNDERSCORE,
		"'"					: pygame.K_BACKQUOTE,
		"a"					: pygame.K_a,
		"b"					: pygame.K_b,
		"c"					: pygame.K_c,
		"d"					: pygame.K_d,
		"e"					: pygame.K_e,
		"f"					: pygame.K_f,
		"g"					: pygame.K_g,
		"h"					: pygame.K_h,
		"i"					: pygame.K_i,
		"j"					: pygame.K_j,
		"k"					: pygame.K_k,
		"l"					: pygame.K_l,
		"m"					: pygame.K_m,
		"n"					: pygame.K_n,
		"o"					: pygame.K_o,
		"p"					: pygame.K_p,
		"q"					: pygame.K_q,
		"r"					: pygame.K_r,
		"s"					: pygame.K_s,
		"t"					: pygame.K_t,
		"u"					: pygame.K_u,
		"v"					: pygame.K_v,
		"w"					: pygame.K_w,
		"x"					: pygame.K_x,
		"y"					: pygame.K_y,
		"z"					: pygame.K_z,
		"delete"			: pygame.K_DELETE,
		"[0]"				: pygame.K_KP0,
		"[1]"				: pygame.K_KP1,
		"[2]"				: pygame.K_KP2,
		"[3]"				: pygame.K_KP3,
		"[4]"				: pygame.K_KP4,
		"[5]"				: pygame.K_KP5,
		"[6]"				: pygame.K_KP6,
		"[7]"				: pygame.K_KP7,
		"[8]"				: pygame.K_KP8,
		"[9]"				: pygame.K_KP9,
		"[.]"				: pygame.K_KP_PERIOD,
		"[/]"				: pygame.K_KP_DIVIDE,
		"[*]"				: pygame.K_KP_MULTIPLY,
		"[-]"				: pygame.K_KP_MINUS,
		"[+]"				: pygame.K_KP_PLUS,
		"enter"				: pygame.K_KP_ENTER,
		"[=]"				: pygame.K_KP_EQUALS,
		"up"				: pygame.K_UP,
		"down"				: pygame.K_DOWN,
		"left"				: pygame.K_RIGHT,
		"right"				: pygame.K_LEFT,
		"insert"			: pygame.K_INSERT,
		"home"				: pygame.K_HOME,
		"end"				: pygame.K_END,
		"page up"			: pygame.K_PAGEUP,
		"page down"			: pygame.K_PAGEDOWN,
		"f1"				: pygame.K_F1,
		"f2"				: pygame.K_F2,
		"f3"				: pygame.K_F3,
		"f4"				: pygame.K_F4,
		"f5"				: pygame.K_F5,
		"f6"				: pygame.K_F6,
		"f7"				: pygame.K_F7,
		"f8"				: pygame.K_F8,
		"f9"				: pygame.K_F9,
		"f10"				: pygame.K_F10,
		"f11"				: pygame.K_F11,
		"f12"				: pygame.K_F12,
		"f13"				: pygame.K_F13,
		"f14"				: pygame.K_F14,
		"f15"				: pygame.K_F15,
		"numlock"			: pygame.K_NUMLOCK,
		"caps lock"			: pygame.K_CAPSLOCK,
		"scroll lock"		: pygame.K_SCROLLOCK,
		"right shift"		: pygame.K_RSHIFT,
		"left shift"		: pygame.K_LSHIFT,
		"right ctrl"		: pygame.K_RCTRL,
		"left ctrl"			: pygame.K_LCTRL,
		"right alt"			: pygame.K_RALT,
		"left alt"			: pygame.K_LALT,
		"alt gr"			: pygame.K_LALT,
		"right meta"		: pygame.K_RMETA,
		"left meta"			: pygame.K_LMETA,
		"left Windows key"	: pygame.K_LSUPER,
		"right Windows key"	: pygame.K_RSUPER,
		"left super"		: pygame.K_LSUPER,
		"right super"		: pygame.K_LSUPER,
		"mode shift"		: pygame.K_MODE,
		"help"				: pygame.K_HELP,
		"print screen"		: pygame.K_PRINT,
		"sysrq"				: pygame.K_SYSREQ,
		"break"				: pygame.K_BREAK,
		"menu"				: pygame.K_MENU,
		"power"				: pygame.K_POWER,
		"Euro"				: pygame.K_EURO,
		}