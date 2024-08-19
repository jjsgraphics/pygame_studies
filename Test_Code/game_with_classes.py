import pygame
import time
import random
import math
pygame.font.init()

class Player:
  # Set player values
  P1_WIDTH = 50
  P1_HEIGHT = 40
  P1_INITIAL_X = 100
  P1_INITIAL_Y = 100
  P1_VEL = 20
  
  def __init__(self, w, h, x, y, v):
    self.w = w
    self.h = h
    self.x = x
    self.y = y
    self.v = v

class Star:
  # Set star values
  STAR_RADIUS = 10
  STAR_VEL = 15
  
class Game:
  @staticmethod
  def keyPressed(player, keys):
    if keys[pygame.K_w] and player.y - p1.v >= 0:
      player.y -= p1.v
    if keys[pygame.K_a] and player.x - p1.v >= 0:
      player.x -= p1.v
    if keys[pygame.K_s] and player.y + p1.v + p1.height <= HEIGHT:
      player.y += p1.v
    if keys[pygame.K_d] and player.x + p1.v + p1.width <= WIDTH:
      player.x += p1.v

#  We need to create a window (TOP LEFT IS 0,0. DOWN IS +Y, RIGHT IS +X)
WIDTH, HEIGHT = 2100,900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gaming time mfers")

# Add a BG image
BG = pygame.image.load("assets/Monitor34.png")
BGScaled = pygame.transform.scale(BG, (WIDTH,HEIGHT))

FONT = pygame.font.SysFont("Arial", 20)

def draw(p1, elapsed_time, stars): # order matters, things drawn first will be underneath first
  WIN.blit(BGScaled, (0, 0))

  time_text = FONT.render(f"Time: {round(elapsed_time, 1)}s", 1, "white") #f string turns it all into a string, 1 adds antialiasing
  WIN.blit(time_text,(10, 10))

  pygame.draw.rect(WIN, (255,0,0), p1)

  for star in stars:
    pygame.draw.rect(WIN, "white", star)

  pygame.display.update() #need to update before new drawings r applied



# create a main game loop
def main():
  run = True
  p1 = pygame.Rect(P1_INITIAL_X, P1_INITIAL_Y, P1_WIDTH, P1_HEIGHT)
  clock = pygame.time.Clock()

  start_time = time.time()
  elapsed_time = 0

  star_add_increment = 2000
  star_counter = 0
  stars = []
  hit = False

  while run:
    star_counter += clock.tick(144) # 144 fps
    elapsed_time = time.time() - start_time

    if star_counter > star_add_increment: # once the counter has hit the threshold, spawn another star
      for i in range(15):
        star_x = random.randint(0, WIDTH - STAR_RADIUS)
        star = pygame.Rect(star_x, -STAR_RADIUS, STAR_RADIUS, STAR_RADIUS)
        stars.append(star)
      star_add_increment = max(500, star_add_increment - 100) # each loop it goes down 50 (initially 2000), but the minimum value between star spawns is 200 
      star_counter = 0

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
    
    keys = pygame.key.get_pressed()
    Game.keyPressed(p1, keys)

    for star in stars[:]: # the colon clones the list so the list
      star.y += STAR_VEL + random.randrange(0, 5)
      x_increment = math.sin((star.y + random.randrange(0, 100))/70) * 5
      star.x += x_increment
      #print(x_increment)
      if star.y > HEIGHT: # if the star is below the screen, delete it
        stars.remove(star)
      elif star.y >= p1.y and star.colliderect(p1):
        stars.remove(star)
        hit = True
        break

      if hit:
        lost_text = FONT.render("You Lost!", 1, "white")
        WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2)) #generate text in the centre
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
        break

    draw(p1, elapsed_time, stars)
  
  pygame.quit()


# only if the file is run directly then the game runs
if __name__ == "__main__":
  main()