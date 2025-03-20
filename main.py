import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = pygame.sprite.Group()
    AsteroidField.containers = (asteroidfield, updatable)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        #Limit to 60 FPS
        dt = clock.tick(60)/1000 
        
        

if __name__ == "__main__":
    main()
