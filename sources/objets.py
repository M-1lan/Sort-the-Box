import pygame, random

sol = pygame.image.load("images/sol.png")
carton = pygame.image.load("images/carton.png") 
bac = pygame.image.load("images/bac_vert.png") 
default = pygame.image.load("images/default.jpg") 
tapis = pygame.image.load("images/tapis.jpg")
transparent = pygame.image.load("images/transparent.png")

directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "O": (-1, 0)}

coordonnees_bordures = {
    "N": {
        "E": (32, 0),
        "O": (16, 0),
        "S": (0, 0),
        "EO": (48, 0),
        "OS": (64, 0),
        "ES": (80, 0)
    }, "E": {
        "N": (16, 16),
        "O": (0, 16),
        "S": (32, 16),
        "NS": (48, 16),
        "NO": (64, 16),
        "OS": (80, 16)
    }, "S": {
        "E": (16, 32),
        "N": (0, 32),
        "O": (32, 32),
        "EO": (48, 32),
        "EN": (64, 32),
        "NO": (80, 32)
    }, "O": {
        "E": (0, 48),
        "N": (32, 48),
        "S": (16, 48),
        "NS": (48, 48),
        "ES": (64, 48),
        "EN": (80, 48)
    }
}

coordonnees_bacs = {
    "N": (0, 0),
    "E": (16, 0),
    "S": (32, 0),
    "O": (48, 0)
}

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
        if isinstance(self, Carton) : print("placage de carton")
        self.window_x, self.window_y = self.fenetre.get_size()
        self.fenetre.blit(self.image, ( \
            self.pos_x * self.grille.dim_case + (self.window_x / 2 - self.grille.dim_case * self.grille.dim_x / 2 ), \
            self.pos_y * self.grille.dim_case + (self.window_y / 2 - self.grille.dim_case * self.grille.dim_y / 2)
            ),
            (0, 0, self.grille.dim_case, self.grille.dim_case)
        )


