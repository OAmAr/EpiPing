from sendsms import sendmessage
from config import data
import RPI.GPIO as GPIO
import time 
def main():
    pin = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    message = "Hi %s, this is %s, %s %s" %
        ( data["Emergency Contact Name"],
          data["My Name"],
          data["Message"],
          data["Location"])
    while not GPIO.input(pin):
        time.sleep(1)

    sendmessage(data["Emergency Contact Number"], message)


if __name__=="__main__":
    main()
