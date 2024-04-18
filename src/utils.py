import subprocess

def run(command):
    output = subprocess.run(command, capture_output=True, shell=True)