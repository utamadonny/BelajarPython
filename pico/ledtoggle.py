import machine

led = machine.Pin(25, machine.Pin.OUT)

led.toggle()