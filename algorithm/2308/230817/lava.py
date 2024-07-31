import pygame
import random

pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("지렁이 게임")

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 2, screen_height / 2])

running = True
game_over = False

x1 = screen_width / 2
y1 = screen_height / 2

x1_change = 0
y1_change = 0

snake_list = []
length_of_snake = 1

foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

while running:
    while game_over == True:
        screen.fill(white)
        message("게임 오버! 다시 하려면 Q, 끝내려면 C", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = True
                    game_over = False
                    x1 = screen_width / 2
                    y1 = screen_height / 2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    length_of_snake = 1
                    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
                if event.key == pygame.K_c:
                    running = False
                    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    our_snake(snake_block, snake_list)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        length_of_snake += 1

    clock.tick(snake_speed)

pygame.quit()
