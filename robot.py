import wpilib as wp
from wpilib import Joystick, Spark, Encoder
from drivetrain import Drivetrain

class StraightRobot(wp.TimedRobot):
    def robotInit(self):
        self.controller = Joystick(0)

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass
