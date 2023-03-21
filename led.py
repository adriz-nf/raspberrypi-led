# Source: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
def flash(blinks=5, ms=500, pin=18):
  import RPi.GPIO as GPIO
  import time
  blinks = int(blinks)
  ms = int(ms)/1000
  pin = int(pin)
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  for i in range(1,blinks+1):
    GPIO.setup(pin,GPIO.OUT)
    print(f"LED on. {i} of {blinks}")
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(ms)
    GPIO.output(pin,GPIO.LOW)
    print("LED off")
    time.sleep(ms)

def double_flash():
  
  for i in range(10): 
    flash(blinks=1, ms=500, pin=18)
    flash(blinks=1, ms=500, pin=23)
  
  
  
if __name__ == '__main__':
    import sys
    #flash(*sys.argv[1:])
    double_flash()
