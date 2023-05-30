import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

signal_led = 2
GPIO.setup(signal_led, GPIO.OUT)

red_led = 4
GPIO.setup(red_led, GPIO.OUT)

green_led = 3
GPIO.setup(green_led, GPIO.OUT)

push_button = 17
GPIO.setup(push_button, GPIO.OUT)
GPIO.setup(push_button, GPIO.IN, GPIO.PUD_UP)

red_on = GPIO.output(red_led, 1)
green_on = GPIO.output(green_led, 1)
signal_on = GPIO.output(signal_led, 1)
red_off = GPIO.output(red_led, 0)
green_off = GPIO.output(green_led, 0)
signal_off = GPIO.output(signal_led, 0)  
      
def light_on(red, green):
      if red == 1:
            GPIO.output(red_led, 1)
      if green == 1:
            GPIO.output(green_led, 1)
      if red == 0:
            GPIO.output(red_led, 0)
      if green == 0:
            GPIO.output(green_led, 0)

def signal_light(signal):
      if signal == 0:
            GPIO.output(signal_led, 0)
      if signal == 1:
            GPIO.output(signal_led, 1)
         
def light_reset():
      GPIO.output(red_led, 0)
      GPIO.output(green_led, 0)
            
def Blinking_green(duration, time_blink):
      i = 0
      while i < duration:
            light_reset()
            time.sleep(time_blink)
            light_on(0, 1)
            time.sleep(time_blink)
            i = i + (time_blink*2)
            light_reset()

def press_button():
   try:
      time.sleep(8)
      red_start_time = time.time()
      while True:
            if GPIO.input(push_button)==False:
                  start_time = time.time()
                  while (GPIO.input(push_button)==False):
                        pass
                  red_end_time = time.time()
                  end_time = time.time()
                  interval = end_time - start_time
                  print('push button pressed for', interval)
                                    
                  if (interval >= 0.5):
                        total_time = red_end_time - red_start_time
                        if total_time < 5:
                              signal_light(1)
                              wait_time = 5 - total_time
                              time.sleep(wait_time)
                              time.sleep(3)
                              signal_light(0)
                              light_reset()
                              light_show()
                              break
                                    
                        elif total_time >= 5:
                              signal_light(1)
                              time.sleep(3)
                              signal_light(0)
                              light_reset()
                              light_show()
                              break
             
   except KeyboardInterrupt:
      print ("CTRL-C: Terminating program.")
   finally:
      print("Cleaning up GPIO...")
      GPIO.cleanup()

def light_show():
      threadLock.acquire()
      light_reset()
      light_on(0,1)
      time.sleep(5)
      Blinking_green(3,0.5)
      light_on(1,0)
      threadLock.release()
      press_button()
      
while True:
      threadLock = threading.Lock()
      
      thread1 = threading.Thread(target=light_show)

      thread2 = threading.Thread(target=press_button)

      thread1.start()
      thread2.start()
      thread1.join()
      thread2.join()
            
   
   



      
