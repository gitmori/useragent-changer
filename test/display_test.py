from pathlib import Path
from sys import path

test_file_path = Path(__file__)
current_dir = test_file_path.resolve().parent

# Move upper directory
path.append(str(current_dir) + '/..')

# Import modules in upper directory
from useragent_changer import UserAgent

def main():

    # Create an instance (random platform if no arguments)
    ua0 = UserAgent()

    #  Create an instance (Set 'Android' as the platform)
    ua1 =  UserAgent('android')

    # Create an instance (Set 'Chrome' as the platform)
    ua2 = UserAgent('chrome')

    # Create an instance (Set 'Edge' as the platform)
    ua3 = UserAgent('edge')

    # Create an instance (Set 'Firefox' as the platform)
    ua4 = UserAgent('firefox')

    # Create an instance (Set 'iPad' as the platform)
    ua5 = UserAgent('ipad')

    # Create an instance (Set 'iPhone' as the platform)
    ua6 = UserAgent('iphone')

    # Create an instance (Set 'Mac' as the platform)
    ua7 = UserAgent('mac')

    # Create an instance (Set 'Safari' as the platform)
    ua8 = UserAgent('safari')

    # Create an instance (Set 'Windows' as the platform)
    ua9 = UserAgent('windows')

    ua_list = [ua0.set(), ua1.set(), ua2.set(), ua3.set(), ua4.set(), ua5.set(), ua6.set(), ua7.set(), ua8.set(), ua9.set()]

    # Test User-Agent output
    for list in ua_list:
        print(list)

if __name__ == '__main__':
    main()