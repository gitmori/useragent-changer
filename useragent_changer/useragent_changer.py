#!/usr/bin/env python3
from pathlib import Path
from os import listdir
from random import randint
from csv import reader

# class definition (Randomly set platform name if no arguments)
class UserAgent:
    def __init__(self, selector = ''):
        self.file_path = Path(__file__)
        self.platform_dir = 'platform_list'
        self.selector = selector
        self.platform_name = self.platform()
        self.csv = self.csv_path()

    # Method to set the platform
    def platform(self):
        dir_path = self.file_path.resolve().parent

        # List of configurable platforms
        platform_list = listdir(str(dir_path) + '/' + self.platform_dir)

        # Number of configurable platforms
        num = len(platform_list)

        # Range of random numbers when setting the platform to random
        rnd = randint(0, num - 1)

        # Set platform as return value
        for i in range(0, num):
            if self.selector == platform_list[i].replace('.csv', ''):
                return self.selector
            elif self.selector == '':
                return platform_list[rnd].replace('.csv', '')

    # A method to generate the path of the CSV file that describes the User-Agent of the platform set above
    def csv_path(self):

        # Generate relative path of CSV file describing User-Agent
        relative_path = self.platform_dir + '/' + self.platform_name + '.csv'

        # Generate the absolute path of the CSV file from the above
        absolute_path = self.file_path.resolve().parent.joinpath(relative_path)

        # Set the absolute path of the above CSV file as the return value
        return absolute_path

    # Method to set User-Agent randomly from inside CSV file
    def set(self):

        # Initialize the list to store the User-Agent in the CSV file
        ua_list = []

        # Initialize the counter
        count = 0

        # Read a CSV file containing User-Agent data
        with open(self.csv) as f:
            lists = reader(f)

            # Loop through the User-Agent data listed in the CSV file
            for row in lists:

                # Store User-Agent in list
                ua_list.append(str(row[0]))

                # Count the number of User-Agents
                count += 1

        # Set random number in list
        rnd = randint(0, count - 1)

        # Set User-Agent randomly
        useragent = ua_list[rnd]

        # Set the above as the return value
        return useragent