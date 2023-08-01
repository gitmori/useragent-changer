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

    # Create instance (random platform if no arguments)
    instance0 = UserAgent()

    # Call the method
    ua0 = instance0.set()

    # Create instance (set 'Android')
    instance1 = UserAgent('android')

    # Call the method
    ua1 = instance1.set()

    # Create instance (set 'Chrome')
    instance2 = UserAgent('chrome')

    # Call the method
    ua2 = instance2.set()

    # Create instance (set 'Edge')
    instance3 = UserAgent('edge')

    # Call the method
    ua3 = instance3.set()

    # Create instance (set 'Firefox')
    instance4 = UserAgent('firefox')

    # Call the method
    ua4 = instance4.set()

    # Create instance (set 'iPad')
    instance5 = UserAgent('ipad')

    # Call the method
    ua5 = instance5.set()

    # Create instance (set 'iPhone')
    instance6 = UserAgent('iphone')

    # Call the method
    ua6 = instance6.set()

    # Create instance (set 'Mac')
    instance7 = UserAgent('mac')

    # Call the method
    ua7 = instance7.set()

    # Create instance (set 'Safari')
    instance8 = UserAgent('safari')

    # Call the method
    ua8 = instance8.set()

    # Create instance (set 'Windows')
    instance9 = UserAgent('windows')

    # Call the method
    ua9 = instance9.set()

    ua_list = [ua0, ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9]

    # Test User-Agent output
    for list in ua_list:
        print(list)

if __name__ == '__main__':
    main()