import engine
import pygame

game = engine.Engine()

testCircle = game.newActor("red")
testSquare = game.newActor("blue", shape="rectangle")

testCircle.setActorSize(x1=450, y1=300, radius=20)
testSquare.setActorSize(x1=225.0, y1=150.0, height=20.0, width=20.0)

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    game.flip()

    game.renderActors()

    game.tick()

pygame.quit()  
