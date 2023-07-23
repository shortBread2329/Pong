import pygame
import sys

# Pygameを初期化
pygame.init()

# ゲームウィンドウの大きさを設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# パドルとボールのプロパティを設定
paddle_width = 15
paddle_height = 80
paddle_speed = 2
paddle1_x_position = 0
paddle1_y_position = screen_height / 2
paddle2_x_position = screen_width - paddle_width
paddle2_y_position = screen_height / 2
ball_size = 15
ball_x_position = screen_width / 2
ball_y_position = screen_height / 2
ball_x_speed = 2
ball_y_speed = 2

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if paddle1_y_position > 0:
            paddle1_y_position -= paddle_speed
    if keys[pygame.K_DOWN]:
        if paddle1_y_position < screen_height - paddle_height:
            paddle1_y_position += paddle_speed
    if keys[pygame.K_w]:
        if paddle2_y_position > 0:
            paddle2_y_position -= paddle_speed
    if keys[pygame.K_s]:
        if paddle2_y_position < screen_height - paddle_height:
            paddle2_y_position += paddle_speed

    ball_x_position += ball_x_speed
    ball_y_position += ball_y_speed

    if ball_y_position > screen_height - ball_size or ball_y_position < 0:
        ball_y_speed *= -1
    if ball_x_position > screen_width - ball_size:
        if paddle2_y_position < ball_y_position < paddle2_y_position + paddle_height:
            ball_x_speed *= -1
        else:
            ball_x_position = screen_width / 2
            ball_y_position = screen_height / 2
    if ball_x_position < 0:
        if paddle1_y_position < ball_y_position < paddle1_y_position + paddle_height:
            ball_x_speed *= -1
        else:
            ball_x_position = screen_width / 2
            ball_y_position = screen_height / 2

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(paddle1_x_position, paddle1_y_position, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(paddle2_x_position, paddle2_y_position, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(ball_x_position, ball_y_position, ball_size, ball_size))
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
