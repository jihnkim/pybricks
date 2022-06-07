from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop

squared = Motor(Port.A)
pump = Motor(Port.B)
pump2 = Motor(Port.C)
squared.control.limits(1500)
pump.control.limits(1500)

while True:
    squared.run(900)
    pump.run(1300)
    pump2.run(400)
    
