from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255, 255, 255)

while True:
  sense.show_message("EEE is awesome!", text_colour=red, back_colour=white, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=orange, back_colour=red, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=yellow, back_colour=orange, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=green, back_colour=yellow, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=blue, back_colour=green, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=indigo, back_colour=blue, scroll_speed=0.05)
  sense.show_message("EEE is awesome!", text_colour=violet, back_colour=indigo, scroll_speed=0.05)
  

