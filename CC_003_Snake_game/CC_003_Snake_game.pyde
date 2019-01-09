""" for original Processing version by @shiffman see
https://github.com/CodingTrain/website/tree/master/CodingChallenges/CC_003_Snake_game/Processing/CC_003_Snake_game
"""

from Snake import Snake

scl = 10

def setup():
  global s
  size(400, 400)
  s = Snake(scl)
  frameRate(10)
  pickLocation()
  
def draw():
  background(52)
  if (s.eat(food)):
    pickLocation()
  s.death()
  s.update()
  s.show()
  fill(255, 0, 100)
  rect(food.x, food.y, scl, scl)
  
def pickLocation():
  global food
  cols = width/scl
  rows = height/scl
  food = PVector(floor(random(cols)), floor(random(rows)))
  food.mult(scl)
  
def keyPressed():
  if keyCode == UP:
    s.dir(0, -1)
  elif keyCode == DOWN:
    s.dir(0, 1)
  elif keyCode == RIGHT:
    s.dir(1, 0)
  elif keyCode == LEFT:
    s.dir(-1, 0)
  
def mousePressed():
  s.total += 1
 
