#!/usr/bin/python
#coding: latin-1

import RPi.GPIO as GPIO

# Selecciona numeración de pines 
# BCM es nro de gpio
# BOARD es nro de pin (indicado en placa)

pinNumber = 12

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNumber, GPIO.OUT) #configura como salida 
#GPIO.output(pinNumber, False) 	#manejo individual

p = GPIO.PWM(pinNumber, 1) #configura pwm en pin, freq=1Hz


for i in range(0,100,5): # aumenta de a 5
    p.start(i)
    s = raw_input(str(i)+"% enter para continuar.")
 
print "fin"
s = raw_input("enter para salir")
GPIO.cleanup()