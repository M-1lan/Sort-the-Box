import pygame

directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "O": (-1, 0)}

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
            # Si la direction demandée est une direction valide

            self.dir = direction

            desired_pos_x = self.pos_x + directions[direction][0]
            desired_pos_y = self.pos_y + directions[direction][1]
            
            if (desired_pos_x >= 0 and \
                    desired_pos_x <= self.grille.max_x and \
                    desired_pos_y >= 0 and \
                    desired_pos_y <= self.grille.max_y and \
                    self.grille.plateau[desired_pos_y][desired_pos_x].get_upper_element().allow_overlay):
                # TO DO : Vérifier aussi les Y
                self.last_y, self.last_x = self.pos_y, self.pos_x
                self.pos_y, self.pos_x = desired_pos_y, desired_pos_x
                
                self.grille.plateau[self.last_y][self.last_x].remove_last_content(self)
                self.grille.plateau[self.pos_y][self.pos_x].add_content(self)

            else:
                raise ValueError("Impossible de déplacer {} vers {}.".format(self.name, direction))
    

    def interagir(self):
        pos_x_interact = self.pos_x + directions[self.dir][0]
        pos_y_interact = self.pos_y + directions[self.dir][1]
        print("I :", pos_x_interact, pos_y_interact)
        self.interagir_avec_coordonnees(pos_x_interact, pos_y_interact)

    def interagir_avec_coordonnees(self, pos_x, pos_y):
        dist_x = abs(pos_x - self.pos_x)
        dist_y = abs(pos_y - self.pos_y)
        if self.grille.plateau[pos_y][pos_x].get_upper_element().allow_interact and ((dist_x == 1 and dist_y == 0) or (dist_x == 0 and dist_y == 1)):
            self.grille.plateau[pos_y][pos_x].get_upper_element().interaction(self.name)
        else:
            raise ValueError("Impossible de faire interagir {} avec l'élément de coordonnées ({}, {})".format(self.name, pos_x, pos_y))