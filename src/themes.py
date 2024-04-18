if __name__ != "__main__":
    exit()

from utils import run
import os
import getpass
import sys

username = getpass.getuser()

neofetch = f'/home/{username}/.config/neofetch/'
themes = f'/home/{username}/.config/neofetch/themes'

def show():
    # List all files in the themes directory and filter only those with the ".conf" extension
    files = [file for file in os.listdir(themes) if file.endswith('.conf')]

    for file in files:
        print('❯ ' + file.replace('.conf', ''))

def apply(theme):
    try:
        run(f'cp "{themes}/{theme}.conf" "{neofetch}/config.conf"')
        print(f"Sucessfully applied theme: {theme}, run 'neofetch' to try it out!")
    except:
        print(f"Error while applying theme: {theme}.conf")

def add(theme):
    try:
        run(f'cp "{theme}" "{themes}/{theme}"')
        print(f"Sucessfully added theme: {theme}")
    except:
        print(f"Error while adding theme: {theme}")

def remove(theme):
    try:
        run(f'rm -rf "{themes}/{theme}"')
        print(f"Sucessfully removed theme: {theme}")
    except:
        print(f"Error while removing theme: {theme}")

def update():
    run('git clone https://github.com/3vandev/themez ~')
    run('cd ~/themez')
    run('python installer.py')


def help():
    print("show ❯ displays all themes")
    print("apply <theme> ❯ applys given theme")
    print("add <theme-path> ❯ installs a new theme config from the path provided")
    print("remove <theme> ❯ removes a theme from your libary")
    print("update ❯ updates the program")

if len(sys.argv) > 1:
    function_name = sys.argv[1]

    # Check if the function exists
    if function_name in locals() and callable(locals()[function_name]):
        func = locals()[function_name]
        
        # Check if additional arguments are provided
        if len(sys.argv) > 2:
            # Call the function with additional arguments
            func(*sys.argv[2:])
        else:
            # Call the function without additional arguments
            func()
    else:
        print(f"Function '{function_name}' does not exist.")
else:
    print("No function name provided.")