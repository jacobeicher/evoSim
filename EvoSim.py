import sys
import pygame
import random
from agent import Agent
from map import Map
from space import Food, Empty

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (235, 140, 52)
grey = (150, 150, 150)
MAP_SIZE = 840
SPACE_SIZE = 40
MAP_SPACES = int(MAP_SIZE/SPACE_SIZE)


def drawSpaceEmpty(i, k, background):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(
        i+1, k+1, SPACE_SIZE - 2, SPACE_SIZE - 2))


def drawSpaceAgent(i, k, background):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(
        i+1, k+1, SPACE_SIZE - 2, SPACE_SIZE - 2))
    pygame.draw.circle(screen, red, (i+SPACE_SIZE/2, k+SPACE_SIZE/2), 6)


def drawSpaceFood(i, k, background, food):
    pygame.draw.rect(screen, white, pygame.Rect(i, k, SPACE_SIZE, SPACE_SIZE))
    pygame.draw.rect(screen, background, pygame.Rect(
        i+1, k+1, SPACE_SIZE - 2, SPACE_SIZE - 2))
    pygame.draw.circle(screen, green, (i+SPACE_SIZE/2,
                       k+SPACE_SIZE/2), food.getRadius())


def makeLabels():
    buttonText = textFont.render('Toggle', False, orange)
    screen.blit(buttonText, (width/3+10, MAP_SIZE + 65))

    energyLabel = textFont.render(
        'Energy: %s' % agent.getEngery(), False, orange)
    screen.blit(energyLabel, (0, MAP_SIZE + 10))

    facingLabel = textFont.render(
        'Facing: %s' % agent.getFacing(), False, orange)
    screen.blit(facingLabel, (0, MAP_SIZE + 40))

    VisionType = textFont.render(
        'Vision Type: %s' % agent.getSenseType(), False, orange)
    screen.blit(VisionType, (0, MAP_SIZE + 70))

    SpacesInSight = textFont.render(
        'Spaces in View: %s' % numOfSpacesInSight, False, orange)
    screen.blit(SpacesInSight, (0, MAP_SIZE + 100))

    foodInSightLabel = textFont.render(
        'Food In Sight: %s' % foodInSight, False, orange)
    screen.blit(foodInSightLabel, (0, MAP_SIZE + 130))


pygame.init()
pygame.font.init()
textFont = pygame.font.SysFont('Monaco', 20, bold=True)

size = width, height = MAP_SIZE, MAP_SIZE+180
screen = pygame.display.set_mode(size)

map = Map(MAP_SPACES)

startingPlacements = random.sample(range(0, map.size()**2), 67)
for i in startingPlacements:
    map.placeElement((int(i/MAP_SPACES), i % MAP_SPACES),
                     Food(random.randint(1, 6)))

agent = Agent((int(startingPlacements[66] / MAP_SPACES),
               int(startingPlacements[66] % MAP_SPACES)), map)

map.placeElement(agent.getPos(), agent)


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
            if width/3 <= mouse[0] <= width/3+100 and MAP_SIZE + 60 <= mouse[1] <= MAP_SIZE + 60+40:
                agent.setSenseType('toggle')
            elif mouseDelay <= 0:
                mouseDelay = 25
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    print((pygame.mouse.get_pos()[0] //
                           SPACE_SIZE, pygame.mouse.get_pos()[1] // SPACE_SIZE))

    screen.fill(black)

    for i in range(0, MAP_SIZE, SPACE_SIZE):
        for k in range(0, MAP_SIZE, SPACE_SIZE):
            if agent.senseCheck((i/SPACE_SIZE, k/SPACE_SIZE)):
                bg = grey
                numOfSpacesInSight += 1
            else:
                bg = black
            if isinstance(map.get((i/SPACE_SIZE, k/SPACE_SIZE)), Empty):
                drawSpaceEmpty(i, k, bg)
            elif isinstance(map.get((i/SPACE_SIZE, k/SPACE_SIZE)), Food):
                drawSpaceFood(i, k, bg, map.get((i/SPACE_SIZE, k/SPACE_SIZE)))
                if bg == grey:
                    foodInSight += 1
            elif isinstance(map.get((i/SPACE_SIZE, k/SPACE_SIZE)), Agent):
                drawSpaceAgent(i, k, bg)

    mouse = pygame.mouse.get_pos()

    if width/3 <= mouse[0] <= width/3+100 and 550 <= mouse[1] <= 590:
        pygame.draw.rect(screen, (170, 170, 170), [
                         width/3, MAP_SIZE + 60, 100, 40])
    else:
        pygame.draw.rect(screen, (200, 200, 200), [
                         width/3, MAP_SIZE + 60, 100, 40])

    makeLabels()

    numOfSpacesInSight = 0
    foodInSight = 0
    mouseDelay -= 1

    pygame.display.flip()
