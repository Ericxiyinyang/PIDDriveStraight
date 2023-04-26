from drivetrain import Drivetrain as DT
from EncoderConstants import MotorConstants as MC

class GyroTurn:
    def __init__(self, drivetrain: DT, goal: float):
        self.drivetrain = drivetrain
        self.goal = goal
        self.kp = MC.GyroRotationCorrectionConstant

    def run(self):
        error = self.drivetrain.getGyroAngleZ() - self.goal
        if abs(error) < 1:
            #got there and we should stop
            return
        else:
            power = error * self.kp
            self.drivetrain.move(power, 0)