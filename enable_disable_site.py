# Import the argparse module to parse command-line arguments
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("command", help="The subcommand to run (enable or disable)")
args = parser.parse_args()

# Extract the command from the command-line arguments
command = args.command

# Run the subcommand
if command == "enable":
    # If the command is "enable", start the Docker containers
    subprocess.run(["docker-compose", "up", "-d"])
    print("The site is enabled.")
elif command == "disable":
    # If the command is "disable", stop the Docker containers
    subprocess.run(["docker-compose", "stop"])
    print("The site is disabled.")
else:
    # If the command is not "enable" or "disable", print an error message
    print("Invalid command. Please use 'enable' or 'disable'.")
