from EncoderConstants import EncoderConstants as EC
from EncoderConstants import MotorConstants as MC
from wpimath.controller import PIDController
from autoroutine import AutoRoutine


class StraightDriver(AutoRoutine):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        # self.kp = MC.PropRotationConstant
        self.goal = EC.intendedDistance
        self.tolerance = 3
        self.dir_pid_controller = PIDController(
            20,
            0,
            0
        )
        self.dir_pid_controller.setSetpoint(0)
        self.dir_pid_controller.setTolerance(0.05)
        self.dir_pid_controller.setIntegratorRange(-0.3, 0.3)
        self.fwd_pid_controller = PIDController(
            0.5,
            0,
            0
        )
        self.fwd_pid_controller.setSetpoint(self.goal)
        self.fwd_pid_controller.setTolerance(0.05)

    def run(self):

        if self.drivetrain.getAvgDistanceTravelled() >= self.goal:
            print("STOPPED MOVING")
            self.drivetrain.move(0, 0)

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        avgDistance = self.drivetrain.getAvgDistanceTravelled()
        diff = lTravel - rTravel
        rotate = self.dir_pid_controller.calculate(diff)
        forward = self.fwd_pid_controller.calculate(avgDistance)

        # print(f"Left traveled:{lTravel}, Right traveled:{rTravel}, Avg traveled:{self.drivetrain.getAvgDistanceTravelled()}")
        if self.dir_pid_controller.atSetpoint():
            rotate = 0
        elif self.fwd_pid_controller.atSetpoint():
            self.drivetrain.move(0, 0)
        else:
            # rotate = diff * self.kp
            self.drivetrain.move(rotate, forward)
        print(f"{forward=}, {rotate=}, distance: {self.drivetrain.getAvgDistanceTravelled()}, difference: {diff}")
