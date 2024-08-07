import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf
from button import Button


def run_game():

    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma instância para armazenar estatísticas do jogo e cria um painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave,um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Cria um botão play
    play_button = Button(ai_settings, screen, "Play")

    # Inicia o laço principal do jogo
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active and not stats.game_pause:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
