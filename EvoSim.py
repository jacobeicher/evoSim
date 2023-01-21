import sys
import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
BOARD_SIZE = 420
SPACE_SIZE = 20
BOARD_SPACES = int(BOARD_SIZE/SPACE_SIZE)
agentPos = (0, 0)


def drawSpaceEmpty(i, k):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, black, pygame.Rect(i+1, k+1, 18, 18))


def drawSpaceAgent(i, k):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, black, pygame.Rect(i+1, k+1, 18, 18))
    pygame.draw.circle(screen, red, (i+10, k+10), 6)


def drawSpaceFood(i, k):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, black, pygame.Rect(i+1, k+1, 18, 18))
    pygame.draw.circle(screen, green, (i+10, k+10), 4)


pygame.init()
size = width, height = BOARD_SIZE, BOARD_SIZE


screen = pygame.display.set_mode(size)


board = [['e' for i in range(int(BOARD_SIZE/SPACE_SIZE))]
         for j in range(int(BOARD_SIZE/SPACE_SIZE))]

randomlist = random.sample(range(0, len(board)**2), 67)

for i in randomlist:
    board[int(i/BOARD_SPACES)][i % BOARD_SPACES] = 'f'

agentPos = (int(randomlist[66]/BOARD_SPACES),
            int(randomlist[66] % BOARD_SPACES))
board[agentPos[0]][agentPos[1]] = 'a'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill(black)
        for i in range(0, BOARD_SIZE, SPACE_SIZE):
            for k in range(0, BOARD_SIZE, SPACE_SIZE):
                if board[int(i/SPACE_SIZE)][int(k/SPACE_SIZE)] == 'e':
                    drawSpaceEmpty(i, k)
                elif board[int(i/SPACE_SIZE)][int(k/SPACE_SIZE)] == 'f':
                    drawSpaceFood(i, k)
                elif board[int(i/SPACE_SIZE)][int(k/SPACE_SIZE)] == 'a':
                    drawSpaceAgent(i, k)

        pygame.display.flip()
