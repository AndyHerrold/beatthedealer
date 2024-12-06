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
#Add constants from previous card game
NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King",)

FILE_RANK_NAME = ("ace", "2", "3", "3", "5", "6", "7", "8", "9", "10", "jack",
                  "queen", "king")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
STATE = ("deck", "playerhand", "dealerhand", "discarded")

DECK = 0
PLAYERHAND = 1
DEALERHAND = 2
DISCARDED = 3

class Game(simplGE.Scene):
    def __init__(self):
        super().__init__()
        self.sndShuffle = simpleGE.Sound("card-shuffle.ogg")
        self.cardSlot = CardSlot(self)
        self.cardSlot.position = (320, 240) #check
        self.setupCards()
        self.lblScore = LblScore()
        self.sprites = [self.cardSlot]
        
        self.sprites = [self.playerHand, self.dealerHand, self.lblScore,]
        
    def setupCards(self):
        self.cards[0-51]
        for cn in range(NUMCARDS):
            self.cards.append(Card(cn))
class CardSlot(simpleGE.Sprite):
    """visual element displaying card sprite
        one for every position on table"""
    def __init__(self.scene):
        super().__init__(scene)
        self.setImage("svg_playing_cards/backs/fish.svg")
        
    def process(self):
        """selects a new card when clicked"""
        if self.clicked
            cardNum = random.randrange(NUMCARDS)
            currentCard = self.scene.cards[cardNum]
            self.copyImage(currentCard.image)
#modify so no card in deck is repeated            
class Card(object):
    def__init__(self, cardNum):
        super().__init__()
        
        self.id = cardNum
        self.suit = cardNum // 13
        self.rank = cardNum % 13
        
        self.suitName = SUITNAME[self.suit]
        self.rankName = RANKNAME[self.rank]
        
        self.state = DECK
        
        #set up file name to get correct image
        self.cardFileName = "svg_playing_cards\\fronts\\"
        self.cardFileName += SUITNAME[self.suit]
        self.cardFileName += File_Rank_Name[self.rank] + ".svg"
        print(self.cardFileName)
        
        #grab and store image
        self.image = pygame.image.load(self.cardFileName)
        
        self.value = self.rank
        
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
        
class stndBtn(simpleGE.Sprite)
    def_init_(self):
        super().__init__()
        self.text = "Stand"
class Deck(object):
    def__init__(self):
        self.cards = []
        self.setDefaultDeck()
        
    def setDefaultDeck(self):#come back to this
        
    def showDeck(self):
        for card in self.cards:
            if card.state == DECK:
                card.display()
                
    def showHand(self):
        for card in self.cards:
            if card.state == Hand:
                card.display()
#figure out how to replace print state ments with copying image to delerHnd and playerHand                
    def showDiscard(self):
        for card in self.cards:
            if card.state == DISCARD:
                card.display()
    
    def showAllCards(self):
        for card in self.cards:
            card.displayShort()
        print()
        
    def shuffle(self):
        """returns used cards back into deck"""
        print("shuffling")
        for card in self.cards:
            if card.state == DISCARD:
                card.state = DECK
                
    def cardsInDeck(self):
        cardsLeft = 0
        for cards in self.cards:
            if card.state == DECK:
                cardsLeft += 1
        return cardsLeft

    def discard(self, cardNum):
        hand = []
        for card in self.cards:
            if card,state == HAND
                hand.append(card)
                
        currentCard = hand[cardNum]
        currentCard.state = DISCARD
        
    def deal(self, numCards):
        for cardNum in range(numCards):
            if self.cardsInDeck() <= 0:
                self.shuffle()
                
            keepGoing = True
            while keepGoing:
                currentCard = random.choice(self.cards) #figure out distributing cards between dealer and player
                if currentCard.state == DECK:
                    currentCard.state = HAND
                    keepGoing = False
        
class Instructions(simpleGE.Scene):
    def__init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore
        self.setImage("lasvegas.jpg")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textlines = [
        "You are the gambler", #Define controls for double down and split with corresponding text instructions
        "Hit with left arrow key, stand with right arrow key",
        "Beat the dealers hand total without exceeding 21",
        "Dealer stands on 17 or greater. "
        "",
        "Good Luck!"]
        
        self.directions.center = (320, 200)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (550, 400)
        
        self.lblScore = simplGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)
        
        self.lblScore.text = f"Last score: {self.prevScore}"
        
        self.sprites = [self.directions, self.btnPlay, self.btnQuit, self.lblScore]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop() 
        
        
        
        
        
        
        
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

