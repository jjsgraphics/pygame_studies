import pygame
import time
import random
import math
pygame.font.init()

#  We need to create a window (TOP LEFT IS 0,0. DOWN IS +Y, RIGHT IS +X)
WIDTH = 2100
HEIGHT = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gaming time mfers")



class Object():
  def __init__(self, w, h, x, y):
    self.w = w
    self.h = h
    self.x = x
    self.y = y
    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

  def drawObject(self):
    print(type(self))
    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    pygame.draw.rect(WIN, (255, 0, 0), self.rect)


class Player(Object): 
  g = 0.1
  
  def __init__(self, w, h, x, y):
    super().__init__(w, h, x, y)
    self.vx = 1
    self.vy = 0
    self.fall_count = 0

  def loop(self, fps):
    self.vy += min(1, (self.fall_count / fps) * self.g)
    print(self.vy)
    self.y += self.vy
    self.fall_count += 1

  def jump():
    # set y velocity to 0 
    pass
  
  @staticmethod
  def keyPressed(self, keys):
    if keys[pygame.K_w] and self.y - self.vy >= 0:
      self.y -= self.vy
    if keys[pygame.K_a] and self.x - self.vx >= 0:
      self.x -= self.vx
      # displacement = u + a * t
    #if keys[pygame.K_s] and self.y + self.vy + self.h <= HEIGHT:
    #  self.y += self.vy
    if keys[pygame.K_d] and self.x + self.vx + self.w <= WIDTH:
      self.x += self.vx


class Level:
  def __init__(self):
    self


class Platform(Object):
  def __init__(self, w, h, x, y):
    super().__init__(w, h, x, y)


def draw(objs):
  WIN.fill((0,0,0))
  for object in objs:    
    object.drawObject()
  pygame.display.update()


def main():
  run = True
  fps = 144
  p1 = Player(10, 10, 200, 200)
  pl1 = Platform(2700, 200, 0, 700)
  clock = pygame.time.Clock()
  start_time = time.time()

  while run:
    clock.tick(fps) # 144 fps
    elapsed_time = time.time() - start_time

    #p1.y += p1.vy

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
    
    keys = pygame.key.get_pressed()
    p1.keyPressed(p1, keys)
    p1.loop(fps)

    objs = [p1, pl1] # objects to draw
    draw(objs)
    #pygame.display.update()

  pygame.quit()

if __name__ == "__main__":
  main()