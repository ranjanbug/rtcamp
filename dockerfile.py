# Import the subprocess module to run system commands
import subprocess

# Check if docker is installed
check_docker = subprocess.run(["docker", "--version"])
if check_docker.returncode != 0:
    # If docker is not installed, install it
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "docker-ce"])

# Check if docker-compose is installed
check_compose = subprocess.run(["docker-compose", "--version"])
if check_compose.returncode != 0:
    # If docker-compose is not installed, install it
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "docker-compose"])
