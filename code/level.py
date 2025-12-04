import sys

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_HEIGHT
from xml.dom.minidom import Entity

import pygame.display

from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000  # 20 segundos

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # por musica na primeira fase
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Texto do topo
            self.level_text(
                text_size=14,
                text=f'{self.name} - Timeout: {self.timeout / 100:.1f}s',
                text_color=COLOR_WHITE,
                text_center_pos=(120, 10)
            )

            # FPS
            self.level_text(
                text_size=14,
                text=f'fps: {clock.get_fps():.0f}',
                text_color=COLOR_WHITE,
                text_center_pos=(60, WIN_HEIGHT - 35)
            )

            # Quantidade de entidades
            self.level_text(
                text_size=14,
                text=f'entidades: {len(self.entity_list)}',
                text_color=COLOR_WHITE,
                text_center_pos=(90, WIN_HEIGHT - 20)
            )

            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
