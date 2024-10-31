import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SAVING SALMAN")

# Load images
salman_image = pygame.transform.scale(pygame.image.load("assets/salman.png"), (140, 140))  # Increased size of Salman
obstacle_images = [
    pygame.transform.scale(pygame.image.load(f"assets/obstacle{i}.png"), (100, 100)) for i in range(1, 7)  # Decreased size of obstacles
]
background_start = pygame.transform.scale(pygame.image.load("assets/background_start.png"), (WIDTH, HEIGHT))
background_game = pygame.transform.scale(pygame.image.load("assets/background_game.png"), (WIDTH, HEIGHT))
background_win = pygame.transform.scale(pygame.image.load("assets/background_win.png"), (WIDTH, HEIGHT))
background_end = pygame.transform.scale(pygame.image.load("assets/background_end.png"), (WIDTH, HEIGHT))

# Define colors
WHITE = (255, 255, 255)

# Function to draw text
def draw_text(text, size, color, center, screen):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen.blit(text_surface, text_rect)

# Start screen
def start_screen():
    while True:
        screen.blit(background_start, (0, 0))
        draw_text("SAVING SALMAN", 74, WHITE, (WIDTH // 2, HEIGHT // 2 - 50), screen)
        draw_text("START", 48, WHITE, (WIDTH // 2, HEIGHT // 2 + 50), screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (WIDTH // 2 - 60 < mouse_x < WIDTH // 2 + 60 and
                    HEIGHT // 2 + 30 < mouse_y < HEIGHT // 2 + 70):
                    return  # Start the game

# Main game function
def main_game():
    clock = pygame.time.Clock()
    salman_rect = salman_image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    obstacles = []
    score = 500  # Start score at a higher value to avoid instant game over
    target_score = 5000  # Define a target score for winning

    # Function to generate obstacles
    def spawn_obstacle():
        obstacle = random.choice(obstacle_images)
        obstacle_rect = obstacle.get_rect(center=(random.randint(0, WIDTH - 50), 0))
        return obstacle, obstacle_rect

    # Initial obstacle generation
    for _ in range(5):
        obstacles.append(spawn_obstacle())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Control SALMAN
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and salman_rect.top > 0:
            salman_rect.y -= 5
        if keys[pygame.K_s] and salman_rect.bottom < HEIGHT:
            salman_rect.y += 5
        if keys[pygame.K_a] and salman_rect.left > 0:
            salman_rect.x -= 5
        if keys[pygame.K_d] and salman_rect.right < WIDTH:
            salman_rect.x += 5

        # Update obstacles with slower speed from the top
        for obstacle_index, (obstacle_image, obstacle_rect) in enumerate(obstacles):
            obstacle_rect.y += 1  # Reduced speed from 2 to 1
            if obstacle_rect.top > HEIGHT:
                obstacles[obstacle_index] = spawn_obstacle()  # Respawn obstacle
                score += 100  # Increase score for dodging an obstacle

            # Collision detection
            if salman_rect.colliderect(obstacle_rect):
                score -= 50  # Decrease score on collision
                obstacles[obstacle_index] = spawn_obstacle()  # Respawn obstacle

        # Check for win condition
        if score >= target_score:
            win_screen()
            return

        # Check for game over condition
        if score < 0:
            end_screen()
            return

        # Draw everything
        screen.blit(background_game, (0, 0))
        screen.blit(salman_image, salman_rect)
        for obstacle_image, obstacle_rect in obstacles:
            screen.blit(obstacle_image, obstacle_rect)

        # Draw the score at the bottom
        draw_text(f'Score: {score}', 36, WHITE, (WIDTH // 2, HEIGHT - 30), screen)

        pygame.display.flip()
        clock.tick(60)

# End screen
def end_screen():
    while True:
        screen.blit(background_end, (0, 0))
        draw_text("SALMAN DIED", 74, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), screen)
        draw_text("OK", 48, WHITE, (WIDTH // 2, HEIGHT // 2 + 50), screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # Go back to start screen

# Win screen
def win_screen():
    while True:
        screen.blit(background_win, (0, 0))
        draw_text("SALMAN LIVES", 74, (0, 255, 0), (WIDTH // 2, HEIGHT // 2), screen)
        draw_text("OK", 48, WHITE, (WIDTH // 2, HEIGHT // 2 + 50), screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # Go back to start screen

# Main execution loop
if __name__ == "__main__":
    while True:
        start_screen()
        main_game()
