"""
Python port of @shiffman Coding Challenge #1 CC_001_StarField
For original Processing version see 
https://github.com/CodingTrain/website/tree/master/CodingChallenges/CC_001_StarField/Processing/CC_001_StarField
"""
from Star import Star

stars = []
NUM_STARS = 800

def setup():
    size(600, 600)
    for i in range(NUM_STARS):
        stars.append(Star())
        
def draw():
    speed = map(mouseX, 0, width, 0, 50)
    background(0)
    translate(width/2, height/2)
    for i in range(NUM_STARS):
        stars[i].update(speed)
        stars[i].show()
