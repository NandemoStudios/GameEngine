import engine
import pygame

game = engine.Engine()

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    game.flip()

    game.draw.draw_circle("red", 450, 300, 20)

    game.tick()

pygame.quit()  
