#!/opt/pwn.college/python

import subprocess

command = ["../../miniirdc-master/miniirdc"]

with open("inputOutput.txt", "w") as file:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=file,
        stderr=file,  # Combine stderr with stdout in the same file
        text=True
    )
    process.communicate(input="--help")

