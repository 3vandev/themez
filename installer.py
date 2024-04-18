import getpass
import subprocess

username = getpass.getuser()

def run(command):
    output = subprocess.run(command, capture_output=True)
    print(output)

run(["cp", "-r", "./src/", f"/home/{username}/.themez"])

subprocess.run(f"echo 'alias themez=\"python3 ~/.themez/themes.py\"' >> ~/.bashrc", shell=True)


