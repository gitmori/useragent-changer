#!/usr/bin/env python3
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

PLATFORM= 'edge'
ua = UserAgent(PLATFORM).set()

URL = 'https://develop.tools/env-variable/'

options = ChromeOptions()
options.add_argument('--user-agent=' + ua)
driver = Chrome(options=options)
driver.get(URL)

sleep(5)
driver.quit()