#!/opt/pwn.college/python

import subprocess

with open("thisworks.txt", "w") as file:
    file.write("")

command = ["cd/challenge/sic-1.3"]
subprocess.run(command, text=True)

command = ["sudo", "make"]
subprocess.run(command, text=True)

command = ["sudo", "make", "install"]
subprocess.run(command, text=True)
