from Scripts.Execution_scripts.robot_executor import RobotExecutor
from Scripts.Execution_scripts.dashboard import execute_robotdashboard
from datetime import datetime


if __name__ == "__main__":

    time = datetime.now().strftime('%Y-%m-%d_%H-%M')

    RobotExecutor = RobotExecutor(include="tests",name="tests",timestamp=time)
    RobotExecutor.run_tests()
    execute_robotdashboard(tag="tests",log_path=f"./Results/{time}/output_test.xml")