# Different inventory settings are defined here
# They affect mostly the visuals of the Inventory screen and the default
# functionality of Items, like whether Usables are consumed by default.

# It has to be defined before it is used in any of the Inventory classes.
# (At the time of writing, closest is Inventory at -900)
# It also can't be below -999, that's where Ren'Py Internals are.
init offset = -966

############################
## Variables of the Inventory screen.
############################

# How many slots is the Inventory wide and high.
define inv_settings.width = 4
define inv_settings.height = 5

# Size of the Inventory
define inv_settings.main_frame_size = (1920, 1080)

# Background of the whole Inventory
define inv_settings.main_frame_image = "gui/frame.png"

# Size of one Inventory Slot
define inv_settings.slot_size = (150, 150)

# Backgrounds of an Inventory Slot that contains an Item.
define inv_settings.slot_full_idle = Frame("/gui/inventory/slot idle.png", 6, 6, 6, 6)
define inv_settings.slot_full_hover = Frame("/gui/inventory/slot hover.png", 6, 6, 6, 6)
define inv_settings.slot_full_selected = Frame("/gui/inventory/slot selected.png", 6, 6, 6, 6)
define inv_settings.slot_full_selected_hover = Frame("/gui/inventory/slot selected.png", 6, 6, 6, 6)

# Background of an Inventory Slot that is empty.
define inv_settings.slot_empty_idle = Frame("/gui/inventory/slot idle.png", 6, 6, 6, 6)
define inv_settings.slot_empty_hover = Frame("/gui/inventory/slot hover.png", 6, 6, 6, 6)

# Background of the Equipped Slot.
define inv_settings.slot_equipped_image = Frame("/gui/inventory/equip empty.png", 6, 6, 6, 6)

# A highlight effect that the Inventory Slot which holds a currently
# equipped item will have.
# Is shown *below* the item.
define inv_settings.slot_equip_empty = "/gui/inventory/equip empty.png"

# Variables that control what is showed on the Inventory screen.
# This allows the user to quickly reduce the Inventory's functionality,
# should they desire to do so.
define inv_settings.show_equipped_label = True
define inv_settings.show_equipped_slot = True
define inv_settings.show_description = True
define inv_settings.show_equip_button = True
define inv_settings.show_use_button = True
define inv_settings.show_throw_away_button = True

############################
## Variables of Item functionality
############################

# Whatever these values are, they can be overwritten in a specific Item.

# If True, usable items get removed upon use by default.
define inv_settings.consumed_on_use = True

# If True, equippable items get removed upon unequip by default.
define inv_settings.consumed_on_unequip = False

# If True, Items are stackable by default.
define inv_settings.stackable = False

# Int. Used if an Item is stackable and stack_size isn't given.
# stack_size is ignored completely by Items that aren't stackable.

# TODO: create a weight system based on character's strength
# define inv_settings.stack_size = 1