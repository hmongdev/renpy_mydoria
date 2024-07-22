label myScreens:
  
  screen mapScreen:
    add "village main" xysize(1920, 1080)
    
    # Inn
    imagebutton:
      xpos 645
      ypos 215
      auto "/gui/map/inn %s.png"
      at transform:
        xysize(154, 127)