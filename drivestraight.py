class StraightDriver:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def run(self):
        if self.drivetrain.getAvgDistanceTravelled() == 2.0:
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        if lTravel == rTravel:
            self.drivetrain.move(0.5, 0)
        elif lTravel > rTravel:
            self.drivetrain.move(0.5, 0.1)
        elif lTravel < rTravel:
            self.drivetrain.move(0.5, -0.1)


