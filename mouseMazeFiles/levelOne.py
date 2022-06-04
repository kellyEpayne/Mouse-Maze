import arcade
import mouseMazeFiles.constants as constants
from mouseMazeFiles.player import Player

class LevelOne():

    def setup(game):
        # a more advance version of a Level class

        # holds the path for the file used to set the level up
        mapName = "mouseMazeFiles/resources/LevelOne.json"

        # sets the walls and floor to use spatial_hash
        # spatial_hashing is turned on for sprites that won't be moved
        layer_options = {
            "Walls": {
                "use_spatial_hash": True
            },

            "Floor": {
                "use_spatial_hash": True
            },
        }

        # keeps scaling constant when scale is altered in constants
        tileScaling = constants.scale

        # load_tilemap is a method in arcade that can load sprite info based on the .json files the Tiled produces
        game.tile_map = arcade.load_tilemap(mapName, tileScaling, layer_options)
        game.scene = arcade.Scene.from_tilemap(game.tile_map)


        # special setup for buttons
        # Buttons are assigned a gate they control
        game.scene["Button1"].gate = 'Gate1'
        # The gate is present at the start of the level
        game.scene["Button1"].gatePresent = True
        # This level has 1 button
        game.amountButtons = 1

        # sets up the player and where they are located in the map
        game.playerSprite = Player()
        game.playerSprite.center_x = constants.screenWidth - 48 * constants.scale
        game.playerSprite.center_y = constants.screenHeight - 48 * constants.scale
        game.scene.add_sprite("Player", game.playerSprite)
        
        # This list holds all the sprites that are impassable in this level
        # All the walls and the single gate this level has
        walls = [game.scene["Walls"], game.scene["Gate1"]]

        # sets up the physics_engine the first parameter is the player, second removes the gravity, third sets the list of walls spirtes as unpassable
        game.physics_engine = arcade.PhysicsEnginePlatformer(
            game.playerSprite, gravity_constant=0, walls=walls,
        )