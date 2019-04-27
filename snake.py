import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 600
display_height = 600

clock = pygame.time.Clock()
fps = 10            #laju snake
block_size = 30     #size snake

font = pygame.font.SysFont(None, 25)
direction = "a"
highscore = 0

def snake(block_size, snakeList, snakeHead, lead_x, lead_y):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, red, [XnY[0],XnY[1],block_size,block_size])       #left top width height

def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

gameDisplay = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game IS CSC 2301")

def gameLoop():
    global direction
    global highscore

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    score = 0

    randAppleX = round(random.randrange(0, display_width - block_size)/block_size)*block_size
    randAppleY = round(random.randrange(0, display_height - block_size)/block_size)*block_size

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(red)
            message_to_screen("Game over", white, 250,150)
            message_to_screen("Press ENTER to play again or ESC to quit.", white, 150, 200)
            message_to_screen(''.join(["High score: ", str(highscore)]), white, 245, 250)
            message_to_screen(''.join(["Your score was: ",str(score)]), white, 230, 300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:    #tekan enter play again
                        direction = "a"
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:    #tekan escape quit game
                        gameExit = True
                        gameOver = False
                elif event.type == pygame.QUIT:         #close window
                    gameExit = True
                    gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"

        if lead_x >= display_width or lead_x <0 or lead_y >= display_height or lead_y <0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)
        message_to_screen(''.join(["Score: ",str(score)]), white, 10,10)
        pygame.draw.rect(gameDisplay, white, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:    #len return the element
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList, snakeHead, lead_x, lead_y)

        if lead_x == randAppleX and lead_y == randAppleY:       #bila pala snake makan
            randAppleX = round(random.randrange(0, display_width - block_size)/block_size)*block_size
            randAppleY = round(random.randrange(0, display_height - block_size)/block_size)*block_size
            snakeLength += 1
            score += 1
            if score > highscore:                               #check high score
                highscore = score
            else:
                highscore = highscore
            message_to_screen(''.join(["Score: ",str(score)]), white, 10,10)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()

gameLoop()