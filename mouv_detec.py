import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
capteur = 7

GPIO.setup(capteur, GPIO.IN)

while True:
   if GPIO.input(capteur):
      print "Mouvement detecte"
      time.sleep(1)
