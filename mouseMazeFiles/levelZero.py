import arcade
from mouseMazeFiles.player import Player
import mouseMazeFiles.constants as constants

class LevelZero():

    def setup(game):
        # simplest version of a Level class

        # holds the path for the file used to set the level up
        mapName = "mouseMazeFiles/resources/LevelZero.json"

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
        
        # LevelZero has no buttons. This variable prevents the program from crashing when no buttons are present
        game.amountButtons = 0

        # sets up the player and where they are located in the map
        game.playerSprite = Player()
        game.playerSprite.center_x = 48 * constants.scale
        game.playerSprite.center_y = 48 * constants.scale
        game.scene.add_sprite("Player", game.playerSprite)

        # sets up the physics_engine the first parameter is the player, second removes the gravity, third sets the Walls spirtes as unpassable
        game.physics_engine = arcade.PhysicsEnginePlatformer(
            game.playerSprite, gravity_constant=0, walls=game.scene["Walls"]
        )