x1 = 0
x2 = 0
sonar_reading = 0
def avg_sonar():
    global x1, x2, sonar_reading
    x1 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    basic.pause(100)
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    basic.pause(100)
    sonar_reading = (x1 + x1) / 2
    return sonar_reading
def Rotate_R():
    cuteBot.motors(1, 15)
    basic.pause(500)
    cuteBot.motors(0, 0)
    return 0
def Rotate_L():
    cuteBot.motors(15, 1)
    basic.pause(500)
    cuteBot.motors(0, 0)
    return 0

def on_forever():
    basic.pause(200)
    avg_sonar()
    cuteBot.motors(15, 15)
    basic.pause(500)
    cuteBot.stopcar()
    Rotate_L()
    avg_sonar()
    if x2 < sonar_reading:
        cuteBot.motors(0, 0)
basic.forever(on_forever)
