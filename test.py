import engine
import pygame

game = engine.Engine()

testCircle = game.newActor(450, 300, "red", 20)

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    game.flip()

    #game.draw.draw_circle("red", 450, 300, 25)
    game.renderActors()

    game.tick()

pygame.quit()  
