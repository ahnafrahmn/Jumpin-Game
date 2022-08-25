import pygame
import random


def score_board():
    this_time = int(pygame.time.get_ticks() / 100) - start_score
    score = score_txt.render(f'{this_time}', False, (64, 64, 64))
    score_rect = score.get_rect(center=(450, 50))
    screen.blit(score, score_rect)


pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Jumpin")
clock = pygame.time.Clock()
game_on = True
start_score = 0

score_txt = pygame.font.Font('fonts/game_font.ttf', 50)
msg_score = score_txt.render('Score', False, (64, 64, 64))


bg_surf = pygame.image.load('image/bg.jpg').convert_alpha()
player = pygame.image.load('image/player1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(200, 360))
enemy = pygame.image.load('image/enemy1.png').convert_alpha()
enemy_rect = enemy.get_rect(midbottom=(700, 360))

player_gravity = 0


# -------------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_on:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and player_rect.bottom >= 360:
                player_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_on = True
                enemy_rect.x = 700
                start_score = int(pygame.time.get_ticks() / 100)

# -------------------------------------------------------------------------------
    if game_on:
        screen.blit(bg_surf, (0, 0))
        screen.blit(player, player_rect)
        screen.blit(enemy, enemy_rect)
        screen.blit(msg_score, (150, 25))
        score_board()
    # -------------------------------------------------------------------------------
    # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 360:
            player_rect.bottom = 360

    # -------------------------------------------------------------------------------
    # ENEMY
        rn = random.randint(3, 15)
        enemy_rect.x -= 1 + rn
        if enemy_rect.x <= 0:
            enemy_rect.x = 690
            enemy_rect.x -= 1 + rn
            # -------------------------------------------------------------------------------
          # COLLISION
        if enemy_rect.colliderect(player_rect):
            game_on = False
            # screen.fill((189, 67, 67))
# -------------------------------------------------------------------------------
    pygame.display.update()
    clock.tick(60)
