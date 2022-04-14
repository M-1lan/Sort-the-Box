import pygame

sol = pygame.image.load("sources/images/sol.jpg") 
mur = pygame.image.load("sources/images/mur.jpg")
element_interactif = pygame.image.load("sources/images/element_interactif.jpg") 

class Objet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, fenetre, allow_interact:bool, allow_overlay:bool)->object:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fenetre = fenetre
        self.allow_interact = allow_interact
        self.allow_overlay = allow_overlay


class ObjetVide(Objet):
    def __init__(self, pos_x, pos_y, fenetre):
        super().__init__(pos_x, pos_y, fenetre, False, True)
        self.fenetre.blit(sol, 0, 0)


class Interactable(Objet):
    def __init__(self, pos_x, pos_y, fenetre, name):
        super().__init__(pos_x, pos_y, fenetre, True, False)
        self.name = name


    def interaction(self, personnage):
        print("{} interagit avec moi. Je suis {}, en ({}, {})".format(personnage.name, self.name, self.pos_x, self.pos_y))


class Bloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre):
        super().__init__(pos_x, pos_y, fenetre, False, False)


class NonBloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre):
        super().__init__(pos_x, pos_y, fenetre, False, True)


class Lit(Interactable):
    def __init__(self, pos_x, pos_y, fenetre, proprietaire:object, name:str="Lit", allow_others:bool=False):
        super().__init__(pos_x, pos_y, fenetre, name)
        self.proprietaire = proprietaire
        self.allow_others = allow_others


    def interaction(self, dormeur):
        if (dormeur == self.proprietaire or \
                self.allow_others):
            super().interaction(dormeur)
            dormeur.grille.plateau[dormeur.pos_y][dormeur.pos_x].remove_last_content(dormeur)
            dormeur.grille.plateau[self.pos_y][self.pos_x].add_content(dormeur)
            dormeur.pos_x, dormeur.pos_y = self.pos_x, self.pos_y
