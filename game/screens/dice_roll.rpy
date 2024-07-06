default dice_size = 250

# label dice roll
label dice_roll(dice, faces, bonus = 0):
    $ dice_audio = renpy.random.randint(1, 8)
    $ roll = renpy.random.randint(1, faces)
    $ dice_total = 0
    
    # randomize dice rolls
    while dice > 0:
        play sound (f"/audio/dice/{dice_audio}.ogg")
        # if roll is 1
        if roll == 1:
            pause 2.0 
            play sound "/audio/dice/d1.ogg"
        # if roll is 20
        if roll == 20:
            pause 2.0 
            play sound "/audio/dice/d20.ogg"
        $ dice_total += roll
        $ dice -= 1
    $ dice_total += bonus
return

# dice text
screen dice_text():
    frame:
        background None at top
        xysize(dice_size, dice_size)
        text "[dice_total]" size 85 align((0.535, 0.4)) outlines [(5, "#2c1401", 0, 0)]
    timer 2.0 action Hide()

# dice roll
screen dice_roll():
    frame:
        background None at top
        xysize(dice_size, dice_size)
        add "/images/dice/d20.png":
            xysize(dice_size, dice_size) 
            align((0.5, 0.5)) at dice_spin, dice_alpha
        timer 1.0 action Show("dice_text")
    timer 3.0 action Hide()

# dice spin animation
transform dice_spin():
    easeout_back 1.0 rotate 1080

# dice transition animation
transform dice_alpha():

    on show:
        alpha 0.0
        easein 2.0 alpha 1.0

    on hide:
        alpha 1.0
        easeout 1.0 alpha 0.0 yoffset 300