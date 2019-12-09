import pygame
import random

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 650  # meaning 600 // 20 = 30 height per block
block_size = 50

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

_COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self):
        self.x = 0
        self.y = random.sample(range(6),1)[0]
        self.x_m = self.x - 1
        self.x_t = self.x_m - 1
        self.color0 = random.sample(_COLORS, 1)[0]
        self.color1 = random.sample(_COLORS, 1)[0]
        self.color2 = random.sample(_COLORS, 1)[0]
        self.rotation = 0


def create_grid(locked_pos={}):  # *
    grid = [[(0,0,0) for _ in range(6)] for _ in range(13)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid


def get_position(shape):
    positions = [(shape.y, shape.x), (shape.y, shape.x_m), (shape.y, shape.x_t)]
    return positions


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(6) if grid[i][j] == (0,0,0)] for i in range(13)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = get_position(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def get_shape():
    return Piece()

def draw_grid(surface, grid):
    sx = 0
    sy = 0

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,0,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))

def draw_window(surface, grid):
    surface.fill((0, 0, 0))
    sx = 0
    sy = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (sx, sy, play_width, play_height), 5)

    draw_grid(surface, grid)
    #pygame.display.update()

def faller_rotate(faller):
    temp = faller.color0
    faller.color0 = faller.color1
    faller.color1 = faller.color2
    faller.color2 = temp

def main(win):  # *
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.20
    level_time = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.x += 1
            current_piece.x_m = current_piece.x - 1
            current_piece.x_t = current_piece.x_m - 1
            if not(valid_space(current_piece, grid)) and current_piece.x > 0:
                current_piece.x -= 1
                current_piece.x_m = current_piece.x - 1
                current_piece.x_t = current_piece.x_m - 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.y -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_SPACE:
                    faller_rotate(current_piece)

        shape_pos = get_position(current_piece)

        if current_piece.x > -1:
            grid[current_piece.x][current_piece.y] = current_piece.color2
        if current_piece.x_m > -1:
            grid[current_piece.x_m][current_piece.y] = current_piece.color1
        if current_piece.x_t > -1:
            grid[current_piece.x_t][current_piece.y] = current_piece.color0


        if change_piece:
            locked_positions[shape_pos[0]] = current_piece.color2
            locked_positions[shape_pos[1]] = current_piece.color1
            locked_positions[shape_pos[2]] = current_piece.color0
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(win, grid)
        pygame.display.update()

surface = pygame.display.set_mode((play_width, play_height))

run = True
while run:
    surface.fill((0,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            main(surface)

pygame.display.quit()
