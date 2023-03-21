# Source: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
def flash(blinks=10, speed=1):
  import RPi.GPIO as GPIO
  import time
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  for i in range(1,blinks):
    GPIO.setup(18,GPIO.OUT)
    print(f"LED on. {i} of {blinks}")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(speed)
    GPIO.output(18,GPIO.LOW)
    print("LED off")
    time.sleep(speed)

if __name__ == '__main__':
    import sys
    flash(*sys.argv[1:])
