import sys
import pygame
import random
from agent import Agent
from map import Map

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (235, 140, 52)
grey = (150, 150, 150)
MAP_SIZE = 420
SPACE_SIZE = 20
MAP_SPACES = int(MAP_SIZE/SPACE_SIZE)


def drawSpaceEmpty(i, k, background):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(i+1, k+1, 18, 18))


def drawSpaceAgent(i, k, background):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(i+1, k+1, 18, 18))
    pygame.draw.circle(screen, red, (i+10, k+10), 6)


def drawSpaceFood(i, k, background):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(i+1, k+1, 18, 18))
    pygame.draw.circle(screen, green, (i+10, k+10), 4)


def makeLabels():
    buttonText = textFont.render('Toggle', False, orange)
    screen.blit(buttonText, (width/2+15, 550+5))

    energyLabel = textFont.render(
        'Energy: %s' % agent.getEngery(), False, orange)
    screen.blit(energyLabel, (0, 430))

    facingLabel = textFont.render(
        'Facing: %s' % agent.getFacing(), False, orange)
    screen.blit(facingLabel, (0, 460))

    VisionType = textFont.render(
        'Vision Type: %s' % agent.getSenseType(), False, orange)
    screen.blit(VisionType, (0, 550))

    SpacesInSight = textFont.render(
        'Spaces in View: %s' % numOfSpacesInSight, False, orange)
    screen.blit(SpacesInSight, (0, 520))

    foodInSightLabel = textFont.render(
        'Food In Sight: %s' % foodInSight, False, orange)
    screen.blit(foodInSightLabel, (0, 490))


pygame.init()
pygame.font.init()
textFont = pygame.font.SysFont('Monaco', 18, bold=True)

size = width, height = MAP_SIZE, MAP_SIZE+180
screen = pygame.display.set_mode(size)

map = Map(MAP_SPACES)

randomlist = random.sample(range(0, map.size()**2), 67)
for i in randomlist:
    map.placeElement((int(i/MAP_SPACES), i % MAP_SPACES), 'f')

agent = Agent((int(randomlist[66]/MAP_SPACES),
              int(randomlist[66] % MAP_SPACES)), map)

map.placeElement(agent.getPos(), 'a')


mouseDelay = 0
numOfSpacesInSight = 0
foodInSight = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                agent.move((0, -1))
            elif event.key == pygame.K_a:
                agent.move((-1, 0))
            elif event.key == pygame.K_s:
                agent.move((0, 1))
            elif event.key == pygame.K_d:
                agent.move((1, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+100 and 550 <= mouse[1] <= 550+40:
                agent.setSenseType('toggle')
            elif mouseDelay <= 0:
                mouseDelay = 25
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    print((pygame.mouse.get_pos()[0] //
                           20, pygame.mouse.get_pos()[1] // 20))

    screen.fill(black)

    for i in range(0, MAP_SIZE, SPACE_SIZE):
        for k in range(0, MAP_SIZE, SPACE_SIZE):
            if agent.senseCheck((i/SPACE_SIZE, k/SPACE_SIZE)):
                bg = grey
                numOfSpacesInSight += 1
            else:
                bg = black
            if map.get((i/SPACE_SIZE, k/SPACE_SIZE)) == 'e':
                drawSpaceEmpty(i, k, bg)
            elif map.get((i/SPACE_SIZE, k/SPACE_SIZE)) == 'f':
                drawSpaceFood(i, k, bg)
                if bg == grey:
                    foodInSight += 1
            elif map.get((i/SPACE_SIZE, k/SPACE_SIZE)) == 'a':
                drawSpaceAgent(i, k, bg)

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+100 and 550 <= mouse[1] <= 590:
        pygame.draw.rect(screen, (170, 170, 170), [width/2, 550, 100, 40])
    else:
        pygame.draw.rect(screen, (200, 200, 200), [width/2, 550, 100, 40])

    makeLabels()

    numOfSpacesInSight = 0
    foodInSight = 0
    mouseDelay -= 1

    pygame.display.flip()
