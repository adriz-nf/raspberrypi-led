# Source: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
blinks = 10
for i in range(1,blinks):
  GPIO.setup(18,GPIO.OUT)
  print(f"LED on. {i} of {blinks}")
  GPIO.output(18,GPIO.HIGH)
  time.sleep(1)
  print("LED off")
  GPIO.output(18,GPIO.LOW)
