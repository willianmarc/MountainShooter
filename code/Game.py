

from code.Menu import Menu

import pygame

from code.const import WIN_HEIGHT,WIN_WIDTH



class Game:
        def __init__(self,):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  # para abrir uma janela e conf o atamanho dela
        def run(self):

            while True:
               menu =Menu(self.window)
               menu.run()
               pass


