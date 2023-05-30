from sense_hat import SenseHat
import random
sense = SenseHat()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255, 255, 255)

colour = [red, orange, yellow, green, blue, indigo, violet, white]


while True:
  anyText_colour = random.choice(colour)
  anyBack_colour = random.choice(colour)
  
  if anyText_colour != anyBack_colour:
    sense.show_message("EEE is awesome!", text_colour = anyText_colour, back_colour = anyBack_colour, scroll_speed=0.05)

