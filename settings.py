class Settings:
    """Uma classe armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""

        # Cofigurações da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Configurações para a espaçonave
        self.ship_limit = 3

        # Configurações dos projéteis
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 0, 0, 230
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.fleet_drop_speed = 7

        # Configurações do alienígenas
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as  configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
