import pygame
pygame.init()

# Création de la fenêtre de jeu 

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Petit Jardin")

# Boucle du jeu

running = True

def generer_grille(dim_x, dim_y):
	grille_de_jeu = []

	for line in range(dim_y):
		grille_de_jeu.append([])
		for column in range(dim_x):
			grille_de_jeu[line].append([])

	print(*grille_de_jeu, sep="\n")

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pass
			elif event.key == pygame.K_RIGHT:
				pass
			elif event.key == pygame.K_UP:
				pass
			elif event.key == pygame.K_DOWN:
				pass

pygame.quit()