

from code.Menu import Menu

import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.level import Level


class Game:
        def __init__(self,):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  # para abrir uma janela e conf o atamanho dela
        def run(self):

            while True:
                menu =Menu(self.window)
                menu_return =menu.run()
                if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                    level =Level(self.window,'Level1' ,menu_return)
                    level_return =level.run()
                elif menu_return == MENU_OPTION[4]: #para quando vc der um enter na exit vc sair do jogo
                    pygame.quit()  # Fechar janela
                    quit()  # encerrar programa
                else :
                    pass




