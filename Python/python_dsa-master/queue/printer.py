#!/usr/bin/python3
"""
Define a Printer
"""


class Printer:
    # Define a Printer
    def __init__(self, ppm):
        # Initialize a Printer
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        # Decrement the timer and set the Printer to idle if task is completed
        if self.current_task is not None:
            self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.current_task = None

    def busy(self):
        # Check if the Printer is busy
        return self.current_task is not None

    def start_next(self, new_task):
        # Start the next task
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate
