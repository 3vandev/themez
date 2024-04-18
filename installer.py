import getpass
import subprocess

username = getpass.getuser()

def run(command):
    output = subprocess.run(command, capture_output=True, shell=True)
    print(output)

alias = input("What alias would you like to use for the command?\nMake sure the alias is not in conflict with another command ❯ ")

run(f"mv ./src/ '/home/{username}/.themez")

run(f"echo 'alias {alias}='python /home/{username}/.themez/themes.py''")


