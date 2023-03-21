# Source: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
def flash(blinks=5, ms=500):
  import RPi.GPIO as GPIO
  import time
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  for i in range(1,blinks+1):
    GPIO.setup(18,GPIO.OUT)
    print(f"LED on. {i} of {blinks}")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(ms/1000)
    GPIO.output(18,GPIO.LOW)
    print("LED off")
    time.sleep(ms/1000)

if __name__ == '__main__':
    import sys
    flash(int(sys.argv[1]), int(sys.argv[2]))
