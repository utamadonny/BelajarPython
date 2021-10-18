temp = input("Enter a number: ")
cel = 0
try:
	fahr = float(temp)
	cel = (fahr - 32.0) * 5.0 / 9.0
except:
	print("That was not a number")
finally:
	print("The temperature is %.2f degrees Celsius." % cel)