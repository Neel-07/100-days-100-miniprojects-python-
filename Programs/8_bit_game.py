import pygame
import sys
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Colox')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock and font initialization
clock = pygame.time.Clock()
font = pygame.font.SysFont('Corbel', 35)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_text('GAME OVER', WHITE, WIDTH // 2 - 150, 295)
        draw_text('Exit', WHITE, 100, HEIGHT - 100)
        draw_text('Restart', WHITE, WIDTH - 180, HEIGHT - 100)

        mouse = pygame.mouse.get_pos()
        if 100 < mouse[0] < 140 and HEIGHT - 100 < mouse[1] < HEIGHT - 80:
            pygame.draw.rect(screen, RED, [100, HEIGHT - 100, 40, 20])
        else:
            pygame.draw.rect(screen, GREEN, [100, HEIGHT - 100, 40, 20])

        if WIDTH - 180 < mouse[0] < WIDTH - 100 and HEIGHT - 100 < mouse[1] < HEIGHT - 80:
            pygame.draw.rect(screen, RED, [WIDTH - 180, HEIGHT - 100, 80, 20])
        else:
            pygame.draw.rect(screen, GREEN, [WIDTH - 180, HEIGHT - 100, 80, 20])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < mouse[0] < 140 and HEIGHT - 100 < mouse[1] < HEIGHT - 80:
                    pygame.quit()
                    sys.exit()
                elif WIDTH - 180 < mouse[0] < WIDTH - 100 and HEIGHT - 100 < mouse[1] < HEIGHT - 80:
                    game()

def game():
    lead_x = 40
    lead_y = HEIGHT // 2
    speed = 15
    count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            lead_y -= 10
        if keys[pygame.K_DOWN]:
            lead_y += 10

        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, 40])
        pygame.draw.rect(screen, RED, [0, HEIGHT - 40, WIDTH, 40])
        pygame.draw.rect(screen, GREEN, [WIDTH - 100, 0, 100, 40])

        pygame.draw.rect(screen, RED, [WIDTH - 100, 0, 100, 40])
        mouse = pygame.mouse.get_pos()

        if WIDTH - 100 < mouse[0] < WIDTH and 0 < mouse[1] < 40:
            pygame.draw.rect(screen, GREEN, [WIDTH - 100, 0, 100, 40])
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        e_p = [WIDTH, random.randint(50, HEIGHT - 50)]

        if e_p[0] > 0 and e_p[0] <= WIDTH:
            e_p[0] -= 10
        else:
            if e_p[1] <= 40 or e_p[1] >= HEIGHT - 40:
                e_p[1] = HEIGHT / 2
            e_p[1] = random.randint(50, HEIGHT - 50)
            e_p[0] = WIDTH

        if lead_x <= e_p[0] <= lead_x + 40 and lead_y >= e_p[1] >= lead_y - 40:
            game_over_screen()

        if lead_y <= e_p[1] + 50 <= lead_y + 40 and lead_x <= e_p[0] <= lead_x + 40:
            game_over_screen()

        pygame.draw.rect(screen, RED, [e_p[0], e_p[1], 50, 50])

        pygame.display.update()

        clock.tick(speed)

# Start the game
game()
