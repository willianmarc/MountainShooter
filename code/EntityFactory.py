import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name:str,position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg =[]
                for i in range(7):

                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,WIN_HEIGHT /2-30)) # posição do jogador ,esta no centro da tela e um pouco pra frente da tela
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2+30))
            case 'Enemy1':
                return  Enemy('Enemy1',(WIN_WIDTH +10,random.randint(0,WIN_HEIGHT)))#para que o inigos aparece fora da tela como posições diferentes
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))