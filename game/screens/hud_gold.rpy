###########################################
# Gold Screen
###########################################
default gold = 100

screen hud_gold():
    frame:
        # background "#000"
        background None
        xysize 400, 60
        anchor(-3.65, -0.8)
        # pos(.9,.08)
        has hbox
        align(.5,.5)
        spacing 10
                
        # Gold Image
        add "/gui/hud/gold.png":
            fit "contain"
            xsize 50

        # Gold Count
        text "{}" .format(gold) size 50 align .98,.5