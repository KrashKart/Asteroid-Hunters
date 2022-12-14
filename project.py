import pygame
from entities import *
import sys
from visuals import *
from pygame.locals import K_w, K_a, K_s, K_d, K_ESCAPE, K_SPACE

def main():

    # call engine and window initialiser from visuals.py
    screen, background = init()

    # main menu screen
    while True:
        game_state = main_menu(screen)
        if game_state == GameState.START:
            break

        if game_state == GameState.QUIT:
            pygame.quit()
            return

    # initialise all assets
    player_list = pygame.sprite.Group()
    player = Player()
    player_list.add(player)

    asteroid_list = pygame.sprite.Group()
    for n in range(8):
            asteroid =  Asteroid()
            asteroid_list.add(asteroid)

    missile_list = pygame.sprite.Group()

    data = Data()

    # initialise timer vars
    timer = 0
    last = 0

    # Game loop
    while True:

        # check if game is paused
        if game_state == GameState.PAUSE:
            pause(screen, player)

        # check if the player has died
        if player.health <= 0:
            break

        # draw screen
        screen.blit(background, (0, 0))

        # event detector
        for event in pygame.event.get():
            match event.type:

                # test for close button press
                case pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit("Closed")

                #test for shooting (space key) or pausing (esc key)
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_SPACE:
                            if pygame.time.get_ticks() - last >= 1000:
                                missile_list = player.fire(missile_list)
                                last = pygame.time.get_ticks()
                            else:
                                pass
                        case pygame.K_ESCAPE:
                            game_state = GameState.PAUSE
                            game_state = pause(screen, player)
                            if game_state == GameState.START:
                                break
                            elif game_state == GameState.QUIT:
                                pygame.quit()
                                sys.exit()

        # test for keyboard input/release
        keys = pygame.key.get_pressed()

        # test for arrow keys for movement
        if keys[K_a] and player.rect.x >= 0:
            player.move(-1, 0, game_state)
        if keys[K_d] and player.rect.x <= 1136:
            player.move(1, 0, game_state)
        if keys[K_w] and player.rect.y >= 0:
            player.move(0, -1, game_state)
        if keys[K_s] and player.rect.y <= 686:
            player.move(0, 1, game_state)

        # timer for difficulty, add points
        timer += 1
        if timer % 180 == 0:
            asteroid = Asteroid()
            asteroid_list.add(asteroid)
        
        if timer % 360 == 0:
            player.points += 100

        # update all asteroids
        for asteroid in asteroid_list:
            asteroid.update(player_list, missile_list, game_state)

        # update all missiles
        for missile in missile_list:
            missile.update(asteroid_list, player, game_state)

        # update player
        player.update(asteroid_list)

        # draw the updated versions of all sprites
        player_list.draw(screen)
        asteroid_list.draw(screen)
        missile_list.draw(screen)

        # show health bar, timer, score
        data.show_data(player, screen, game_state)

        # refresh window
        pygame.display.update()

    # game over screen
    while True:
        game_over(screen, player)

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def abso(a):
    return a if a > 0 else -a

if __name__ == "__main__":
    main()