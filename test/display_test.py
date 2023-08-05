#!/usr/bin/env python3
from pathlib import Path
from sys import path

test_file_path = Path(__file__)
current_dir = test_file_path.resolve().parent

# Move upper directory
path.append(str(current_dir) + '/..')

# Import modules in upper directory
from useragent_changer import UserAgent

def main():

    # Create an instance and call the method (random platform if no arguments)
    ua0 = UserAgent().set()

    #  Create an instance and call the method (set 'Android')
    ua1 =  UserAgent('android').set()

    # Create an instance and call the method (set 'Chrome')
    ua2 = UserAgent('chrome').set()

    # Create an instance and call the method (set 'Edge')
    ua3 = UserAgent('edge').set()

    # Create an instance and call the method (set 'Firefox')
    ua4 = UserAgent('firefox').set()

    # Create an instance and call the method (set 'iPad')
    ua5 = UserAgent('ipad').set()

    # Create an instance and call the method (set 'iPhone')
    ua6 = UserAgent('iphone').set()

    # Create an instance and call the method (set 'Mac')
    ua7 = UserAgent('mac').set()

    # Create an instance and call the method (set 'Safari')
    ua8 = UserAgent('safari').set()

    # Create an instance and call the method (set 'Windows')
    ua9 = UserAgent('windows').set()

    ua_list = [ua0, ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9]

    # Test User-Agent output
    for list in ua_list:
        print(list)

if __name__ == '__main__':
    main()