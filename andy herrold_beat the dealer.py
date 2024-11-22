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
class Taxi(simpleGE.Sprite):
    def__init__(self, scene):
        super().__init__(scene)
        self.setImage("?")
        self.setSize(25, 25)