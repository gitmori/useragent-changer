# useragent-changer
A library for changing user agents in order to verify the operation of web systems.

## Features
- This package contains a total of 19,381 User-Agent data for Android (2,144), Chrome (4,996), Edge (91), Firefox (2,132), iPad (45), iPhone (750), Mac (1,739), Safari (4,952), Windows (2,532).
- User-Agent corresponding to each platform is described in 9 csv files in the data folder in this package.
- Supports Python 3.x

### Installation
Enter one of the following two commands:
```
pip install useragent-changer
```
```
pip install git+https://github.com/gitmori/useragent-changer
```

### Usage
```
from useragent_changer import UserAgent

ua = UserAgent('android')
ua.set()
# Dalvik/2.1.0 (Linux; U; Android 10; ASUS_Z01RD Build/QKQ1.191008.001)

ua = UserAgent('iphone')
ua.set()
# Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1

ua = UserAgent('ipad')
ua.set()
# Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1

ua = UserAgent('windows')
ua.set()
# Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)

ua = UserAgent('mac')
ua.set()
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0

ua = UserAgent('chrome')
ua.set()
# Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 74.0.3729.169 Safari / 537.36

ua = UserAgent('edge')
ua.set()
# Mozilla/5.0 (Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.9200

ua = UserAgent('safari')
ua.set()
# Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; ja) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.523 Mobile Safari/534.11+

ua = UserAgent('firefox')
ua.set()
# Dalvik/2.1.0 (Linux; U; Android 10; ASUS_Z01RD Build/QKQ1.191008.001)

ua = UserAgent()
ua.set()
# Get a random User-Agent
```

### Test
If you don't have Selenium installed, run the following command: `pip install selenium==4.10.0`  
Regarding Selenium versions higher than 4.10.0, I have not yet confirmed the operation.

```
from selenium.webdriver import ChromeOptions, Chrome
from useragent_changer import UserAgent
from time import sleep

PLATFORM= 'firefox'
ua = UserAgent(PLATFORM).set()

URL = 'https://develop.tools/env-variable/'

options = ChromeOptions()
options.add_argument('--user-agent=' + ua)
driver = Chrome(options=options)
driver.get(URL)

sleep(5)
driver.quit()
```

## Changelog
- 0.1.1 August 02, 2023
    - First push
- 0.2.1 August 06, 2023
    - Fixed README file, test files and version number
- 0.2.2 August 06, 2023
    - Fixed README file, test files and version number
- 0.2.3 August 06, 2023
    - Fixed README file and version number
- 0.2.4 August 06, 2023
    - Fixed README file and version number

## Author
Yuki Moriya ([gitmori](https://github.com/gitmori/))  
ym19820219@gmail.com

## Licence
Copyright (c) 2023 Yuki Moriya  
This software is released under the MIT License, see LICENSE.txt.
