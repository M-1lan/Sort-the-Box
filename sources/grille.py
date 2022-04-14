from objets import ObjetVide
import pygame

class Case:
    def __init__(self, pos_x:int, pos_y:int, is_filled:bool, content:object=None)->object:
        self.pos_x, self.pos_y  = pos_x, pos_y
        self.content = []
        if not(is_filled):
            self.content.append(ObjetVide(self.pos_x, self.pos_y))
        else:
            self.content.append(content if content != None else ObjetVide(self.pos_x, self.pos_y))

    
    def check_and_fill(self):
        if len(self.content) == 0:
            self.set_content(ObjetVide(self.pos_x, self.pos_y))


    def add_content(self, content:object):
        self.content.append(content)
        self.check_and_fill()


    def set_content(self, content:object):
        self.content = [content]
        self.check_and_fill()


    def remove_content_by_id(self, id:int):
        del self.content[id]
        self.check_and_fill()
    

    def remove_all_content(self, content):
        content_without_el = []
        for element in self.content:
            if content != element:
                content_without_el.append(element)
        self.content = content_without_el
        self.check_and_fill()
    

    def remove_first_content(self, content):
        self.content.remove(content)
        self.check_and_fill()


    def remove_last_content(self, content):
        trouve = False
        for index in range(len(self.content)):
            index_from_end = -index - 1
            if not(trouve) and self.content[index_from_end] == content:
                trouve = True
                del self.content[index_from_end]
        self.check_and_fill()


    def get_upper_element(self)->object:
        return self.content[-1]
    

class Grille:
    def __init__(self, dim_x, dim_y, case_size):
        self.dim_x, self.dim_y = dim_x, dim_y
        self.max_x, self.max_y = dim_x - 1, dim_y - 1

        self.case_size = case_size

        self.plateau = list()

        for line in range(dim_y):
            self.plateau.append(list())
            for column in range(dim_x):
                self.plateau[line].append(Case(column, line, False))


    def change_case(self, pos_x, pos_y, content, do_replace=False):
        if do_replace:
            if content == None:
                self.plateau[pos_y][pos_x].set_content(ObjetVide(self.pos_x, self.pos_y))
            else:
                self.plateau[pos_y][pos_x].set_content(content)
        else:
            if content == None:
                self.plateau[pos_y][pos_x].set_content(ObjetVide(self.pos_x, self.pos_y))
            else:
                self.plateau[pos_y][pos_x].add_content(content)
