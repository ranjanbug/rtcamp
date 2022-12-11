# Import the argparse module to parse command-line arguments
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("site_name", help="The name of the WordPress site to be created")
args = parser.parse_args()

# Extract the site name from the command-line arguments
site_name = args.site_name

# Create the WordPress site
subprocess.run(["docker-compose", "run", "--rm", "wordpress", "wp", "core", "download"])
subprocess.run(["docker-compose", "run", "--rm", "wp", "config", "create", "--dbname=" + site_name, "--dbuser=wp", "--dbpass=wp", "--dbhost=db", "--extra-php", "define('FS_METHOD', 'direct');"])
