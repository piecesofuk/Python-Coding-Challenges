class Snake:
  def __init__(self, scl):
    self.x = 0
    self.y = 0
    self.xspeed = 1
    self.yspeed = 0
    self.total = 0
    self.tail = []
    self.scl = scl

  def eat(self, pos):
    d = dist(self.x, self.y, pos.x, pos.y);
    if d < 1:
      self.total += 1
      return True
    else:
      return False

  def dir(self, x, y):
    self.xspeed = x;
    self.yspeed = y;

  def death(self):
    for item in self.tail:
      pos = item
      d = dist(self.x, self.y, pos.x, pos.y)
      if d < 1:
        print("starting over")
        total = 0
        tail = []

  def update(self):
    if self.total > 0:
      if self.total == len(self.tail) and len(self.tail) > 0:
        self.tail = self.tail[1:]
      self.tail.append(PVector(self.x, self.y))

    self.x = self.x + self.xspeed*self.scl
    self.y = self.y + self.yspeed*self.scl

    self.x = constrain(self.x, 0, width-self.scl)
    self.y = constrain(self.y, 0, height-self.scl)

  def show(self):
    fill(255)
    for v in self.tail:
      rect(v.x, v.y, self.scl, self.scl)
    rect(self.x, self.y, self.scl, self.scl)