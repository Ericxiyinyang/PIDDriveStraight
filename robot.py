import wpilib as wp
from wpilib import Joystick, Spark, Encoder
from drivetrain import Drivetrain
from drivestraight import StraightDriver
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from robotcontainer import RobotContainer
from autoroutine import AutoRoutine

class StraightRobot(wp.TimedRobot):
    def robotInit(self):
        self.container = RobotContainer()

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.container.drivetrain.zeroEncoders()
        self.container.drivetrain.resetGyro()
        self.auto = self.container.get_autonomous()

    def autonomousPeriodic(self) -> AutoRoutine:
        self.auto.run()


    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        # print(forward)
        # print(rotate)
        self.container.drivetrain.move(-forward, rotate)

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wp.run(StraightRobot)
    window = tk.Tk()
    label = tk.Label(text="Python rocks!")
    label.pack()

    window.mainloop()