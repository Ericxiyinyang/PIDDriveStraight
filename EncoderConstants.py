import math


class EncoderConstants:
    distancePerTick = (math.pi * 0.07) / (12 * 120)
    intendedDistance = 2.0


class MotorConstants:
    forwardAmount = 0.5
    rotateAmount = 0.1355
    invRotateAmount = -0.1355
    PropRotationConstant = -20
    RotationCorrectionConstant = -1/120
    IntegralRotationCorrectionConstant = -1/4000
    DerivativeRotationCorrectionConstant = -1/1000
