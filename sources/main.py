import pygame
pygame.init()

## Création de la fenêtre de jeu 

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Petit Jardin")
			
running = True
infos_grille = dict()


def generer_grille(dim_x, dim_y):
	grille_de_jeu = []

	infos_grille["dimensions"] = dict()
	infos_grille["dimensions"]["x"] = dim_x
	infos_grille["dimensions"]["y"] = dim_y

	for line in range(dim_y):
		grille_de_jeu.append([])
		for column in range(dim_x):
			grille_de_jeu[line].append([])

	return grille_de_jeu

grille_de_jeu = generer_grille(9, 7)
print(grille_de_jeu)

personnage = {"coordinates": {"x": 0, "y": 0}}


def placer_personnage(pos_x, pos_y):
	print(pos_x, infos_grille["dimensions"]["x"], pos_y, infos_grille["dimensions"]["y"])
	if (pos_x <= infos_grille["dimensions"]["x"] - 1 and pos_x >= 0) and (pos_y <= infos_grille["dimensions"]["y"] - 1 and pos_y >= 0):
		grille_de_jeu[personnage["coordinates"]["y"]][personnage["coordinates"]["x"]] = []
		print("ok move")
		personnage["coordinates"] = dict()
		personnage["coordinates"]["x"] = pos_x
		personnage["coordinates"]["y"] = pos_y

		grille_de_jeu[pos_y][pos_x] = ["S"]

placer_personnage(8, 6)
print("grille:", *grille_de_jeu, sep="\n")

def deplacer_personnage(x, y):
	# x : 1 droite -1 gauche
	# y : 1 haut -1 bas

	placer_personnage(personnage["coordinates"]["x"] + x, personnage["coordinates"]["y"] - y)

	print("grille:", *grille_de_jeu, sep="\n")

## Boucle du jeu

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				deplacer_personnage(-1, 0)
			elif event.key == pygame.K_RIGHT:
				deplacer_personnage(1, 0)
			elif event.key == pygame.K_UP:
				deplacer_personnage(0, 1)
			elif event.key == pygame.K_DOWN:
				deplacer_personnage(0, -1)

pygame.quit()