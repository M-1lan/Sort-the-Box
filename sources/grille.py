from objets import ObjetVide
import pygame

class Case:
	def __init__(self, pos_x:int, pos_y:int, is_filled:bool, content:object=ObjetVide())->object:
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.content = []
		if not(is_filled):
			self.content.append(ObjetVide())
		else:
			self.content.append(content)
	
	def change_content(self, content:object):
		self.content.append(content)

	def get_upper_element(self):
		for element in self.content:
			upper_element = element
		return upper_element


class Grille:
	def __init__(self, dim_x, dim_y):
		self.dim_x = dim_x
		self.max_x = dim_x - 1

		self.dim_y = dim_y
		self.max_y = dim_y - 1
		self.plateau = list()

		for line in range(dim_y):
			self.plateau.append(list())
			for column in range(dim_x):
				self.plateau[line].append(Case(column, line, False))

	def change_case(self, pos_x, pos_y, content):
		if content == None:
			self.plateau[pos_y][pos_x].change_content(ObjetVide())
		else:
			self.plateau[pos_y][pos_x].change_content(content)