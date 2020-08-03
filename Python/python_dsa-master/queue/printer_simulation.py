#!/usr/bin/python3
"""
Run the printer simulation
"""
from queue import Queue
from printer import Printer
from task import Task
import random


def simulation(seconds, ppm, students, tasks_per_student):
    # Run the printer simulation
    printer = Printer(ppm)
    queue = Queue()
    waiting_time = []

    for second in range(seconds):
        if new_print_task(students, tasks_per_student):
            task = Task(second)
            queue.enqueue(task)

        if not printer.busy() and not queue.is_empty():
            next_task = queue.dequeue()
            waiting_time.append(next_task.wait_time(second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_time) / len(waiting_time)
    print('Average wait %5d seconds %2d tasks remaining.' %
          (average_wait, queue.size()))


def new_print_task(students, tasks_per_student):
    # Generate a new task for the printer on average once every 180 seconds
    tasks_per_hour = 3600 // (students * tasks_per_student)
    return random.randrange(1, tasks_per_hour + 1) == tasks_per_hour

if __name__ == '__main__':
    # Run simulation for one hour at 5 ppm vs. 10 ppm
    # Assume 10 students each printing 2 tasks per hour
    print('\nFive pages per minute:\n')
    for i in range(10):
        simulation(3600, 5, 10, 2)
    print('\nTen pages per minute:\n')
    for i in range(10):
        simulation(3600, 10, 10, 2)
