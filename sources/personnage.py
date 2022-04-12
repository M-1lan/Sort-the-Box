import pygame

directions = ["N", "E", "S", "O"]

class Personnage(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, name, grille):
		super().__init__()
		self.pos_x = self.last_x = pos_x
		self.pos_y = self.last_y = pos_y
		self.dir = "N"
		self.name = name
		self.grille = grille
		self.grille.change_case(self.pos_x, self.pos_y, self)
	

	def deplacer(self, direction):
		if direction in directions:
			self.dir = direction
			if direction == "N" and self.pos_y - 1 >= 0 and self.grille.plateau[self.pos_y - 1][self.pos_x].get_upper_element().allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_y -= 1
				self.move_status = True

			elif direction == "E" and self.pos_x + 1 <= self.grille.max_x and self.grille.plateau[self.pos_y][self.pos_x + 1].get_upper_element().allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_x += 1
				self.move_status = True
			
			elif direction == "S" and self.pos_y + 1 <= self.grille.max_y and self.grille.plateau[self.pos_y + 1][self.pos_x].get_upper_element().allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_y += 1
				self.move_status = True

			elif direction == "O" and self.pos_x - 1 >= 0 and self.grille.plateau[self.pos_y][self.pos_x - 1].get_upper_element().allow_overlay:
				self.last_y, self.last_x = self.pos_y, self.pos_x
				self.pos_x -= 1
				self.move_status = True
			else:
				self.move_status = False
		else:
			self.move_status = False
		
		if self.move_status:
			self.grille.change_case(self.last_x, self.last_y, None) # TO DO : Ne pas supprimer tout le contenu de la case
			self.grille.change_case(self.pos_x, self.pos_y, self)
		else:
			raise ValueError("Impossible de déplacer {} vers {}.".format(self.name, direction))
	
	def interagir(self, pos_x, pos_y):
		dist_x = abs(pos_x - self.pos_x)
		dist_y = abs(pos_y - self.pos_y)
		if self.grille.plateau[pos_y][pos_x].get_upper_element().allow_interact and ((dist_x == 1 and dist_y == 0) or (dist_x == 0 and dist_y == 1)):
			self.grille.plateau[pos_y][pos_x].get_upper_element().interaction(self.name)
		else:
			raise ValueError("Impossible de faire interagir {} avec l'élément de coordonnées ({}, {})".format(self.name, pos_x, pos_y))