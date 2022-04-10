class Objet:
	def __init__(self, allow_interact:bool, allow_overlay:bool)->object:
		self.allow_interact = allow_interact
		self.allow_overlay = allow_overlay


class ObjetVide(Objet):
	def __init__(self):
		super().__init__(False, True)