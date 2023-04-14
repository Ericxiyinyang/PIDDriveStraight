import wpilib as wp
from wpilib import Joystick, Spark, Encoder
from drivetrain import Drivetrain
from drivestraight import StraightDriver

class StraightRobot(wp.TimedRobot):
    def robotInit(self):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain()
        self.autodriver = StraightDriver()

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.drivetrain.zeroEncoders()

    def autonomousPeriodic(self):
        self.autodriver.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        # print(forward)
        # print(rotate)
        self.drivetrain.move(forward, rotate)
