class player:    
    def __init__(self):
        self.hand= []
        
    def remove_card(self, c):
        print(c)
        print(self.__str__())
        self.hand.remove(c)

    def add_card(self,c):
        self.hand.append(c)
        
    def __str__(self):
        res = ''
        for i in self.hand:
            res += str(i) + '\n'
        return res
    

    