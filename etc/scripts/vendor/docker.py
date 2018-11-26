import sys
import subprocess

from process import *
from exceptions import ExistCodeError
from vendor.env import Environment

root_dir = os.path.abspath(os.path.join(__file__, "../../.."))


def container_exec(service, command):
    try:
        data = Environment.read(root_dir + '/.env')

        project_name = data['COMPOSE_PROJECT_NAME']

        container_id = subprocess.check_output([
            "docker-compose", "-p", project_name, "ps", "-q", service
        ], cwd=root_dir).strip()

        if command is None:
            exec_command(["docker", "exec", "-it", container_id, "sh"])
        else:
            exec_command(["docker", "exec", container_id, "sh", "-c \"" + command + "\""])

    except ExistCodeError as error:
        print "Bad exist code: " + str(error)
        sys.exit(error.value)
