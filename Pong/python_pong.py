# NOTE TO SELF
# pygame.Rect(x coordinate, y coordinate, width, height)
# the top left corner is the start

# Imports
import pygame
import random

# Variables
screen_width = (960)
screen_height = (720)
color_black = (0,0,0) # RGB value for background
color_white = (255, 255, 255) # RGB valuse for pieces
clock = pygame.time.Clock()
started = False

# Game Setup
def main():
  global started
  pygame.init()
  game_screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Pong")

  # Paddles
  paddle_1_rect = pygame.Rect(30, 0, 7, 100)
  paddle_2_rect = pygame.Rect(screen_width - 50, 0, 7, 100)
  paddle_1_move = 0
  paddle_2_move = 0

  # Ball
  ball_rect = pygame.Rect(screen_width / 2, screen_height / 2, 25, 25)
  ball_accel_x = random.randint(2, 4) * 0.1
  ball_accel_y = random.randint(2, 4) * 0.1

  # Randomize Ball Direction
  if random.randint(1, 2) == 1:
    ball_accel_x *= -1
  if random.randint(1, 2) == 1:
    ball_accel_y *= -1

  # Game Loop
  while True:
    game_screen.fill(color_black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          return
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            started = True
          if event.key == pygame.K_w: # PLAYER 1 (W and S)
            paddle_1_move = -0.5
          if event.key == pygame.K_s:
            paddle_1_move = 0.5
          if event.key == pygame.K_UP: # PLAYER 2 (Up and Down Arrows)
            paddle_2_move = -0.5
          if event.key == pygame.K_DOWN:
            paddle_2_move = 0.5

        # If the key is released
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w or event.key == pygame.K_s: # Stop the movement of paddle_1
            paddle_1_move = 0.0
          if event.key == pygame.K_UP or event.key == pygame.K_DOWN: # Stop the movement of paddle_2
            paddle_2_move = 0.0

    # Color Component
    pygame.draw.rect(game_screen, color_white, paddle_1_rect)
    pygame.draw.rect(game_screen, color_white, paddle_2_rect)
    pygame.draw.rect(game_screen, color_white, ball_rect)
    pygame.display.update()

    # make the ball move after 3 seconds
    if not started:
      font = pygame.font.SysFont('Consolas', 30)
      text = font.render('Press Space to Start', True, color_white)
      text_rect = text.get_rect()
      text_rect.center = (screen_width // 2, screen_height // 2)
      game_screen.blit(text, text_rect)
      pygame.display.flip()
      clock.tick(60)

    # Movement Logic
    delta_time = clock.tick(60)
    if ball_rect.left <= 0 or ball_rect.left >= screen_width:
      return # If the ball goes out of bounds, end the game
    if ball_rect.top < 0:
      ball_accel_y *= -1 # Invert vertical velocity
      ball_rect.top = 0 # Add some y to not trigger the code above
    if ball_rect.bottom > screen_height:
      ball_accel_y *= -1
      ball_rect.bottom = screen_height
    if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
      ball_accel_x *= -1
      ball_rect.left += 5
    if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
      ball_accel_x *= -1
      ball_rect.left -= 5
    if started:
      ball_rect.left += ball_accel_x * delta_time
      ball_rect.top += ball_accel_y * delta_time
    
    paddle_1_rect.top += paddle_1_move * delta_time
    paddle_2_rect.top += paddle_2_move * delta_time
    if paddle_1_rect.top < 0:
      paddle_1_rect.top = 0
    if paddle_1_rect.bottom > screen_height:
      paddle_1_rect.bottom = screen_height
    if paddle_2_rect.top < 0:
      paddle_2_rect.top = 0
    if paddle_2_rect.bottom > screen_height:
      paddle_2_rect.bottom = screen_height

if __name__ == '__main__':
  main()