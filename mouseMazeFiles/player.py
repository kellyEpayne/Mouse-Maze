import arcade
from mouseMazeFiles.constants import scale

class Player(arcade.Sprite):

    def __init__(self):

        super().__init__()


        self.scale = scale
        # holds a set of spirtes for the player
        self.textures = []
        # sets up the sprites for the player
        texture = arcade.load_texture("mouseMazeFiles/resources/Mouse.png")
        self.textures.append(texture)
        texture = arcade.load_texture("mouseMazeFiles/resources/Mouse.png", flipped_vertically=True)
        self.textures.append(texture)
        texture = arcade.load_texture("mouseMazeFiles/resources/MouseRight.png")
        self.textures.append(texture)
        texture = arcade.load_texture("mouseMazeFiles/resources/MouseRight.png", flipped_horizontally=True)
        self.textures.append(texture)

        # default direction for the player to face is up
        self.texture = self.textures[0]
        

    def update(self):
        # moves the player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # when there is a change in direction there is a change in the currently used sprite
        if self.change_y > 0:
            self.texture = self.textures[0]
        elif self.change_y < 0:
            self.texture = self.textures[1]
        elif self.change_x > 0:
            self.texture = self.textures[2]
        elif self.change_x < 0:
            self.texture = self.textures[3]