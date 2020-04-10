import pygame
import random
import math

clock = pygame.time.Clock()

# initialize py_game
pygame.init()

# setup or run the screen
screen = pygame.display.set_mode((800, 600))
running = True

# title
pygame.display.set_caption("Snake Game")

# Direction Values of Snake
snake_x = 380
snake_y = 280
snake_x_change = 0
snake_y_change = 0

# game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Properties of snake
ls = []
length_snake = 1
snake_speed = 15
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)


# game over function
def game_over_text():
    over_text_1 = over_font.render("GAME OVER !!", True, (225, 0, 0))
    over_text_2 = over_font.render("YOUR SCORE : " + str(score), True, (0, 255, 0))
    screen.blit(over_text_1, (200, 250))
    screen.blit(over_text_2, (160, 320))


# For Drawing Snake
def snake(ls2):
    for x in ls2:
        pygame.draw.rect(screen, (0, 225, 0), [x[0], x[1], 25, 25])


# function of score
def show_score(n):
    score2 = font.render("score :" + str(n), True, (0, 255, 0))
    screen.blit(score2, (10, 15))


def change_state():
    pygame.time.wait(500)
    return False


# Co-ordinates for food
food_x = (random.randrange(0, 766))
food_y = (random.randrange(0, 566))

# game loop
while running:

    # RGB color
    screen.fill((0, 0, 225))

    for event in pygame.event.get():

        # when game is closed
        if event.type == pygame.QUIT:
            running = False

        # for left, right, up, down moments
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -10
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 10
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -10
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = 10
                snake_x_change = 0

    # Creating condition when snake hits the boundary
    if snake_x <= 0 or snake_x >= 788:
        food_y = 2000
        food_x = 2000
        game_over_text()
        running = change_state()

    if snake_y < 0 or snake_y >= 588:
        food_y = 2000
        food_x = 2000
        game_over_text()
        running = change_state()

    snake_x += snake_x_change
    snake_y += snake_y_change

    # for drawing food
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 15, 15))

    ls.append([snake_x, snake_y])

    if len(ls) > length_snake:
        del ls[0]

    for i in ls[:-1]:
        if i == [snake_x, snake_y]:
            food_y = 2000
            food_x = 2000
            game_over_text()
            running = change_state()

    snake(ls)
    score = length_snake - 1
    show_score(score)

    # this runs the output screen and updates the screen continuously
    if math.sqrt((math.pow(snake_x - food_x, 2)) + (math.pow(snake_y - food_y, 2))) < 16:
        food_x = (random.randrange(0, 766))
        food_y = (random.randrange(0, 566))
        length_snake += 1
    pygame.display.update()
    clock.tick(snake_speed)
