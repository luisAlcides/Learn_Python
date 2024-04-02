import pygame
import random


pygame.init()

# setting up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

game_over = False
white = (255, 255, 255)
black= (0, 0, 0)
red = (213, 50, 80)

score = 0

x1 = window_width / 2
y1 = window_height / 2

x1_change = 0
y1_change = 0

snake_body = []
length_of_snake = 1

foodx = round(random.randrange(0, window_width-10) / 10) * 10
foody = round(random.randrange(0, window_height-10) / 10) * 10


clock = pygame.time.Clock()
fps = 15


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # check for arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change

    if x1 < 0:
        x1 = 0
    elif x1 > window_width - 10:
        x1 = window_width - 10
    if y1 < 0:
        y1 = 0
    elif y1 > window_height - 10:
        y1 = window_height - 10

    window.fill(black)

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)

    if len(snake_body) > length_of_snake:
        del snake_body[0]

    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    font_style = pygame.font.SysFont(None, 50)
    score_text = font_style.render('Score: ' + str(score), True, white)
    window.blit(score_text, (10, 10))

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width-10) / 10) * 10
        foody = round(random.randrange(0, window_height-10) / 10) * 10
        length_of_snake += 1
        score += 1

    pygame.draw.rect(window, red, [foodx, foody, 10, 10])
    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], 10, 10])
    pygame.display.update()

    clock.tick(fps)