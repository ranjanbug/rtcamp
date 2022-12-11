# Import the requests module to check if the site is up and healthy
import requests

# Check if the site is up and healthy
site_status = requests.get("http://example.com").status_code
if site_status == 200:
    # If the site is up and healthy, prompt the user to open it in a browser
    print("The site is up and healthy. Please open http://example.com in your browser.")
else:
    # If the site is not up and healthy, print an error message
    print("The site is not up and healthy. Please check the site status.")
