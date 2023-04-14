from EncoderConstants import EncoderConstants as EC
from EncoderConstants import MotorConstants as MC

class StraightDriver:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def run(self):
        if self.drivetrain.getAvgDistanceTravelled() == EC.intendedDistance:
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        if lTravel == rTravel:
            self.drivetrain.move(0, MC.forwardAmount)
        elif lTravel > rTravel:
            self.drivetrain.move(MC.rotateAmount, MC.forwardAmount)
        elif lTravel < rTravel:
            self.drivetrain.move(-MC.rotateAmount, MC.forwardAmount)


