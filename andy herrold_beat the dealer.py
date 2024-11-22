#Andy Herrold
#beat the dealer
import random
import pygame
import SimpleGE
"""
beatthedealer.py
final project
AndyHerrold
"""
# I need to figure out how to assign SVG card to player and dealer hand
class playerHand(simpleGE.Sprite):
    def__init__(self, scene):
        super()__init__(scene)
        self.setImage("?")
        self.setSize(25, 25)
        self.reset()
        
class dealerHand(simpleGE.Sprite):
    def__init__(self, scene):
        super().__init__(scene)
        self.setImage("?")
        self.setSize(25, 25)
        
class lblScore(simpleGe.Sprite):
    def__init__(self):
        super().__init__()
        self.text = "Score: 10"
        self.center (100, 30) # try different positions
        
class hitBtn(simpleGE.Sprite):
    def_init_(self):
        super().__init__()
        self.text = "Hit"
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    
    keepGoing = True
    lastScore = 0
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            LastScore = game.score
        else:
            keepGoing = False
        
        
        
        

if __name__==__ "main__":
    main()

