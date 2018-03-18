from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

redLight = 0
blueLight = 0
greenLight = 0

@app.get('/')
def index():
	global redLight
	global blueLight
	global greenLight
	redLight = 0
	blueLight = 0
	greenLight = 0
	return template('index')

@app.get('/off')
def off():
	global redLight
	global blueLight
	global greenLight
	redLight = 0
	blueLight = 0
	greenLight = 0
	print "Turning Lights Off"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }

@app.get('/RedOn')
def RedOn():
	global redLight
	global blueLight
	global greenLight
	if redLight == 0:
		print "Turning light Red on"
		GPIO.output(8,True)
		redLight = 1
		sleep(1) # sleep for 1 second
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }

@app.get('/RedOff')
def RedOff():
	global redLight
	global blueLight
	global greenLight
	if redLight == 1:
		GPIO.output(8,False)
		redLight = 0
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }

@app.get('/BlueOn')
def BlueOn():
	global redLight
	global blueLight
	global greenLight
	if blueLight == 0:
		print "Turning light Blue on"
		blueLight = 1
		GPIO.output(12,True)
		sleep(1) # sleep for 1 second
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }

@app.get('/BlueOff')
def BlueOff():
	global redLight
	global blueLight
	global greenLight
	if blueLight == 1:
		print "Turning light Blue off"
		GPIO.output(12,False)
		sleep(1) # sleep for 1 second
		blueLight = 0
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }


@app.get('/GreenOn')
def GreenOn():
	global redLight
	global blueLight
	global greenLight
	if greenLight == 0:
		print "Turning light Green on"
		GPIO.output(10,True)
		greenLight = 1
		sleep(1) # sleep for 1 second
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }

@app.get('/GreenOff')
def GreenOff():	
	if greenLight == 1:
		print "Turning light Green off"
		# Turn LEDs on
		GPIO.output(10,False)
		greenLight = 0
		sleep(1) # sleep for 1 second
		return { "Red_Light": redLight, "Blue_Light": blueLight, "Green_Light": greenLight }


@app.get('/shutdown')
def shutdown():
	print "Shutdown"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.
	return {'Shutdown': True}

run(app, host='192.168.0.35', port=80)	