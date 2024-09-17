import pygame
from constants import *
from player import *
from astreoid import *
from astroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.isCollide(player):
                print("Game Over!")
                exit()
            
            for shot in shots:
                if asteroid.isCollide(shot):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()