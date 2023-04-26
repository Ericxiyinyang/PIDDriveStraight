from EncoderConstants import EncoderConstants as EC
from EncoderConstants import MotorConstants as MC

class StraightDriver:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.kp = MC.PropRotationConstant

    def run(self):

        if self.drivetrain.getAvgDistanceTravelled() >= EC.intendedDistance:
            print("STOPPED MOVING")
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        diff = lTravel - rTravel
        print(f"Left traveled:{lTravel}, Right traveled:{rTravel}, Avg traveled:{self.drivetrain.getAvgDistanceTravelled()}")
        if lTravel == rTravel:
            self.drivetrain.move(0, MC.forwardAmount)
        else:
            rotate = diff * self.kp
            fwd = MC.forwardAmount
            self.drivetrain.move(rotate, fwd)