class ObjetVide(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille):
        super().__init__(pos_x, pos_y, fenetre, False, True)
        self.image = sol
        self.image = pygame.transform.scale(sol, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()


class Interactable(Objet):
    def __init__(self, pos_x, pos_y, fenetre, name, grille, do_resize=True, image=default):
        super().__init__(pos_x, pos_y, fenetre, True, False)
        self.name = name
        self.backup_image = image.copy()
        self.image = image.copy()
        if do_resize:
            self.backup_image = pygame.transform.scale(self.backup_image, (image.get_width() // 16 * grille.dim_case, image.get_height() // 16 * grille.dim_case))
            self.image = pygame.transform.scale(image, (image.get_width() // 16 * grille.dim_case, image.get_height() // 16 * grille.dim_case))
        self.transparent = pygame.transform.scale(transparent, (grille.dim_case,)*2) 
        self.status_transparence = False
        self.grille = grille
        super().placer()

    def interaction(self, personnage):
        print("{} (positionné en ({}, {}), en direction {}) interagit avec moi. Je suis {}, en ({}, {}).".format(personnage.name, personnage.pos_x, personnage.pos_y, personnage.dir, self.name, self.pos_x, self.pos_y))

    def ajouter_transparence(self):
        self.status_transparence = True
        self.image.blit(self.transparent, (0, 0))
        super().placer()

    def enlever_transparence(self):
        self.status_transparence = False
        self.image = self.backup_image.copy()
        super().placer()

class Bloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille, do_resize=True, image=default):
        super().__init__(pos_x, pos_y, fenetre, False, False)
        if do_resize:
            self.image = pygame.transform.scale(image, (grille.dim_case,)*2)
        self.grille = grille 
        super().placer()


class NonBloquant(Objet):
    def __init__(self, pos_x, pos_y, fenetre, grille):
        super().__init__(pos_x, pos_y, fenetre, False, True)
        self.image = pygame.transform.scale(tapis, (grille.dim_case,)*2)
        self.grille = grille
        super().placer()

class Convoyeur(Interactable):
    def __init__(self, pos_x:int, pos_y:int, fenetre, grille, from_dir:str, default_to_dir:str, allowed_dirs:tuple):
        self.from_dir = from_dir
        self.to_dir = default_to_dir
        self.allowed_dirs = allowed_dirs
        self.compressed_dirs = "".join(sorted(self.allowed_dirs))
        self.to_dir_number = self.allowed_dirs.index(self.to_dir)
        
        self.fonds = pygame.image.load("images/convoyeur/tapis.png")
        self.fleches = pygame.image.load("images/convoyeur/fleches/{}{}.png".format(self.from_dir, self.to_dir))
        
        self.bordures = pygame.image.load("images/convoyeur/bordures/all.png")

        self.bordure_top_left = coordonnees_bordures[from_dir][self.compressed_dirs]

        self.creer_images()

        self.animation_step = 0

        self.image = self.images.subsurface(self.animation_step * 16, 0, 16, 16)
        self.carton = None
        self.do_check_carton = True

        fenetre.blit(self.images, (0, 0))
        super().__init__(pos_x, pos_y, fenetre, "Tapis-{}-{}".format(from_dir, default_to_dir), grille, True, self.image)

    def animation(self):
        self.animation_step = (self.animation_step + 1) % (self.images.get_width() // 16)
        self.image = self.images.subsurface(self.animation_step * 16, 0, 16, 16)

        self.image = pygame.transform.scale(self.image, (self.grille.dim_case,)*2)

        if self.status_transparence:
            self.ajouter_transparence()

        if self.animation_step == 0 and self.carton != None and self.do_check_carton:
            self.carton.deplacer()
        elif not self.do_check_carton:
            self.do_check_carton = True
        super().placer()

    def creer_images(self):
        self.images = self.fonds.copy()
        self.images.blit(self.fleches, (0, 0))

        for i in range(0, self.images.get_width(), 16):
            self.images.blit(self.bordures, (i, 0, 16, 16),
                (*self.bordure_top_left, 16, 16))


    def interaction(self, personnage):
        super().interaction(personnage)
        self.to_dir_number = (self.to_dir_number + 1) % len(self.allowed_dirs)
        self.to_dir = self.allowed_dirs[self.to_dir_number]

        self.fleches = pygame.image.load("images/convoyeur/fleches/{}{}.png".format(self.from_dir, self.to_dir))

        self.creer_images()

    def creer_carton(self):
        self.carton = Carton(self, self.fenetre, self.grille, "Rose")
        self.grille.change_case(self.pos_x, self.pos_y, self.carton)

    # def supprimer_carton(self):
    #     self.grille.plateau[self.pos_y][self.pos_x].remove_content_by_id(-1)
    #     self.carton = None

    def supprimer_carton(self):
        self.grille.plateau[self.pos_y][self.pos_x].remove_last_content(self.carton)
        self.carton = None

    def accueillir_carton(self, carton):
        self.carton = carton
        self.carton.convoyeur = self
        self.carton.to_dir = self.to_dir
        self.grille.change_case(self.pos_x, self.pos_y, self.carton)
        self.do_check_carton = False
    
    def ajouter_transparence(self):
        if len(self.allowed_dirs)>1 :
            super().ajouter_transparence()

class Bac(Bloquant):
    def __init__(self, pos_x, pos_y, fenetre, grille, couleur, direction):
        self.couleur = couleur
        self.from_dir = direction
        self.image = pygame.image.load("images/convoyeur/bacs/{}.png".format(couleur))
        self.image = self.image.subsurface(coordonnees_bacs[self.from_dir], (16, 16))
        self.score = 0
        super().__init__(pos_x, pos_y, fenetre, grille, True, self.image)

    def accueillir_carton(self, carton):
        self.carton = carton
        if self.carton.couleur == self.couleur:
            self.score += 1
        else:
            self.score -= 1
        self.carton.convoyeur = self
        self.grille.change_case(self.pos_x, self.pos_y, self.carton)
        self.supprimer_carton()
        print(self.score)

    def supprimer_carton(self):
        self.grille.plateau[self.pos_y][self.pos_x].remove_last_content(self.carton)
        self.carton = None
        

class Carton(Interactable):
    def __init__(self, convoyeur, fenetre, grille, couleur):
        self.image = pygame.Surface((grille.dim_case, )*2, pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image = self.image.copy()
        self.convoyeur = convoyeur
        self.to_dir = self.convoyeur.to_dir
        self.pos_x, self.pos_y = self.convoyeur.pos_x, self.convoyeur.pos_y
        self.couleur = couleur

        self.carton = pygame.image.load("images/cartons/carton_{}.png".format(self.couleur))
        self.carton = pygame.transform.scale(self.carton, (10 / 16 * grille.dim_case,)*2)
        
        self.image.blit(self.carton, (self.image.get_width() / 2 - self.carton.get_width() / 2, )*2)
        super().__init__(self.convoyeur.pos_x, self.convoyeur.pos_y, fenetre, "Carton-{couleur}", grille, False, self.image)
        

    def animation(self):
        desired_pos_x = self.pos_x + directions[self.convoyeur.to_dir][0]
        desired_pos_y = self.pos_y + directions[self.convoyeur.to_dir][1]
        test_convoyeur = self.grille.plateau[desired_pos_y][desired_pos_x].get_last_element_by_classname(Convoyeur)
        
        if test_convoyeur != None:
            self.pos_x = desired_pos_x
            self.pos_y = desired_pos_y
            # self.convoyeur.carton = None
            self.convoyeur.supprimer_carton()
            self.convoyeur = test_convoyeur
            self.convoyeur.carton = self

            self.convoyeur.creer_carton()
        super().placer()

    def deplacer(self):
        print("déplacer  carton")
        desired_pos_x = self.pos_x + directions[self.to_dir][0]
        desired_pos_y = self.pos_y + directions[self.to_dir][1]
        desired_case = self.grille.plateau[desired_pos_y][desired_pos_x]
        if isinstance(desired_case.get_upper_element(), (Convoyeur, Spawner, Bac)):
            self.pos_x, self.pos_y = desired_pos_x, desired_pos_y
            self.convoyeur.supprimer_carton()
            # self.convoyeur = desired_case.get_upper_element()
            desired_case.get_upper_element().accueillir_carton(self)
            # self.to_dir = self.convoyeur.to_dir
        elif isinstance(desired_case.get_upper_element(), (Carton)):
            self.pos_x, self.pos_y = desired_pos_x, desired_pos_y
            self.convoyeur.supprimer_carton()
            # self.convoyeur = desired_case.get_upper_element().convoyeur
            desired_case.get_upper_element().deplacer()
            desired_case.get_upper_element().accueillir_carton(self)
            # self.to_dir = self.convoyeur.to_dir
        super().placer()

    def interaction(self, personnage):
        super().interaction(personnage)
        self.convoyeur.interaction(personnage)
        self.to_dir = self.convoyeur.to_dir

class Spawner(Bloquant):
    def __init__(self, pos_x, pos_y, fenetre, grille, direction):
        self.carton = None
        self.to_dir = direction
        self.already_spawned_one = False
        self.already_spawned_two = False
        self.animation_step = 0
        self.image = pygame.image.load("images/convoyeur/depart.png")
        self.image = self.image.subsurface(coordonnees_bacs[self.to_dir], (16, 16))
        self.couleurs = ("rose", "blanc", "vert", "bleu", "orange")
        super().__init__(pos_x, pos_y, fenetre, grille, True, self.image)


    def creer_carton(self):
        self.carton = Carton(self, self.fenetre, self.grille, self.couleurs[random.randint(0, 4)])
        self.grille.change_case(self.pos_x, self.pos_y, self.carton)


    def supprimer_carton(self):
        self.grille.plateau[self.pos_y][self.pos_x].remove_last_content(self.carton)
        self.carton = None

    
    def animation(self):
        self.animation_step = (self.animation_step + 1) % 8

        if self.animation_step == 0 :
            if self.carton != None:
                self.carton.deplacer()

            if random.randint(0, 20) == 0:
                self.creer_carton()