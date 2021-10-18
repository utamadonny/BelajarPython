def whatever():
	print("I am a function")
	print("I can be called")
	print("I can be used")
	print("I can be used as a function")

def suhu(temp,cel):
	cel = 0
	try:
	fahr = float(temp)
		cel = (fahr - 32.0) * 5.0 / 9.0
	except:
		print("That was not a number")
	finally:
		print("The temperature is %.2f degrees Celsius." % cel)


whatever()
print('hello world')
# suhu(10)
suhu(10,0)