from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

# the original position of the ball when the game start
ball_position = [3, 3]
ball_velocity = [1, 1]
# the original bat postion when the game start
bat_pos = 4

# making a bat
def draw_bat():
  # set the bat length
  # violet is the ultimate level
  sense.set_pixel(0, bat_pos, 238, 130, 238)      #the pixel of the bat
  
# control the bat to move up
def move_up(event): 
  global bat_pos
  if bat_pos > 1 and event.action=='pressed':
    bat_pos -= 1
    
# control the bat to move down
def move_down(event):
  global bat_pos
  if bat_pos < 6 and event.action=='pressed':
    bat_pos += 1

def draw_ball():
  global ball_position
  # Draws the ball pixel
  sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
  # Moves the ball to the next position
  ball_position[0] += ball_velocity[0]
  ball_position[1] += ball_velocity[1]
    
  # the velocity is revered back to the opposite direction
  if ball_position[1] == 0 or ball_position[1] == 7:
    ball_velocity[1] = -ball_velocity[1]
  if ball_position[0] == 0 or ball_position[0] == 7:
    ball_velocity[0] = -ball_velocity[0]
    
  # the collision with the bat
  if ball_position[0] == 1 and bat_pos - 1 <= ball_position[1] <= bat_pos + 1:
    ball_velocity[0] = -ball_velocity[0]
    
  # display the "Losing message"
  if ball_position[0] == 0:
    sense.show_message("Lose :(")
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down


while True:
  sense.clear(0, 0, 0)
  #call the draw bet function
  draw_bat()
  #call the draw_ball function
  draw_ball()
  # the speed of the moving ball by controlling the time that the ball stay in a specific pixel
  sleep(0.1)

