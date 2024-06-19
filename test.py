import engine
import pygame

game = engine.Engine()

dataSave = game.data.Data('GameData.txt')
LoadData = dataSave.LoadData()

x_pos = 255
y_pos = 150

print(LoadData)

x_pos = int(LoadData[0])
y_pos = int(LoadData[1])

# Makes two actors and sets the colours of them
# The first is a circle, which is red, don't have to set it to a circle
# because the default is a circle

# the second is a square, which I assign to the shape of square

testCircle = game.newActor("red")
testSquare = game.newActor("blue", shape="rectangle")

# Sets the size and position of the two actors
testCircle.setActorSize(x1=450, y1=300, radius=20)
testSquare.setActorSize(x1=225, y1=150, height=20, width=20)

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    # Checks if the W or S is pressed or if the A or D is pressed
    # Moves the character around respectively
    if game.Input.key_down('w'):
        y_pos -= 1
    elif game.Input.key_down('s'):
        y_pos += 1
    if game.Input.key_down('a'):
        x_pos -= 1
    elif game.Input.key_down('d'):
        x_pos += 1

    game.flip()

    game.renderActors()
    testSquare.MoveActor(x_pos, y_pos)

    game.tick()
dataSave.AddSaveData(x_pos)
dataSave.AddSaveData(y_pos)
dataSave.SaveData()
pygame.quit()
