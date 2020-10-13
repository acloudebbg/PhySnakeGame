# Snake Game!
# First change
import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] != 0:
    print(" (!) Had {0} Initializing errors, exiting ...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play surface
playsurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake game !")

# Colors
red = pygame.Color(255, 0, 0)  # Game over
green = pygame.Color(0, 255, 0)  # Snake
blue = pygame.Color(0, 0, 255)  # To use at your discretion
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
# initial snake coordinates
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = "RIGHT"
changeto = direction

score = 0

# Game over function
def gameOver():
    myFont = pygame.font.SysFont("monaco", 80)
    GOSurf = myFont.render("Game over!", True, red)
    Gorect = GOSurf.get_rect()
    Gorect.midtop = (360, 40)
    playsurface.blit(GOSurf, Gorect)
    showScore(2)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() # pygame exit
    sys.exit() # console exit

# Show score
def showScore(choice=1):
    sFont = pygame.font.SysFont("monaco", 24)
    SSurf = sFont.render("Score : {0}".format(score),True, black)
    Srect = SSurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playsurface.blit(SSurf, Srect)
    pygame.display.flip()

#Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # validation of direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "LEFT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

    # change the direction
    if direction == "RIGHT":
        snakePos[0] += 10
    if direction == "LEFT":
        snakePos[0] -= 10
    if direction == "UP":
        snakePos[1] -= 10
    if direction == "DOWN":
        snakePos[1] += 10

    # Body update possition
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += score
        foodSpawn = False
    else:
        snakeBody.pop()

    #Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playsurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playsurface, green,pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playsurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if snakePos[0] > 720 or snakePos[0]< 0:
        gameOver()
    if snakePos[1] > 460 or snakePos[1] < 0 :
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    pygame.display.flip()
    showScore()
    fpsController.tick(15)
