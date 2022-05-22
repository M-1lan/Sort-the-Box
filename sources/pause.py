import pygame, sys

btn_lecture = pygame.image.load("images/btn_lecture.png")
btn_lecture = pygame.transform.scale(btn_lecture, (60, 60))
width_btn, heigth_btn = btn_lecture.get_size()

def bouton_pause(fenetre, cases_plateau_l):
    execution = True
    width, heigth = fenetre.get_size()
    
    while execution:
        pygame.draw.rect(fenetre, (250,250,250), [width/2-width_btn/2, heigth/2+(32*cases_plateau_l)/2+10, width_btn, heigth_btn])
        
        bouton_lecture = fenetre.blit(btn_lecture, (width/2-width_btn/2, 500))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_lecture.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(fenetre,(250,250,250),[width/2-width_btn/2, heigth/2+(32*cases_plateau_l)/2+10, width_btn, heigth_btn])
                    execution = False
        pygame.display.flip()

    # def retour_menu():
    # execution = True
    # while execution:
    #     pygame.time.wait(1000)
    #     menu.page_menu()
    #     execution = False