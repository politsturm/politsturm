import os
from vendor.exceptions import ExistCodeError


def exec_command(command, suppress=False):
    """Выполнить команду"""

    if isinstance(command, list):
        command = ' '.join(command)

    if not suppress:
        print("Executing the command: " + str(command))

    cmd = os.system(command)

    if os.name == 'nt':
        exitCode = 0
    else:
        exitCode = os.WEXITSTATUS(cmd)

    if exitCode != 0:
        raise ExistCodeError(exitCode)
