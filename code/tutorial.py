import pygame

pygame.init()

WHITE = (255,255,255)
size = [400,300]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60,45))

def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_RIGHT:
                    x += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
            if y>=280 or y<-20:
                x = 20
                y = 24
            elif x>=380 or x<-20:
                x = 20
                y = 24
        screen.blit(airplane, (x,y))
        pygame.display.update()

runGame()
pygame.quit()