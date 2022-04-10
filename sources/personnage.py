directions = ["N", "E", "S", "O"]

class Personnage:
	def __init__(self, pos_x, pos_y, name, grille):
		self.pos_x = self.last_x = pos_x
		self.pos_y = self.last_y = pos_y
		self.dir = "N"
		self.name = name
		grille.change_case(self.pos_x, self.pos_y, self)
	

	def deplacer(self, direction, grille):
		if direction in directions:
			self.dir = direction
			if direction == "N" and self.pos_y - 1 >= 0 and grille.plateau[self.pos_y - 1][self.pos_x].content.allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_y -= 1
				self.move_status = True

			elif direction == "E" and self.pos_x + 1 <= grille.max_x and grille.plateau[self.pos_y][self.pos_x + 1].content.allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_x += 1
				self.move_status = True
			
			elif direction == "S" and self.pos_y + 1 <= grille.max_y and grille.plateau[self.pos_y + 1][self.pos_x].content.allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_y += 1
				self.move_status = True

			elif direction == "O" and self.pos_x - 1 >= 0 and grille.plateau[self.pos_y][self.pos_x - 1].content.allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_x -= 1
				self.move_status = True
			else:
				self.move_status = False
		else:
			self.move_status = False
		
		if self.move_status:
			grille.change_case(self.last_x, self.last_y, None)
			grille.change_case(self.pos_x, self.pos_y, self)
		else:
			raise ValueError("Impossible de déplacer {} vers {}.".format(self.name, direction))
	

	

	def interagir(self, pos_x, pos_y, check_place=True, check_interaction=True):
		if not check_place:
			pass
		else:
			if (abs(pos_x - self.pos_x) == 1 and abs(pos_y - self.pos_y) == 0) \
					or (abs(pos_x - self.pos_x) == 0 and abs(pos_y - self.pos_y) == 1):
				pass
			else:
				raise ValueError("Impossible de faire intéragir {} avec l'élément de coordonnées {}".format(self.name, (pos_x, pos_y)))