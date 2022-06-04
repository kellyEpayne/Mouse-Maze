import arcade
import arcade.gui

class TextButtons():
    #This class is to setup the buttons for resetting and qutting

    def __init__(self, game):
        # In charge of the UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # details on what a button looks like
        default_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 10,
            "font_color": arcade.color.BLACK,
            "border_width": 1,
            "border_color": None,
            "bg_color": None,
        }

        # holds on to the buttons
        self.v_box = arcade.gui.UIBoxLayout(vertical=False, space_between=5)

        # create the buttons
        resetButton = arcade.gui.UIFlatButton(text="Reset", width=75, style=default_style)
        quitButton = arcade.gui.UIFlatButton(text="Quit", width=75, style=default_style)

        # add the buttons to the holder
        self.v_box.add(resetButton)
        self.v_box.add(quitButton)
        
        # functions that activate when the button is clicked
        @resetButton.event("on_click")
        def on_click_reset(event):
            # textButtons was passed game so that I could call the setup() method here
            # resets the current level - nice :)
            game.setup()

        @quitButton.event("on_click")
        def on_click_quit(event):
            # built in arcade function to close the window. closed window = closed game
            arcade.close_window()

        # adds the holder the manager
        self.manager.add(
            # sets the postions for the grouped buttons
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box
            )
        )