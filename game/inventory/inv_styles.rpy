###########################################
#
# Inventory Screen Styles

##########################
## The Main Frame
##########################

# Main window of the Inventory.
style inventory_main_frame:
    background "#2b2929ce"
    xysize inv_settings.main_frame_size
    align (0.5, 0.4)

##########################
## The Grid with Slots
##########################

# Grid of the Item Slots
style inventory_slots_grid:
    left_margin 75
    yalign 0.45
    # yoffset 0
    xspacing 5
    yspacing 5

# One Slot for an Item inside the grid, when the slot is full.
style inventory_slot:
    # idle_background inv_settings.slot_full_idle
    # hover_background inv_settings.slot_full_hover
    # selected_idle_background inv_settings.slot_full_selected
    # selected_hover_background inv_settings.slot_full_selected_hover
    xysize inv_settings.slot_size

# One Slot for an Item inside the grid, when the slot is empty.
style inventory_slot_empty:
    idle_background inv_settings.slot_empty_idle
    hover_background inv_settings.slot_empty_hover
    xysize inv_settings.slot_size

# Text - Number of items on the stack.
style inventory_slot_text:
    align (1.0, 1.0)
    offset (-8, 0)
    bold True
    size 48
    color "#ffda46"
    outlines [ (absolute(2), "000", absolute(1), absolute(2)) ]

# Vbox holding the Equippable and Usable indicators.
style inventory_slot_indicator_hbox:
    xalign 1.0
    offset (-10, 10)

##########################
## Inventory Card
##########################

style inventory_card_frame:
    background "/gui/inventory/card basic.png"
    align((0.4, 0.5))
    ysize 800
    xsize 568

style inventory_card_frame_image:
    # background "#fff"
    xysize(482, 352)
    align(.5, 0.2)

# Selected Item's Name.
style inventory_card_name:
    align((0.22, 0.055))
    color "#1a1a1a"
    size 40

style inventory_card_kind:
    align((0.12, 0.605))
    size 35
    italic True
    color "#000"

style inventory_card_frame_description:
    # background "#ffffffff" # width of the description
    left_margin 10
    pos((0.07, 0.635))
    xysize((480, 219))

# Selected Item's Description.
style inventory_card_description:
    size 25
    italic True
    color "#1a1a1a"

##########################
##  Equip Screen
##########################

# Frame that contains everything in the Side Menu.
style inventory_side_menu_frame:
    # background Solid("000") # Great for testing, shows the Frame.
    background "/gui/inventory/frame alt 1.png"
    xysize(400, 800)
    align (1.0, 0.5)
    xoffset -50

#-----------------------------------------------------
# Vbox of Equipped Item and its Slot.
#-----------------------------------------------------

# Vbox that contains the "Equipped Item" label, 
# and the Equipped Slot.
style inventory_side_menu_vbox_equipped:
    xalign 0.5
    spacing 5
    ypos 30

# The "Equipped Item" label.
# Has no properties at the time of writing.
# style inventory_side_menu_vbox_equipped_text:
#     example 123

# The Equipped Slot.
style inventory_side_menu_vbox_equipped_slot:
    # background inv_settings.slot_equipped_image
    xysize (150, 150)
    align(0.0, 0.5)

#-----------------------------------------------------
# Vbox of Interactables (Buttons)
#-----------------------------------------------------

# Vbox that contains:
# Hbox containing Equip and Unequip buttons 
# Use button
# Throw Away button.
style inventory_buttons_frame:
    xysize (568, 60)

# Hbox containing Equip and Unequip buttons.
style inventory_buttons_equip_box:
    background "#000"
    xalign 0.5
    spacing 75

#---------------

# The Unequip textbutton.
# style inventory_buttons_unequip_textbutton:
#     background "#ff0000"

# The Unequip Text
style inventory_buttons_unequip_textbutton_text:
    xalign 0.5
    insensitive_color "#4b4848ff"
    idle_color"#c8aa00"
    hover_color "#605100"

#---------------

# The Equip textbutton.
style inventory_buttons_equip_textbutton:
    background None

# The Equip Text
style inventory_buttons_equip_textbutton_text:
    xalign 0.5
    insensitive_color "#4b4848ff"
    idle_color "#605100"
    hover_color "#c8aa00"

#---------------

# The Use textbutton.
# Has no properties at the time of writing.
# style inventory_buttons_use_textbutton:
#     example 123

# The Use textbutton - Text part.
style inventory_buttons_use_textbutton_text:
    insensitive_color '#272727ff'
    idle_color "#18750f"
    hover_color "#27ba1a"

#---------------

# The Throw Away textbutton.
style inventory_buttons_discard_textbutton:
    xalign 0.5

# The Throw Away textbutton - Text part.
style inventory_buttons_discard_textbutton_text:
    insensitive_color '#272727ff'
    idle_color "#690000"
    hover_color "#860000"
    

#-----------------------------------------------------
# Others
#-----------------------------------------------------

# The Return textbutton.
style inventory_side_menu_return_textbutton:
    align (0.5, 1.0)
    yoffset -10

# The Return textbutton - Text part.
style inventory_side_menu_return_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

##########################
## Pages 
##########################

# Hbox containing:
# Left Arrow
# Text Current/Last page
# Right Arrow
style inventory_pages_hbox:
    xanchor 0.5
    align((0.235, 0.80))
    spacing 30

# The Left Arrow textbutton. 
# Has no properties at the time of writing, 
# but has to be defined. Background already is None.
style inventory_pages_hbox_left:
    background None    

# The Left Arrow textbutton - Text part. 
style inventory_pages_hbox_left_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
    size 42

#---------------

# The Right Arrow textbutton. 
# Has no properties at the time of writing, 
# but has to be defined. Background already is None.
style inventory_pages_hbox_right:
    background None

# The Right Arrow textbutton - Text part. 
style inventory_pages_hbox_right_text:
    size 42
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

#---------------

# The Current/Last Page text. 
style inventory_pages_hbox_text:
    ypos 7