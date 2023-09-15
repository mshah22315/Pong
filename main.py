import pygame
from pygame.locals import *
from ball import Ball
from paddle import Paddle

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)  # Background color
WHITE = (255, 255, 255)  # Text color
WINNING_SCORE = 20  # Winning score

# Create the game screen with a black background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
screen.fill(BLACK)  # Fill the screen with black

# Create the ball and paddles
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
player_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, is_player=True)
opponent_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, is_player=False)  # Opponent's paddle

# Initialize the scoreboard text
font = pygame.font.Font(None, 36)

# Main game loop
running = True
player_score = 0
opponent_score = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and player_paddle.y > 0:
        player_paddle.y -= player_paddle.speed
    if keys[K_s] and player_paddle.y + player_paddle.height < SCREEN_HEIGHT:
        player_paddle.y += player_paddle.speed

    if keys[K_UP] and opponent_paddle.y > 0:
        opponent_paddle.y -= opponent_paddle.speed
    if keys[K_DOWN] and opponent_paddle.y + opponent_paddle.height < SCREEN_HEIGHT:
        opponent_paddle.y += opponent_paddle.speed

    # Update the ball
    ball.update(player_paddle, opponent_paddle)

    # Check for scoring
    if ball.check_score():
        if ball.out_of_bounds() == 'left':
            opponent_score += 1
        elif ball.out_of_bounds() == 'right':
            player_score += 1
        ball.reset()

    # Draw everything
    screen.fill(BLACK)  # Clear the screen with black
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)
    player_paddle.draw(screen)
    opponent_paddle.draw(screen)
    ball.draw(screen)

    # Display the score
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (20, 20))
    screen.blit(opponent_text, (SCREEN_WIDTH - opponent_text.get_width() - 20, 20))

    # Check for the winning condition
    if player_score >= WINNING_SCORE or opponent_score >= WINNING_SCORE:
        running = False  # Exit the game loop when a player wins

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
