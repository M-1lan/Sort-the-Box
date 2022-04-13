import pygame

class Objet(pygame.sprite.Sprite):
    def __init__(self, allow_interact:bool, allow_overlay:bool)->object:
        super().__init__()
        self.allow_interact = allow_interact
        self.allow_overlay = allow_overlay


class ObjetVide(Objet):
    def __init__(self):
        super().__init__(False, True)


class Interactable(Objet):
    def __init__(self, name):
        super().__init__(True, False)
        self.name = name


    def interaction(self, personnage):
        print("{} interagit avec moi.".format(personnage))


class Bloquant(Objet):
    def __init__(self):
        super().__init__(False, False)

class NonBloquant(Objet):
    def __init__(self):
        super().__init__(False, True)
