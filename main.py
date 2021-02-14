import pygame
import random

# initialize pygame
pygame.init()

# create display & run update
width = 820
height = 520
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("SnakeAI")

# define colors
colors = {
    "snake_head": (0, 255, 0),
    "snake_tail": (0, 200, 0),
    "apple": (255, 0, 0)
}

# snake position with offsets
snake_pos = {
    "x": width / 2 - 10,
    "y": height / 2 - 10,
    "x_change": 0,
    "y_change": 0
}

# snake el size
snake_size = (10, 10)

# current snake movement speed
snake_speed = 10

# snake tails
snake_tails = []

# set motion immediately
snake_pos["x_change"] = -snake_speed

# food
food_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
}

food_size = (10, 10)
food_eaten = 0

# start loop
game_end = False
clock = pygame.time.Clock()

while not game_end:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    # clear screen
    display.fill((0, 0, 0))

    # move snake tails
    ltx = snake_pos["x"]
    lty = snake_pos["y"]

    for i, v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    # draw snake tails
    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tail"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])

    # draw snake
    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]

    # teleport snake, if required
    if snake_pos["x"] < -snake_size[0]:
        snake_pos["x"] = width

    elif snake_pos["x"] > width:
        snake_pos["x"] = 0

    elif snake_pos["y"] < -snake_size[1]:
        snake_pos["y"] = height

    elif snake_pos["y"] > height:
        snake_pos["y"] = 0

    # AI
    if snake_pos["y"] > food_pos["y"] and snake_pos["x"] == food_pos["x"]:
        snake_pos["x_change"] = 0
        snake_pos["y_change"] = -snake_speed

    if snake_pos["y"] < food_pos["y"] and snake_pos["x"] == food_pos["x"]:
        snake_pos["x_change"] = 0
        snake_pos["y_change"] = snake_speed

    if snake_pos["x"] > food_pos["x"] and snake_pos["y"] == food_pos["y"]:
        snake_pos["x_change"] = -snake_speed
        snake_pos["y_change"] = 0

    if snake_pos["x"] < food_pos["x"] and snake_pos["y"] == food_pos["y"]:
        snake_pos["x_change"] = snake_speed
        snake_pos["y_change"] = 0

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]])

    # draw food
    pygame.draw.rect(display, colors["apple"], [
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]])

    # detect collision with food
    if (snake_pos["x"] == food_pos["x"]
            and snake_pos["y"] == food_pos["y"]):
        food_eaten += 1
        snake_tails.append([food_pos["x"], food_pos["y"]])

        food_pos = {
            "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
        }

    # detect collision with tail
    for i, v in enumerate(snake_tails):
        if (snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
            game_end = True

    pygame.display.update()

    # set FPS
    clock.tick(30)

# close app, if required
pygame.quit()
quit()