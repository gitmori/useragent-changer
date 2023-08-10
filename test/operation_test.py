from selenium.webdriver import ChromeOptions, Chrome

from pathlib import Path
from sys import path

test_file_path = Path(__file__)
current_dir = test_file_path.resolve().parent

# Move upper directory
path.append(str(current_dir) + '/..')

# Import modules in upper directory
from useragent_changer import UserAgent
from time import sleep

# Set the platform
PLATFORM= 'android'

# Set the URL
URL = 'https://develop.tools/env-variable/'

# Create an instance
ua = UserAgent(PLATFORM)

# Set options
options = ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent=' + ua.set())

# Launch browser using 'chromedriver'
driver = Chrome(options=options)
driver.get(URL)

# Quit the browser after waiting a set number of seconds
SECONDS = 5
sleep(SECONDS)
driver.quit()