#Return the probability of exactly one head in three flips

#out of 8 difference out comes of flipping coin 3 times

def  myfun(p):
    return 3 * p * (1-p)*(1-p)

print(myfun(0.5))

#2 COINS
#Return the probability of flipping one head each from two coins
#One coin has a probability of heads of p1 and the other of p2

def coins2fun(p1,p2):
    return p1*p2