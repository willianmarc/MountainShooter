from idlelib.sidebar import EndLineDelegator
from operator import length_hint

import pygame.image
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # carregando a imagem do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # criar o retangulo

    def run(self,):
        menu_option=0
        pygame.mixer_music.load('./asset/Menu.mp3')  # para carregar a musica
        pygame.mixer_music.play(-1)  # para a musica continua tocando
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha imagem dentro do retangulo
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))  # nome do jogo
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))  # nome do jogo

            for i in range(len(MENU_OPTION)):
              if i ==menu_option: #opção selecionada mudade cor para amaerelo
                self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH /2) ,180 + 30 * i))  # menu do jogo nome do jogo ,para ficar um embaixo do outro
              else: #opção nao selecionada fica na cor branca
                self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))
            pygame.display.flip()
            # Chechar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar janela
                    quit()  # encerrar programa
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN: #SETA PARA BAIXO
                      if menu_option < len(MENU_OPTION) -1:
                          menu_option += 1
                      else:
                          menu_option =0

                    if event.key == pygame.K_UP:  # SETA PARA BAIXO
                       if menu_option >0:
                                menu_option -= 1
                       else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
