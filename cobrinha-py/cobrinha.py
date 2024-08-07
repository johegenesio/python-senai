import pygame
import time
import random

pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Cobrinha')

green_fill = (94,179,79)
green_cs = (124,204,110)
green_s = (154,255,137)
orange_f = (255,166,112)

game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_b = 20
snake_speed = 5
snake_list = []
Length_of_snake = 1

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, orange_f, [x[0], x[1], snake_b, snake_b])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50, dis_height/2])

foodx = round(random.randrange(0, dis_width-snake_b)/20)*20
foody = round(random.randrange(0, dis_height-snake_b)/20)*20

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_b
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = snake_b
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_b
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_b

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change

    dis.fill(green_fill)

    pygame.draw.rect(dis, orange_f, [foodx, foody, snake_b, snake_b],0,4)

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    if len(snake_list) > Length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_Head

    pygame.draw.rect(dis,green_s,[x1,y1,snake_b,snake_b],0,4)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width-snake_b)/20)*20
        foody = round(random.randrange(0, dis_height-snake_b)/20)*20

    clock.tick(snake_speed)

message('Você perdeu!', green_s)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()