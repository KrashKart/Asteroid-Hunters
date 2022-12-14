import pygame
import pygame.freetype
import sys
from enum import Enum
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def init():
    # Initialise game engine
    pygame.init()

    # initialise window
    screen = pygame.display.set_mode((1200, 750))
    screen.fill((0, 0, 0))

    # initialise background image
    background = pygame.image.load("bg.jpg")
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))

    # set window title and icon
    pygame.display.set_caption("Asteroid Hunters by KrashKart")
    icon = pygame.image.load("asteroid.png")
    pygame.display.set_icon(icon)
    return screen, background



class Data:
    def show_data(self, player, screen, game_state):
        font = pygame.font.Font("freesansbold.ttf", 32)
        score = font.render(f"Score   {player.points}", True, (255, 255, 255))
        screen.blit(score, (10, 10))


        font = pygame.font.Font("freesansbold.ttf", 32)
        score = font.render("Health", True, (255, 255, 255))
        screen.blit(score, (10, 50))

        heartImg = pygame.image.load("heart.png")
        heartImg = pygame.transform.scale(heartImg, (32, 32))
        heartImg.set_colorkey((0, 0, 0))
        for i in range(player.health):
            heart = heartImg.get_rect()
            heart.x = 130 + 40 * i
            heart.y = 50
            screen.blit(heartImg, heart)

        if game_state == GameState.PAUSE:
            pass
        else:
            current_time = int(pygame.time.get_ticks())
            font = pygame.font.Font("freesansbold.ttf", 24)
            seconds = int((current_time/1000) % 60)
            minutes = int(current_time/60_000)
            clocker = font.render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
            screen.blit(clocker, (10, 90))


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
        font = pygame.freetype.SysFont("Courier", font_size, bold=True)
        surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
        return surface.convert_alpha()


class element(pygame.sprite.Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action):
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameState(Enum):
    QUIT = -1
    START = 1
    PAUSE = 0

def main_menu(screen):
    start_btn = element(
        center_position=(600, 550),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Start",
        action=GameState.START,
    )
    quit_btn = element(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        
        font = pygame.font.Font("freesansbold.ttf", 64)
        score = font.render("ASTEROID HUNTERS", True, (255, 255, 255))
        screen.blit(score, (250, 300))

        pygame.display.flip()

def game_over(screen, player):
    quit_btn = element(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [quit_btn]
    current_time = int(pygame.time.get_ticks())
    seconds = int((current_time/1000) % 60)
    minutes = int(current_time/60_000)
    alpha = pygame.image.load("alpha_surface.png")
    alpha = pygame.transform.scale(alpha, (1200, 750))
    alpha.set_alpha(5)
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(alpha, (0,0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                pygame.quit()
                sys.exit()
            button.draw(screen)

        font = pygame.font.Font("freesansbold.ttf", 64)
        score = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(score, (400, 300))

        font = pygame.font.Font("freesansbold.ttf", 56)
        score = font.render(f"Score {player.points:05d}", True, (255, 255, 255))
        screen.blit(score, (430, 400))

        font = pygame.font.Font("freesansbold.ttf", 56)
        clocker = font.render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
        screen.blit(clocker, (525, 500))

        pygame.display.flip()

def pause(screen, player):
    quit_btn = element(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    resume_btn = element(
        center_position=(600, 550),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Resume",
        action=GameState.START,
    )

    buttons = [resume_btn, quit_btn]
    current_time = int(pygame.time.get_ticks())
    seconds = int((current_time/1000) % 60)
    minutes = int(current_time/60_000)

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        font = pygame.font.Font("freesansbold.ttf", 64)
        paused = font.render("Paused", True, (255, 255, 255))
        screen.blit(paused, (485, 200))

        font = pygame.font.Font("freesansbold.ttf", 32)
        score = font.render(f"Score {player.points:05d}", True, (255, 255, 255))
        screen.blit(score, (505, 400))

        font = pygame.font.Font("freesansbold.ttf", 32)
        clocker = font.render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
        screen.blit(clocker, (560, 450))

        pygame.display.update()


if __name__ == "__main__":
    pass