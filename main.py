from fileinput import close

import pygame
print("Setup Start")
pygame.init()
window =pygame.display.set_mode(size=(600 , 480)) #para abrir uma janela e conf o atamanho dela
print("Setup End")

print("Loop Start")
while True: #Chechar eventos
    for event in pygame.event.get():
        print('quitting...')
      if event.type == pygame.QUIT: #Fechar janela
          pygame.quit()
          quit() #encerrar programa
