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

class Player(): 
  def __init__(self, w, h, x, y, v):
    self.w = w
    self.h = h
    self.x = x
    self.y = y
    self.v = v
    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

  def drawPlayer(self):
    print(f"x = {self.x}")
    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    pygame.draw.rect(WIN, (255, 0, 0), self.rect)

  @staticmethod
  def keyPressed(self, keys):
    if keys[pygame.K_w] and self.y - self.v >= 0:
      self.y -= self.v
    if keys[pygame.K_a] and self.x - self.v >= 0:
      self.x -= self.v
    if keys[pygame.K_s] and self.y + self.v + self.h <= HEIGHT:
      self.y += self.v
    if keys[pygame.K_d] and self.x + self.v + self.w <= WIDTH:
      self.x += self.v

def draw(p1):
  WIN.fill((0,0,0))
  p1.drawPlayer()
  print("drawing")
  pygame.display.update()
  
def main():
  run = True
  p1 = Player(10, 10, 200, 200, 5)
  clock = pygame.time.Clock()
  start_time = time.time()
  
  while run:

    clock.tick(144) # 144 fps
    elapsed_time = time.time() - start_time


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
    
    keys = pygame.key.get_pressed()
    p1.keyPressed(p1, keys)

    draw(p1)

  pygame.quit()

if __name__ == "__main__":
  main()