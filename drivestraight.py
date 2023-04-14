from EncoderConstants import EncoderConstants as EC

class StraightDriver:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def run(self):
        if self.drivetrain.getAvgDistanceTravelled() == EC.intendedDistance:
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        if lTravel == rTravel:
            self.drivetrain.move(0, 0.5)
        elif lTravel > rTravel:
            self.drivetrain.move(0.1, 0.5)
        elif lTravel < rTravel:
            self.drivetrain.move(-0.1, 0.5)


