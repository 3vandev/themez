# Themez
THEMEZ is a themes manager for neofetch and can also be modified to run for other programs

<hr/>

### Plans
My plan is to allow the user to install themes directly from the internet quickly and easily and add them to their themes libary
<hr>

### Installation
Open a terminal window and type the command
`git clone https://github.com/3vandev/themez`

Once the repository is cloned cd into as follows
`cd themez`


Now make sure python3 is install on your computer if not install it with your systems package manager


`pacman -S python3` - Arch based distros

`apt install python3` debian based distro

`dnf install python3` Fedora and other redhat based distros

if you are not root make sure you run the command with sudo


Now that python is installed run the installer with:
`python installer.py` or
`python3 installer.py`

once the installer finshies restart your terminal and run `themez list` to test

<hr>

### How to use themez?
If you don't already add a themes folder to your neofetch config
`mkdir ~/.config/themes`

Once you have made this folder drag all of your neofetch configs into the folder or run `themez add <configfile>` to add it directly to your themes folder. If you don't already have any neofetch configs there are plenty of repositorys full of different ones.

Now run `themez list` to display your themez.
and `themez apply <theme>` to select one.
