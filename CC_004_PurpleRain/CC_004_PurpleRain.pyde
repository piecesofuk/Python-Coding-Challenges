"""
Python version of @shiffman's Coding Challenge #4 
see https://github.com/CodingTrain/website/tree/master/CodingChallenges/CC_004_PurpleRain/Processing/CC_004_PurpleRain
"""

from Drop import Drop

NUM_DROPS = 150
drops = []

def setup():
  size(640, 360)
  for i in range(NUM_DROPS):
    drops.append(Drop())
  
def draw():
  background(230, 230, 250)
  
  for drop in drops:
    drop.fall()
    drop.show()

