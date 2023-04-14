import wpilib as wp
from wpilib import Spark, Encoder
import wpilib.drive as drive
from EncoderConstants import EncoderConstants as EC

class Drivetrain:
    def __init__(self):
        self.lMotor = Spark(0)
        self.rMotor = Spark(1)
        self.lEncoder = Encoder(4, 5)
        self.rEncoder = Encoder(6, 7)
        self.lEncoder.setDistancePerPulse(EC.distancePerTick)
        self.rEncoder.setDistancePerPulse(EC.distancePerTick)
        self.drivetrain = drive.DifferentialDrive(self.lMotor, self.rMotor)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(rotate, forward)

    def getLEncoderDistance(self):
        return self.lEncoder.getDistance()

    def getREncoderDistance(self):
        return self.rEncoder.getDistance()

    def zeroEncoders(self):
        self.lEncoder.reset()
        self.rEncoder.reset()

    def getAvgDistanceTravelled(self):
        totalTravelled = self.lEncoder.getDistance() + self.rEncoder.getDistance()
        #convert to decimal precision
        return totalTravelled/2.0


