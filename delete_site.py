# Import the argparse module to parse command-line arguments
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("command", help="The subcommand to run (delete)")
args = parser.parse_args()

# Extract the command from the command-line arguments
command = args.command

# Run the subcommand
if command == "delete":
    # If the command is "delete", delete the Docker containers and local files
    subprocess.run(["docker-compose", "down", "--rmi", "all", "--volumes"])
    print("The site has been deleted.")
else:
    # If the command is not "delete", print an error message
    print("Invalid command. Please use 'delete'.")
