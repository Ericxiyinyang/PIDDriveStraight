from drivetrain import Drivetrain as DT
from EncoderConstants import MotorConstants as MC
from wpimath.controller import PIDController
from autoroutine import AutoRoutine


class GyroTurn(AutoRoutine):
    def __init__(self, drivetrain: DT, goal: float):
        self.drivetrain = drivetrain
        self.goal = goal
        self.tolerance = 3
        self.pid_controller = PIDController(
            MC.GyroRotationCorrectionConstant,
            MC.GyroIntegralRotationCorrectionConstant,
            MC.GyroDerivativeRotationCorrectionConstant
        )
        self.pid_controller.setSetpoint(self.goal)
        self.pid_controller.setTolerance(self.tolerance)
        self.pid_controller.setIntegratorRange(-.3, .3)
        #self.kp = MC.GyroRotationCorrectionConstant
        #self.ki = MC.GyroIntegralRotationCorrectionConstant
        self.total_error = 0

    def run(self):
        current_reading = self.drivetrain.getGyroAngleZ()
        power = self.pid_controller.calculate(current_reading)
        #error = current_reading - self.goal
        #self.total_error += error
        #self.total_error=min(200, max(-200, self.total_error))

        if self.pid_controller.atSetpoint():
            # turn is good enough
            self.drivetrain.move(0, 0)
        else:
            #power = error * self.kp + self.total_error * self.ki
            #power = max(-0.5, min(0.5, power))
            print(f"{current_reading=} {power=}")
            self.drivetrain.move(power, 0)
