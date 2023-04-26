import wpilib as wp
from wpilib import Joystick, Spark, Encoder
from drivetrain import Drivetrain
from drivestraight import StraightDriver
import os

class StraightRobot(wp.TimedRobot):
    def robotInit(self):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain()
        self.autodriver = StraightDriver(self.drivetrain)

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain.zeroEncoders()
        self.drivetrain.resetGyro()

    def autonomousPeriodic(self):
        self.autodriver.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        # print(forward)
        # print(rotate)
        self.drivetrain.move(-forward, rotate)

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wp.run(StraightRobot)