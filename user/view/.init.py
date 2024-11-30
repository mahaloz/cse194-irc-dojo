#!/opt/pwn.college/python

import subprocess

command = ["../../miniirdc"]

process = subprocess.Popen(
    command,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input="--help")

print("STDOUT:", stdout)
print("STDERR:", stderr)

