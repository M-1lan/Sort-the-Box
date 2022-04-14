import pygame

directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "O": (-1, 0)}


class Personnage(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name, grille):
        super().__init__()
        self.pos_x = self.last_x = pos_x
        self.pos_y = self.last_y = pos_y

        self.real_x, self.real_y = self.pos_x * 20, self.pos_y * 20
        self.dir = "N"

        self.speed = 20

        self.name = name
        self.grille = grille
        self.grille.change_case(self.pos_x, self.pos_y, self)
    

    def deplacer_pixels(self, direction):
        print("deplacer_pixels")
        if direction in directions:
            print("direction acceptée")
            self.dir = direction

            desired_pos_x = self.pos_x + directions[direction][0]
            desired_pos_y = self.pos_y + directions[direction][1]

            desired_real_x = self.real_x + (directions[direction][0] * self.speed)
            desired_real_y = self.real_y + (directions[direction][1] * self.speed)

            if (desired_real_x >= 0 and \
                    desired_real_x <= self.grille.max_x * self.grille.case_size and \
                    desired_real_y >= 0 and \
                    desired_real_y <= self.grille.max_y * self.grille.case_size and \
                    self.grille.plateau[desired_pos_y][desired_pos_x].get_upper_element().allow_overlay):
                print("I'm OK to move to ({}, {}) / ({}, {}) from ({}, {}) / ({}, {})".format(
                    desired_pos_x, desired_pos_y,
                    desired_real_x, desired_real_y,
                    self.pos_x, self.pos_y,
                    self.real_x, self.real_y
                ))
            else:
                print("I'm NOT OK to move to ({}, {}) / ({}, {}) from ({}, {}) / ({}, {})".format(
                    desired_pos_x, desired_pos_y,
                    desired_real_x, desired_real_y,
                    self.pos_x, self.pos_y,
                    self.real_x, self.real_y
                ))
                self.real_x, self.real_y = desired_real_x, desired_real_y
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
                self.last_y, self.last_x = self.pos_y, self.pos_x
                self.pos_y, self.pos_x = desired_pos_y, desired_pos_x
                
                self.grille.plateau[self.last_y][self.last_x].remove_last_content(self)
                self.grille.plateau[self.pos_y][self.pos_x].add_content(self)

            else:
                raise ValueError("Impossible de déplacer {} vers {}.".format(self.name, direction))
    

    def interagir(self):
        pos_x_interact = self.pos_x + directions[self.dir][0]
        pos_y_interact = self.pos_y + directions[self.dir][1]
        self.interagir_avec_coordonnees(pos_x_interact, pos_y_interact)


    def interagir_avec_coordonnees(self, pos_x, pos_y):
        dist_x = abs(pos_x - self.pos_x)
        dist_y = abs(pos_y - self.pos_y)
        if self.grille.plateau[pos_y][pos_x].get_upper_element().allow_interact and ((dist_x == 1 and dist_y == 0) or (dist_x == 0 and dist_y == 1)):
            self.grille.plateau[pos_y][pos_x].get_upper_element().interaction(self)
        else:
            raise ValueError("Impossible de faire interagir {} avec l'élément de coordonnées ({}, {})".format(self.name, pos_x, pos_y))