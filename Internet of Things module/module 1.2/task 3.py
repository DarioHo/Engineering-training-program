from sense_hat import SenseHat
import random
import time
sense = SenseHat()
sense.clear()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255, 255, 255)

fin_x = random.randint(0, 7)
fin_y = random.randint(0, 7)

colour = [red, orange, yellow, green, blue, indigo, violet, white]

while True:
  
  pixel_colour = random.choice(colour)
  sense.set_pixel(fin_x, fin_y, pixel_colour)
  time.sleep(1)
  sense.clear()
  
  if (fin_x == 0):
    move_x = random.randint(0,1)
    fin_x = fin_x + move_x
  elif (fin_x == 7):
    move_x = random.randint(-1,0)
    fin_x = fin_x + move_x
  else:
    move_x = random.randint(-1,1)
    fin_x = fin_x + move_x
    

  if (fin_y == 0):
    if (move_x == 0):
      move_y = 1
      fin_y = fin_y + move_y
  elif(fin_y == 7):
    if (move_x == 0):
        move_y = -1
        fin_y = fin_y + move_y
  else:
    if (move_x == 0):
        ran = [-1,1]
        move_y = random.choice(ran)
        fin_y = fin_y + move_y
    
  

    
  
