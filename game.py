from card import card
from player import player
import numpy as np
import serial
import sys
import time
sys.path.insert(1, 'OpenCV-Playing-Card-Detector-master')
from CardDetector import identify_card

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

class game:
    def __init__(self):
        self.deck = []
        self.initialize_deck()
   
        self.p1 = player()
        self.p2 = player()

        self.topCard = self.select_card()
        self.currentTurn = 1
        for _ in range(0,7):
            self.p1.add_card(self.select_card())
            self.p2.add_card(self.select_card())
        #self.topcard= current_top_card
        # self.turn 
    
    def initialize_deck(self):
        for c in ['R' , 'G' ,'B' ,'Y']:
            for n in range (-2, 10):
                # if n == 7:
                #     continue
                self.deck.append(card(c,n))
        
        self.deck.append(card('W',-4))
        self.deck.append(card('W',-4))
        self.deck.append(card('W',0))
        self.deck.append(card('W',0))
        
    
    def select_card(self):
        c = np.random.choice(self.deck)
        self.deck.remove(c)
        return c
        
    def turn(self, turnCard):
        if (self.currentTurn == 1):
            self.p1.remove_card(turnCard)
            self.topCard = turnCard
            self.currentTurn = 2
        elif (self.currentTurn == 2):
            self.reset()
            while True:
                self.move_a_card()
                col, num = identify_card()
                print(turnCard)
                if (turnCard == card(col, num)):
                    self.p2.remove_card(turnCard)
                    break
            self.topCard = turnCard
            self.currentTurn = 1
        
        
    
    # def play_card(self, topCard, card):
    #    pass
    # def uno(self):
    #    pass 
    
    def cpu_choose_card(self):
        t = self.p2.hand
        for c in t:
            print(c.number)
            if (self.topCard.number == c.number) or (self.topCard.color == c.color) :
                self.turn(c)
                return
        for c in t:
            if (c.color == 'W') :
                self.turn(c)
                return

        drawCard = self.select_card()
        self.p2.add_card(drawCard)
        self.currentTurn = 1
                
        

    def move_a_card(self):
        a = arduino.write(bytes("1", 'utf-8'))
        time.sleep(0.05)
    
    def reset(self):
        a = arduino.write(bytes("2", 'utf-8'))
        time.sleep(0.5)



        

g = game()
print("Player 1 Hand")
print(g.p1)
print("Player 2 Hand")
print(g.p2)
print("Top Card")
print(g.topCard)

a = arduino.readline()
while not ((a == b'played\r\n') or (a == b'skipped\r\n')) :#
    a = arduino.readline()
    #print(a)
    
print(a)
if a == b'played\r\n':
    #try:
    col, num = identify_card()
    ca = card(col, int(num))
    g.turn(ca)
    #print("test")
    #except ValueError:
    #    col, num = identify_card()
    #    g.turn(card(col, num))
else:
    #some function to draw a card
    g.reset()
    newCard = g.select_card()
    while True:
        g.move_a_card()
        col, num = identify_card()
        if (newCard == card(col, num)):
            g.p1.add_card(newCard)
            g.currentTurn = 2
            break

print("Player 1 Hand")
print(g.p1)
print("Player 2 Hand")
print(g.p2)
print("Top Card")
print(g.topCard)

g.cpu_choose_card()

#print("Top Card")
#print(g.topCard)

#g.turn(card(input("Color"), int(input("number"))))
print("Player 1 Hand")
print(g.p1)
print("Player 2 Hand")
print(g.p2)
print("Top Card")
print(g.topCard)