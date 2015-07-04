import RPi.GPIO as GPIO
import time
class Servo:

	def __init__(self, pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)
		self.freq = 50
		self.ms = 1000 / self.freq
		self.pos = 1.625 
		self.pwm = GPIO.PWM(pin, self.freq)
		self.pwm.start(self.pos * 100 / self.ms)

	def center(self):
		self.pos = 1.625
		self.turn()

	def right(self, degree):
		self.pos += float(degree) * .00972	
		if self.pos > (2.5):
			self.pos = 2.5
		self.turn()

	def left(self, degree):
		self.pos -= float(degree) * .00972	
		if self.pos < (0.75):
			self.pos = 0.75 
		self.turn()

	def turn(self):
		duty = self.pos * 100 / self.ms 

		print self.pos
		print duty
		self.pwm.ChangeDutyCycle(duty)
		time.sleep(0.5)

	def exit(self):
		self.pwm.stop()
		GPIO.cleanup()
	
