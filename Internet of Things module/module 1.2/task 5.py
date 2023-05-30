from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
import os

sense.clear()
while True:
  
  temp = sense.get_temperature()
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      if event.direction == "up":
        print("Please press in the middle to show the temperature")
      elif event.direction == "down":
        print("Please press in the middle to show the temperature")
      elif event.direction == "left": 
        print("Please press in the middle to show the temperature")
      elif event.direction == "right":
        print("Please press in the middle to show the temperature")
      elif event.direction == "middle":
	temp = round(temp, 2)
        print(temp)
       
      # Wait a while and then clear the screen
      sleep(1)
      sense.clear()
      # clear message when the button is not pressed in the middle
      os.system('clear')
      
	  
