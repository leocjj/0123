import cmd, sys
from turtle import *
import configparser
import csv
import sqlite3
import tempfile

class TurtleShell(cmd.Cmd):
    intro = 'Big Mountain Interfase\n   Type help or ? to list commands.\n'
    prompt = '[BMI] '
    file = None

    def do_color(self, arg):
        color(arg.lower())
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        reset()
    def do_bye(self, arg):
        print('Thank you for using Turtle')
        return True

    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        print("Si")
        if self.file and 'playback' not in line:
            print("HN", file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    TurtleShell().cmdloop()