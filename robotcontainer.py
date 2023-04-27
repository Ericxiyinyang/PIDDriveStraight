import wpilib
import wpilib as wp

from drivestraight import StraightDriver as SD
from gyroturn import GyroTurn
from drivetrain import Drivetrain

class RobotContainer:
    def __init__(self):
        self.controller = wp.Joystick(0)
        self.drivetrain = Drivetrain()
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Go Straight", SD(self.drivetrain))
        self.chooser.addOption("Turn 90", GyroTurn(self.drivetrain, 90))
        wpilib.SmartDashboard.putData(self.chooser)

    def get_autonomous(self):
        return self.chooser.getSelected()