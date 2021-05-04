#!/usr/bin/env python3
import subprocess
from time import sleep, strftime
from datetime import datetime

if __name__ == "__main__":
    # a = subprocess.run("dir", shell=True, check=True)
    # b = subprocess.run("main.exe", shell=True, check=True, stdout=subprocess.PIPE)
    # c = str(b.stdout, encoding='utf-8')
    # print(c)
    for i in range(20):
        print(datetime.now())
        sleep(3)
    pass