# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
#from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from words import ScoreText

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Asteroid.containers = (asteroids, updatable, drawable)
    Asteroid.containers = (asteroids, updatable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    score_text = ScoreText(position=(SCREEN_WIDTH // 2, 30))  # Center top
    PLAYER_SCORE = 0

    dt = 0

    while True: # This will make the window's close button work:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        updatable.update(dt)   

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                print(f"Your score was: {PLAYER_SCORE}!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    if asteroid.radius == ASTEROID_MIN_RADIUS:
                        PLAYER_SCORE += 3
                    if asteroid.radius == 2 * ASTEROID_MIN_RADIUS:
                        PLAYER_SCORE += 2
                    if asteroid.radius == 3 * ASTEROID_MIN_RADIUS:
                        PLAYER_SCORE += 1
                    score_text.set_score(PLAYER_SCORE)
                    shot.kill()
                    asteroid.split()

        screen.fill("black")    # Clear screen with black   
        for obj in drawable:
            obj.draw(screen) 
        for obj in asteroids:
            if obj.radius == ASTEROID_MIN_RADIUS:
                obj.draw(screen, "white")
            if obj.radius == 2 * ASTEROID_MIN_RADIUS:
                obj.draw(screen, "yellow")
            if obj.radius == 3 * ASTEROID_MIN_RADIUS:
                obj.draw(screen, "red")
        score_text.draw(screen) 
        pygame.display.flip()   # Update the display

        dt = clock.tick(60)/1000    # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()