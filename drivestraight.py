from EncoderConstants import EncoderConstants as EC
from EncoderConstants import MotorConstants as MC
from wpimath.controller import PIDController
from autoroutine import AutoRoutine


class StraightDriver(AutoRoutine):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.kp = MC.PropRotationConstant
        self.goal = EC.intendedDistance
        self.tolerance = 3
        self.pid_controller = PIDController(
            20,
            0,
            0
        )
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(0.05)
        self.pid_controller.setIntegratorRange(-.3, .3)

    def run(self):

        if self.drivetrain.getAvgDistanceTravelled() >= self.goal:
            print("STOPPED MOVING")
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        diff = lTravel - rTravel
        rotate = self.pid_controller.calculate(diff)
        if self.pid_controller.atSetpoint():
            rotate = 0
        print(f"Left traveled:{lTravel}, Right traveled:{rTravel}, Avg traveled:{self.drivetrain.getAvgDistanceTravelled()}")
        if lTravel == rTravel:
            self.drivetrain.move(0, MC.forwardAmount)
        else:
            rotate = diff * self.kp
            fwd = MC.forwardAmount
            self.drivetrain.move(rotate, fwd)
