
# 필요한 패키지들을 import 합니다.
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait

# 컬러소터 담당 허브 객체를 생성합니다.
myHub=TechnicHub()
# 허브 port A 부분에 첫 번째 볼 분리기 모터를 연결합니다.
ballSep=Motor(Port.A)
# 최종 분류 후 투출구 부분의 모터를 port B 에 연결합니다.
sortRamp=Motor(Port.B)
# 컬러 및 거리센서를 port C 에 연결합니다.
colSensor=ColorDistanceSensor(Port.C)
print(colSensor.color())

# 초기 위치를 설정합니다.
sortRamp.run_target(600,0,Stop.BRAKE)
ballSep.run_target(500, 90,Stop.BRAKE)
wait(1000)

while True:
    while colSensor.color() == None:
        myHub.light.on(Color.WHITE)
        wait(10)
        myHub.light.off()
        wait(10)
    wait(50)
    # 볼이 들어 왔을 경우, col 변수의 값을 colSensor.color() 메서드의 리턴값으로 지정합니다.
    col=None
    while col == None or col == Color.NONE or colSensor.hsv().v <= 15:
        col=colSensor.color()
        wait(10)
    print (col)
    print(colSensor.hsv())
    print(colSensor.hsv().v)
    # col 변수 값에 따라 특정 각도로 최종 투출구 모터가 회전합니다.
    if col == Color.RED:
        sortRamp.run_target(1000, -15,Stop.BRAKE,False)
        myHub.light.on(Color.RED)
    if col == Color.YELLOW:
        sortRamp.run_target(1000, 25,Stop.BRAKE,False)
        myHub.light.on(Color.YELLOW)
    if col == Color.BLUE:
        sortRamp.run_target(1000, -40,Stop.BRAKE,False)
        myHub.light.on(Color.BLUE)
    
    ballSep.run_target(1500, 0, Stop.BRAKE)
    ballSep.run_target(1500, -270,Stop.BRAKE)
