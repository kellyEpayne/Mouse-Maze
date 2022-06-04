import mouseMazeFiles.constants as constants
import arcade
from mouseMazeFiles.textButtons import TextButtons
from mouseMazeFiles.levelZero import LevelZero
from mouseMazeFiles.levelOne import LevelOne
from mouseMazeFiles.levelTwo import LevelTwo

class Game(arcade.Window):
    def __init__(self):

        super().__init__(constants.screenWidth, constants.screenHeight, constants.screenTitle)

        # These will be altered by the LevelNumber classes - these change everytime setup is called
        self.tile_map = None
        self.scene = None
        self.playerSprite = None
        self.physics_engine = None
        self.level = 0
        self.wallsRemoved = 0
        self.amountButtons = 0
        
        # These are set once
        self.movementSpeed = 4
        self.textButtons = TextButtons(self)
        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):

        if self.level == 0:
            LevelZero.setup(self)
        elif self.level == 1:
            LevelOne.setup(self)
        elif self.level == 2:
            LevelTwo.setup(self)
        else:
            # If the level number doesn't match a current level the level number will be set to zero and the player will be sent to the first level
            self.level = 0
            self.setup()

    def on_draw(self):
        
        # Arcade will draw these things in this order
        self.clear()
        self.scene.draw()
        # This is drawn on the highest level
        self.textButtons.manager.draw()

    def on_key_press(self, key, modifiers):
        # modifiers is not used but when I removed it in early development the program broke

        if key == arcade.key.W:
            self.playerSprite.change_y = self.movementSpeed
        elif key == arcade.key.S:
            self.playerSprite.change_y = -self.movementSpeed
        elif key == arcade.key.A:
            self.playerSprite.change_x = -self.movementSpeed
        elif key == arcade.key.D:
            self.playerSprite.change_x = self.movementSpeed


    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.W:
            self.playerSprite.change_y = 0
        elif key == arcade.key.S:
            self.playerSprite.change_y = 0
        elif key == arcade.key.A:
            self.playerSprite.change_x = 0
        elif key == arcade.key.D:
            self.playerSprite.change_x = 0

    def on_update(self, delta_time):
        # special collison cases
        
        self.physics_engine.update()
        self.playerSprite.update()

        # arcade.check_for_collision returns true or false
        cheese_collect_check = arcade.check_for_collision(
            # Levels are to be built with only 1 cheese
            self.playerSprite, self.scene["Cheese"][0]
        )

        # on contact with cheese the player moves to the next level
        if cheese_collect_check:
            self.level +=1
            self.setup()


        # on contact with the player boxes will be added to a list
        box_push = arcade.check_for_collision_with_list(
            self.playerSprite, self.scene["Boxes"]
        )

        # with this box list loop through the list to push the box
        for box in box_push:
            # moves the box
            box.center_x += self.playerSprite.change_x *2
            box.center_y += self.playerSprite.change_y *2

            # check to see if the box is touching a wall
            walls_hit = arcade.check_for_collision_with_lists(
                box, self.physics_engine.walls
            )

            # if the box touches the walls - prevent the box from going into the wall - prevent the player from going into the box
            if walls_hit:
                # anti wall
                box.center_x -= self.playerSprite.change_x *2
                box.center_y -= self.playerSprite.change_y *2
                # anti box
                self.playerSprite.center_x -= self.playerSprite.change_x *2
                self.playerSprite.center_y -= self.playerSprite.change_y *2


        
        # loops through the amount of buttons because some levels have 0 to 4 buttons
        for buttonNum in range(1, self.amountButtons + 1):

            # buttons are placed in Tiled as layers name like Button1
            button = self.scene[f"Button{buttonNum}"]

            # One button per layer
            # check to see if there is a box or player on the button
            button_pressed = arcade.check_for_collision_with_lists(button[0], [self.scene["Boxes"], self.scene["Player"]])

            # if there is a player or box on the button enter this if statment
            if button_pressed:
                # if this buttons .gatePresent is True
                # .gatePresent is set for each button in the Level classes
                if button.gatePresent:
                    gate = button.gate
                    # Hides the gate from the player
                    self.scene[gate].visible = False
                    # toggles .gatePresent
                    button.gatePresent = False
                    # removes that gate layer from the physics_engine walls list
                    self.physics_engine.walls.remove(self.scene[gate])

            # there is nothing pressing the button
            else:
                # if the buttons gate is invisble
                if button.gatePresent == False:
                    gate = button.gate
                    # let the player see the gate
                    self.scene[gate].visible = True
                    # adds the gate back to the physics_engine walls list
                    self.physics_engine.walls.append(self.scene[gate])
                    # toggles .gatePresent to True
                    button.gatePresent = True

    
#def testMain():
#    #for testing
#    window = Game()
#    window.setup()
#    arcade.run()
#
#testMain()