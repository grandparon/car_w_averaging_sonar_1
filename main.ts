let x1 = 0
let x2 = 0
let sonar_reading = 0
function avg_sonar () {
    x1 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    basic.pause(100)
    x2 = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    basic.pause(100)
    sonar_reading = (x1 + x1) / 2
    return sonar_reading
}
function Rotate_R () {
    cuteBot.motors(1, 15)
    basic.pause(500)
    cuteBot.motors(0, 0)
    return 0
}
function Rotate_L () {
    cuteBot.motors(15, 1)
    basic.pause(500)
    cuteBot.motors(0, 0)
    return 0
}
basic.forever(function () {
    basic.pause(200)
    avg_sonar()
    cuteBot.motors(15, 15)
    basic.pause(500)
    cuteBot.stopcar()
    Rotate_L()
    avg_sonar()
    if (x2 < sonar_reading) {
        cuteBot.motors(0, 0)
    }
})
