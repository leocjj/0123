#!/usr/bin/python3
"""
Define a Task
"""
import random


class Task:
    # Define a Task
    def __init__(self, time):
        # Initialize a Task
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        # Return the timestamp
        return self.timestamp

    def get_pages(self):
        # Return the number of pages
        return self.pages

    def wait_time(self, current_time):
        # Return the wait time
        return current_time - self.timestamp
