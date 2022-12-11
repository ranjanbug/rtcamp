# Import the argparse module to parse command-line arguments
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("site_name", help="The name of the site to create the /etc/hosts entry for")
args = parser.parse_args()

# Extract the site name from the command-line arguments
site_name = args.site_name

# Create the /etc/hosts entry for the site
with open("/etc/hosts", "a") as f:
    f.write("localhost " + site_name + "\n")
