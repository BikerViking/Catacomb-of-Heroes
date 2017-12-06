import pygame

class inputModel(object):
	"""
	Input's Model class.

	Attributes:
		K_UP: Key to move up.
		K_DOWN: Key to move down.
		K_LEFT: Key to move left.
		K_RIGHT: Key to move right.
		K_UL: Key to move up+left.
		K_UR: Key to move up+right.
		K_DL: Key to move down+left.
		K_DR: Key to move down+right.

		K_WAIT: Key to wait or pick up itens at the same x and y.

		K_OK: Key to confirm.
		K_OK2: Secondary key to confirm.

		K_NG: Key to refuse/go back.

		K_START: Key to bring the main menu.
		
		N_UP: Navigate key to move up.
		N_DOWN: Navigate key to move down.
		N_LEFT: Navigate key to move left.
		N_RIGHT: Navigate key to move right.

		N_OK: Navigate key to confirm.
		N_NG: Navigate key to refuse/go back.
		
		keys: Dictionary with all keyboard keys.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(inputModel, self).__init__()		
		self.setKeys()
		self.default()
		self.navi()

	def default(self):
		"""
		Set the default keys.
		"""
		self.K_UP = self.keys["[8]"]
		self.K_DOWN = self.keys["[2]"]
		self.K_LEFT = self.keys["[4]"]
		self.K_RIGHT = self.keys["[6]"]

		self.K_UL = self.keys["[7]"]
		self.K_UR = self.keys["[9]"]
		self.K_DL = self.keys["[1]"]
		self.K_DR = self.keys["[3]"]

		self.K_WAIT = pygame.K_KP5

		self.K_OK = self.keys["return"]
		self.K_OK2 = pygame.K_KP_ENTER

		self.K_NG = pygame.K_BACKSPACE

		self.K_START = pygame.K_ESCAPE

	def navi(self):
		"""
		Set the default navigation keys.
		"""
		self.N_UP = pygame.K_UP
		self.N_DOWN = pygame.K_DOWN
		self.N_LEFT = pygame.K_LEFT
		self.N_RIGHT = pygame.K_RIGHT

		self.N_OK = pygame.K_RETURN
		self.N_NG = pygame.K_BACKSPACE

	def setKeys(self):
		"""
		Fill the dictionary with all keyboard keys.

		After I finished this dictionary I felt really dumb.
		But... It is done now... I don' want to remove it because it works...
		"""
		self.keys = {
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