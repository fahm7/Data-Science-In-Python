#we have a bag full of coins , each of this coins may be different  ,
# one coin have  aprobablity of landing a heads of 0.5 ,
# another coin have probablity of landing a head he 0.1 ,

# Now aim going draw one coin from this bad and i will flip it  repetitively, each time i flip it ,
# I would like you to tell me  , WHAT IS your guess in for the probablity of it being heads on the next flip


#Bayes rule tells us that the probability of the coin selected being a given coin is equal
# to the probability of flip being what it was that its head or tails,
# given coin i times probablity of coin i being the coin divided by
# the probablity of Flip , heads or tails

from __future__ import division
class FlipPredictor(object):
    def __init__(self,coins):
        self.coins = coins
        n = len(coins)
        self.probs = [1 / n] * n

    def pheads(self):
        return sum(pcoin * p for pcoin, p in zip(self.coins, self.probs))

    def update(self, result):
        pheads = self.pheads()
        if result == 'H':
            self.probs = [pcoin * p / pheads for pcoin, p in zip(self.coins, self.probs)]
        else:
            self.probs = [(1 - pcoin) * p / (1 - pheads) for pcoin, p in zip(self.coins, self.probs)]


def test(coins,flips):
    f=FlipPredictor(coins)
    gueses=[]
    for flip in flips:
        f.update(flip)
        gueses.append(f.pheads())
    return gueses

print (test([0.5,0.4,0.3],"HHTH"))