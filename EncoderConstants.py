import math


class EncoderConstants:
    distancePerTick = (math.pi * 0.07) / (12 * 120)
    intendedDistance = 2.0

class MotorConstants:
    forwardAmount = 0.5
    rotateAmount = 0.1
