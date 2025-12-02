from threading import settrace_all_threads

from code.Menu import Menu

import pygame
class Game:
        def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode(size=(600, 480))  # para abrir uma janela e conf o atamanho dela
        def run(self):
            while True:
               menu =Menu(self.window)
               menu.run()
               pass
                     # Chechar eventos
                     #  for event in pygame.event.get():
                     #  if event.type == pygame.QUIT:
                     #    pygame.quit()#Fechar janela
                     #    quit() #encerrar programa
