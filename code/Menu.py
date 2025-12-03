import pygame.image
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # carregando a imagem do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # criar o retangulo

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # para carregar a musica
        pygame.mixer_music.play(-1)  # para a musica continua tocando
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha imagem dentro do retangulo
            self.menu_text(50, "Mountain", COLOR_WHITE, ((WIN_WIDTH / 2), 70))  # nome do jogo
            self.menu_text(50, "Shooter", COLOR_WHITE, ((WIN_WIDTH / 2), 120))  # nome do jogo
            for i in range(len(MENU_OPTION)):
                self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2),
                                                                 180 + 30 * i))  # menu do jogo nome do jogo ,para ficar um embaixo do outro

            pygame.display.flip()
            # Chechar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar janela
                    quit()  # encerrar programa

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
