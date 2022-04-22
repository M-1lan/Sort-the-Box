import pygame

sol = pygame.image.load("images/sol.jpg")
mur = pygame.image.load("images/mur.jpg")
element_interactif = pygame.image.load("images/element_interactif.jpg") 
tapis = pygame.image.load("images/tapis.jpg")

class Objet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, fenetre, allow_interact:bool, allow_overlay:bool)->object:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fenetre = fenetre
        self.window_x, self.window_y = self.fenetre.get_size()
        self.allow_interact = allow_interact
        self.allow_overlay = allow_overlay
        

    def placer(self):
        self.fenetre.blit(self.image, ( \
            self.pos_x * self.grille.dim_case + (self.window_x / 2 - self.grille.dim_case * self.grille.dim_x / 2 ), \
            self.pos_y * self.grille.dim_case + (self.window_y / 2 - self.grille.dim_case * self.grille.dim_y / 2)
            )
        )


class ObjetVide(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille):
        super().__init__(pos_x, pos_y, fenetre, False, True)
        self.image = sol
        self.image = pygame.transform.scale(sol, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()


class Interactable(Objet):
    def __init__(self, pos_x, pos_y, fenetre, name, grille):
        super().__init__(pos_x, pos_y, fenetre, True, False)
        self.name = name
        self.image = element_interactif
        self.image = pygame.transform.scale(element_interactif, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()

    def interaction(self, personnage):
        print("{} (positionné en ({}, {}), en direction {}) interagit avec moi. Je suis {}, en ({}, {}).".format(personnage.name, personnage.pos_x, personnage.pos_y, personnage.dir, self.name, self.pos_x, self.pos_y))


class Bloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille):
        super().__init__(pos_x, pos_y, fenetre, False, False)
        self.image = mur
        self.image = pygame.transform.scale(mur, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()


class NonBloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille):
        super().__init__(pos_x, pos_y, fenetre, False, True)
        self.image = pygame.transform.scale(tapis, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()

class Lit(Interactable):
    def __init__(self, pos_x, pos_y, fenetre, proprietaire:object, grille, name:str="Lit", allow_others:bool=False):
        super().__init__(pos_x, pos_y, fenetre, name, grille)
        self.proprietaire = proprietaire
        self.allow_others = allow_others
        super().placer()


    def interaction(self, dormeur):
        if (dormeur == self.proprietaire or \
                self.allow_others):
            super().interaction(dormeur)
            dormeur.grille.plateau[dormeur.pos_y][dormeur.pos_x].remove_last_content(dormeur)
            dormeur.grille.plateau[self.pos_y][self.pos_x].add_content(dormeur)
            dormeur.pos_x, dormeur.pos_y = self.pos_x, self.pos_y
