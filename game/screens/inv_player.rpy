###########################################
# Inventory Screen
###########################################
screen inv_player():
    modal True

    # Inventory Frame
    frame: 
        style_prefix "inventory"
        style_suffix "main_frame"

        use hud_inv()

        # Close Backpack Button
        imagebutton:
            align(0, 1.0)
            idle "/gui/hud/bag hover.png"
            hover "/gui/hud/bag idle.png"
            action [Play("sound", "/audio/hud/inv close.ogg"), Hide(), ToggleScreen('hud_inv')]
            at transform:
                xysize(150, 150)
                
        # Inventory
        use inv_grid()
        use inv_card()
       
        # Pages
        # hbox:

        #     style_prefix "inventory_pages"
        #     style_suffix "hbox" # Style: inventory_pages_hbox

        #     # Left Arrow. Goes DOWN a Page.
        #     textbutton "<":

        #         style_suffix "hbox_left" # Style: inventory_pages_hbox_left

        #         sensitive inventory.can_change_page( -1 )
        #         action Function( inventory.change_page, -1 )

        #     # Text with the current page and total pages.
        #     # .format expects two arguments.
        #     # .get_pages_repr() returns a tuple (<current page>, <total pages>),
        #     # which is then unpacked into two arguments by the *.
        #     text "{} / {}".format( *inventory.get_pages_repr() ):

        #         style_suffix "hbox_text" # Style: inventory_pages_hbox_text

        #     # Left Arrow. Goes UP a Page.
        #     textbutton ">":

        #         style_suffix "hbox_right" # Style: inventory_pages_hbox_right

        #         sensitive inventory.can_change_page( 1 )
        #         action Function( inventory.change_page, 1 )
