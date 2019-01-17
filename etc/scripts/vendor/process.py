# coding=utf-8
import os
from vendor.exceptions import ExistCodeError


def exec_command(command):
    """Выполнить команду"""

    cmd = os.system(command)

    if os.name == 'nt':
        exitCode = 0
    else:
        exitCode = os.WEXITSTATUS(cmd)

    if exitCode != 0:
        raise ExistCodeError(exitCode)
