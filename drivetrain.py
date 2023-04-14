import wpilib as wp
from wpilib import Spark, Encoder

class Drivetrain:
    def __init__(self):
        self.lMotor = Spark(0)
        self.rMotor = Spark(1)
        self.lEncoder = Encoder(4, 5)
        self.rEncoder = Encoder(6, 7)

