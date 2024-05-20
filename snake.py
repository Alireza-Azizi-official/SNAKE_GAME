import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width = 600
height = 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE GAME")

clock = pygame.time.Clock()

block = 10
speed = 20

font = pygame.font.SysFont("bahnschrift", 17)
score_font = pygame.font.SysFont("comicsansms", 15)

def your_score(score):
    value = score_font.render( "Score:" + str(score), True, black)
    display.blit(value, [0, 0])

def snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, red, [x[0], x[1], block, block]) 

def message(msg, color):
    mesg = font.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x =  round(random.randrange(0, width - block) / 10.0) * 10.0
    food_y =  round(random.randrange(0, height - block) / 10.0) * 10.0

    while not game_over :
        while game_close == True:
            display.fill(blue)
            message("GAME OVER \n " + "Press C to play again \n" + "Press Q to quit", black)
            your_score(snake_length - 1 )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        pygame.draw.rect(display, color, [food_x, food_y, block, block])
        snake_head = [x1, y1]

        if len(snake_list) > snake_length :
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake_list.append(snake_head)

        snake(block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block)/ 10.0) * 10.0
            snake_length += 1
        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()