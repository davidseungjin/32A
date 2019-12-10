#######################################
# Student ID    : 001037870
# UCInetID      : seungl21
# Name          : Seungjin Lee
#######################################

import pygame
import project5_faller as pm

play_width = 300
play_height = 650
block_size = 50
myline = (128, 128, 128)
myviolet = (255, 0, 255)

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

def get_faller():
    return pm.Faller()

def draw_grid(surface, grid):
    for i in range(len(grid)):
        pygame.draw.line(surface, myline, (0, 0 + i*block_size), (0 + play_width, 0 + i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, myline, (0 + j*block_size, 0),(0 + j*block_size, 0 + play_height))

def draw_window(surface, grid):
    surface.fill((0, 0, 0))
    sx = 0
    sy = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (0 + j*block_size, 0 + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, myviolet, (0, 0, 0 + play_width, 0 + play_height), 10)
    draw_grid(surface, grid)

def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    c_player = get_faller()
    n_player = get_faller()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick(30)

        if fall_time/1000 > fall_speed:
            fall_time = 0
            c_player.x += 1
            c_player.x_m = c_player.x - 1
            c_player.x_t = c_player.x_m - 1
            if not(valid_space(c_player, grid)) and c_player.x > 0:
                c_player.x -= 1
                c_player.x_m = c_player.x - 1
                c_player.x_t = c_player.x_m - 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    c_player.y -= 1
                    if not(valid_space(c_player, grid)):
                        c_player.y += 1
                if event.key == pygame.K_RIGHT:
                    c_player.y += 1
                    if not(valid_space(c_player, grid)):
                        c_player.y -= 1
                if event.key == pygame.K_SPACE:
                    c_player.faller_rotate()

        faller_pos = get_position(c_player)

        if c_player.x > -1:
            grid[c_player.x][c_player.y] = c_player.color2
        if c_player.x_m > -1:
            grid[c_player.x_m][c_player.y] = c_player.color1
        if c_player.x_t > -1:
            grid[c_player.x_t][c_player.y] = c_player.color0

        if change_piece:
            locked_positions[faller_pos[0]] = c_player.color2
            locked_positions[faller_pos[1]] = c_player.color1
            locked_positions[faller_pos[2]] = c_player.color0
            c_player = n_player
            n_player = get_faller()
            change_piece = False
        draw_window(win, grid)
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((play_width, play_height))

    run = True
    try:
        while run:
            surface.fill((0,0,0))
            pygame.display.update()
            for event in pygame.event.get():
                main(surface)
    finally:
        pygame.quit()
