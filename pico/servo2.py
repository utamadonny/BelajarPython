import time
import machine

pwm=machine.PWM(machine.Pin(0))
pwm.freq(1000)

def PosToDuty(pos):
  return int((1.5 + (pos / 180)) * 65535 / 20 + 0.5)
  
pos = 90
pwm.duty_u16(PosToDuty(pos))
# time.sleep(100)
# pos = 90
# pwm.duty_u16(PosToDuty(pos))
# time.sleep(100)
# pos = -90
# pwm.duty_u16(PosToDuty(pos))
# time.sleep(100)
# pos = 90
# pwm.duty_u16(PosToDuty(pos))
# time.sleep(100)