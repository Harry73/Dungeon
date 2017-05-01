# Linux Documentation

By Ian Patel (pateli3@tcnj.edu)

## Linux commands

Use Tab to auto-complete things in terminal.



### Basic commands

* ```clear``` will clear the terminal screen
* ```exit``` will quit the terminal

#### Man Pages

* ```man <command>``` opens the Linux documentation for the \<command\>  

#### sudo

* ```sudo <command>``` runs \<command\> as root. sudo gives you free reign to do just about anything, so **be careful**
* ```sudo su -``` changes you to the root terminal. Again, this will give you free reign to do anything, **so be careful**
* ```sudo su - <user>``` changes you to the \<user\>'s terminal. You can essentially log in as someone else with this

#### List Files

* ```ls``` lists files in current directory  


* ```ls -a``` lists all (including hidden) files in current directory  


* ```ls -l``` lists files in current directory with more information  

#### Change Directory

* ```cd``` changes to your home directory  


* ```cd ~``` changes to your home directory  


* ```cd /home/pateli3/DCNN/tools``` changes to the /home/pateli3/DCNN/tools directory
* ```pwd``` shows the full path to the current directory

#### Create and Delete

* ```touch test.txt``` creates a file called "test.txt"
* ```mkdir test``` creates a directory called "test"
* ```rm test.txt``` deletes a file called "test.txt"
* ```rm -r test/``` deletes a directory called "test" and everything in it
* ```rm -rf test/``` deletes a directory called "test" and everything in it without checking anything - **be careful with this**

#### Copy

* ```cp test.txt new_file.txt``` create a copy of "test.txt "called "new_file.txt"
* ```cp test/* newStuff/``` copy everything in the "test" folder to the "newStuff" folder
* ```cp -r test/ newStuff/```  create a copy of the "test" folder called "newStuff"

#### Rename or Move

Renaming a file is the same as moving it to the same location with a different name.

* ```mv test.txt newFile.txt``` renames "test.txt" to "newFile.txt"
* ```mv test newStuff``` renames the "test" folder to "newStuff"
* ```mv * ../test``` move everything in the current directory up one level and into the "test" folder
* ```mv test.txt /tmp/temp.txt```  move "test.txt" to "/tmp" and rename the file to "temp.txt"

#### Show Tasks

* ```ps``` lists programs you started in this terminal  
* ``` ps -a``` lists all your running programs  
* ```ps auxx``` lists all running programs on the computer  
* ```top``` is an alternative to ps that shows the programs with more information

#### Searching with grep

* ```grep pattern <file>``` will search a file for the pattern and print matching lines  

Often it's useful to run grep on the output of another command. This can be done by "piping" the output of a command to grep with the | character:  

* ```ps auxx | grep vnc``` runs "ps auxx", then searches and displays only the running processes whose name include "vnc"  
* ```ls -l | grep test.txt``` lists information for the "test.txt" file only







#### File Commands

* ```more test.txt``` will show the beginning of the "test.txt" file. Use enter to continuing showing more lines
* ```tail test.txt``` will show the end of the "test.txt" file. Add ```-n <num>``` to display \<num\> lines
* ```truncate -s 0 test.txt``` will clear the contents of the "test.txt" file

#### Command Line Downloads

```wget``` and ```curl``` are two utilities for downloading files from the Internet in command line, but I'm more familiar with wget.

Download the "get-pip.py" file from the Internet:

```
wget https://bootstrap.pypa.io/get-pip.py
```

Download the same file and save it as "pip.py":

```
wget -O pip.py https://bootstrap.pypa.io/get-pip.py
```

#### Miscellaneous

- ```uname -a``` displays information about the system

* ```ln test1.txt test2.txt``` creates a hard link between two files. In this case, "test2.txt" shares the same space on the disk as "test1.txt", and the two are essentially equivalent.
* ```ln -s test1.txt my_link``` creates a symbolic link. The "my_link" object will point to "test1.txt". If a command involves "my_link", "my_link" is replaced by "test1.txt"
* ```who``` lists users that are currently connected or logged in
* ```whoami``` displays the user of the current terminal
* ```df -h``` and ```du -sh``` can show the free disk space
* ```sudo reboot now``` restarts the computer immediately
* ```sudo shutdown now``` turns off the computer immediately



### Processes

If you need to stop a process, use ```CTRL+C```.

Most of the time, you'll likely start a process in the foreground, meaning it will run directly in the current terminal, so if you close the terminal the process will also end. For a process that takes a very long time to run though, you may want it to run in the background. This can be done with the & operator:

```
make &
```

The above command would be used to compile a program. Adding the & runs the program in the background, and allows you to do other work in the terminal in the meantime.

If you want to move a foreground process to the background, use:

```
CTRL+Z
bg %1
```



### SSH and SCP

SSH stands for Secure Shell. As long as a Linux computer is running, you should be able to connect to it through SSH. Doing so will give you access to a terminal. SCP stands for Secure Copy, and is a method of copying files from one computer to another through the SSH protocol.

#### Windows

I recommend using [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) for SSH. In the "Host Name (or IP address)" bar, type the address you would like to connect to and the username you will do so with. If I wanted to connect to lp-1, this would be:

```pateli3@lp-research-linux-1```

You would use your own username instead of pateli3 though. Hit "Open", and you should be prompted for a password. If there is a warning message, you can say "yes".

For SCP, I like [WinSCP](https://winscp.net/eng/download.php). To open a new connection, select "New Site", and enter the hostname (like "lp-research-linux-1") and username (like "pateli3"). Hit "Login" and enter your password when prompted. You can drag and drop files between the two computers afterwards.

Note: If you want to use the command line versions of SSH and SCP like I describe for Mac/Linux, you can install the git command line interface. This will allow you to use git commands from the command prompt, and it also comes with SSH and SCP.

#### Mac/Linux

The terminal application should be sufficient on a Mac or a Linux computer. If I wanted to connect to lp-1, I would type in a terminal:

```ssh pateli3@lp-research-linux-1```

You would use your own username instead of pateli3 though. Hit enter and you should be prompted for a password. If there is a warning message, you can say "yes".

For SCP, the terminal is also sufficient. If I want to copy a file from lp-1, I'd type:

```
scp pateli3@lp-research-linux-1:/home/pateli3/test.txt .
```

To copy from my local computer to lp-1, simply reverse the order.

```
scp ./test.txt pateli3@lp-research-linux-1:/home/pateli3/
```

A folder and its contents can be copied with the -R option:

```
scp -R pateli3@lp-research-linux-1:/home/pateli3/test/ .
```



### Terminal Editing

Files can be edited in the terminal, though a program is required. I like nano, Dr. Pearlstein likes vim.

#### Nano
I like nano most of the time because it is very simple.  

Edit a file called test.txt (creates the file if it does not exist):  

```
nano test.txt
```

Nano lists its available commands at the bottom, but in general:  

* ```CTRL+O``` saves the file. Press enter to confirm the file name.    
* ```CTRL+X``` exits the editor.  

#### Vim
Vim provides a lot of useful functions, as long as you know all the keyboard shortcuts.  

Edit a file called test.txt (creates the file if it does not exist):

```
vim test.txt  
```

By default, vim will put you in command mode. Use "i" to switch to edit mode. Use "ESCAPE" to switch back to command mode.  In edit mode, you can type and alter the file as normal.  In command mode, you can use shortcuts to perform useful operations.  

* ```:wq``` save and quit  
* ```:q!``` quit without saving  
* ```dd``` deletes a line  
* ```/<word>``` jumps to the next occurence of \<word\> in the file. Use "n" to move to the next occurence and "N" to move to the previous occurence.  

Search for more commands, if you like.  



### Shells

I prefer bash, Dr. Pearlstein prefers tcsh. To see which shell is running, use:  

```
echo $SHELL
```

#### Environment Variables

Environment variables are just variables in a shell that store some value. The command to create an environment variable depends on your shell. To create, for example, a variable named "DCNN_ROOT" with a value of "/home/pateli3/DCNN/"  

Set a variable in bash:

```
export DCNN_ROOT=/home/pateli3/DCNN
```

Set a variable in tcsh:

```
setenv DCNN_ROOT /home/pateli3/DCNN
```

To print the value of an environment variable, use ```echo```, and put a dollar sign before the variable name:

```
echo $DCNN_ROOT
```

#### Aliases

Create a shortcut keyword to perform a command. For instance, I made an alias called "update" to run update commands  

```
alias update="sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y"  
```

This way, I can simply type "update" to run the three commands.  

#### Persistent Variables and Aliases

If you want environment variables or aliases to remain even after you close the terminal, add the lines to ~/.bashrc for bash or ~/.cshrc for tcsh. These are files that run whenever a shell opens.

For example, my .bashrc file on lp-1 looks looked like:  

```
# .bashrc  

alias avconv="/home/libav/libav-11.4/avconv"  
alias matlab="/usr/local/MATLAB/R2015a/bin/matlab"  
alias proj="cd /home/pateli3/proj_vfrp_2016/master"  

# Admin update  
alias update="sudo yum update -y"  

# Quick ssh to lp-research-linux-2  
alias ssh2="ssh pateli3@lp-research-linux-2"  
alias ssh3="ssh pateli3@lp-research-linux-3"  

# proj_vfrp root environment variable  
export PROJ_VFRP_2016_ROOT="/home/pateli3/proj_vfrp_2016/master"  
export LD_LIBRARY_PATH=/home/opencv/opencv/install/lib  

# Making bash shell pretty  
PS1='\[\e[1;31m\]\u@\h \w \n\[\e[1;32m\]\@ \d\[\e[m\] > '  
ls --color=al > /dev/null 2>&1 && alias ls='ls -F --color=al' || alias ls='ls -G'  
```

My .cshrc file on lp-2 looks like:  

```
setenv DCNN_ROOT /home/pateli3/DCNN  
setenv CAFFE_ROOT /home/caffe  
setenv ELC470_SP17_ROOT ${HOME}/elc470_sp17  

set path = ( $path /usr/local/bin )  
set path = ( $path /home/caffe/build/tools )  
set path = ( $path ${ELC470_SP17_ROOT}/tools/bin )  
set path = ( $path ${ELC470_SP17_ROOT}/script )  
set path = ( $path . )  
```

If you change the .bashrc or .cshrc file and want to use the new changes, use:

```
source ~/.bashrc
	OR
source ~/.cshrc
```

#### Default Shell

To change the default shell for a user, edit the /etc/passwd file. Entries in here should look like:  

```
pateli3:x:520:520:Ian Patel:/home/pateli3:/bin/bash  
```

The last piece, "/bin/bash", is what defines the default shell for the user. Other shells, like tcsh, are also located in /bin.  



### Permissions and Owners:

```ls -l``` will show you the permissions, owners, and last date modified for a file or folder.  

For an entry like:  

```
drwxr-xr--. 4 pateli3 all  4096 Feb 18 16:51 Desktop/  
```

the permissions are "rwxr-xr--" (the "d" stands for directory), the user owner is "pateli3", the group is "all", and the last date modified is Feb 18th at 16:51.  

#### Permissions
Every file and folder has permissions on it describing who can read, write, and execute the item.

As an example, suppose ```ls -l``` reports something like "rwxr-xr--". This is really three pieces of information, "rwx", "r-x", and "r--", which correspond to user owner, group, and other, in order. In this case, the user owner can read, write, and execute the file. Anyone in the group can read and execute this file. Any other user can only read this file.  

These permissions can be controlled with the ```chmod``` command.

```
chmod <options> <permissions> <file>  
```

A common option I'll use is "-R", which, when used on a folder, will recursively go down into the folder and change the permission on every file and folder in the folder. The permissions are specified with 3 digits decimal numbers, where each digit's binary equivalent specifies the permissions allowed.  

|  Binary   | Becomes |  Binary   | Becomes |
| :-------: | :-----: | :-------: | :-----: |
| 000 (---) |    0    | 100 (r--) |    4    |
| 001 (--x) |    1    | 101 (r-x) |    5    |
| 010 (-w-) |    2    | 110 (rw-) |    6    |
| 011 (-wx) |    3    | 111 (rwx) |    7    |
Examples:  

* ```chmod 777 test.txt``` allows anyone to read, write, and execute test.txt  
* ```chmod -R 755 test/``` gives user read/write/execute permission, while others have read/execute permissions on the test/ directory and everything in it  
* ```chmod 740 test.txt``` gives user read/write/execute permission, group has read permission, others have no permission on test.txt  

#### Owners:
```ls -l``` also showed the user owner and group owner of a file and folder. Going back to:  

```
drwxr-xr-x. 4 pateli3 all  4096 Feb 18 16:51 Desktop/  
```

The user owner is pateli3 and the group is all. The user owner gets the first set of permissions (rwx), and the group gets the second set of permissions (r-x).

To change the owners, use the ```chown``` command:  

```
chown <options> <user owner>:<group> <file>  
```

Again, I'd use the "-R" option to recursively go into a folder and change the owner and group of all files within.  

Examples:  

* ```chown pateli3:research test.txt``` makes the user "pateli3" and the group "research" for the test.txt file  
* ```chown pateli3 test.txt``` makes the user "pateli3" and leaves the group untouched for the test.txt file  
* ```chown -R pateli3:research test/``` makes the user "pateli3" and teh group "research" for the test/ folder and everything in it  

Often it will be necessary to use ```sudo``` before the chown command, since you may be attempting to change something that you don't have permission to control as a regular user.



### Users and Groups

#### RedHat

To manage users and groups on RedHat, in VNC, run:

```
/usr/bin/system-config-users
```

Enter the root password. It should bring up window in which you can easily manage users. When adding a new user, fill out the first 5 lines. We usually pick /bin/tcsh for the login shell.

#### Ubuntu

Ubuntu also has "Users and Groups" application that comes from installing gnome-system-tools. On lp-2, you can simply search for "Users" and it should show up. On lp-3, the application is under Applications -> System Tools -> Administration -> Users and Groups.

#### Command Line User Control

If you prefer working through terminal, here's some help.

Add a user:

```
sudo adduser <username>  
```

Delete a user:

```
sudo deluser <username>  
```

Create a new group:  

```
sudo groupadd <group_name>  
```

Put a user in a group:  

```
sudo usermod –aG <group_name> <username>  
```

Give a user sudo permission:  

```
sudo usermod –aG sudo <username>  
```



### Updates and Packages

Updating a Linux computer is dependent on the flavor of Linux. Basically every variant of Linux has its own package manager. Ubuntu use "apt" and RedHat uses "yum". The package manager is used to get updates for the computer and to install or remove new software from the the standard distributions.

#### Getting Latest Updates

##### Ubuntu

```
sudo apt-get update -y  
sudo apt-get upgrade -y  
sudo apt-get dist-upgrade -y  
```
##### RedHat

```
sudo yum update -y
```

#### Installing a new package

##### Ubuntu

```
sudo apt-get install <package name>
```

If you have a downloaded Ubuntu package, it will likely be a .deb file. These can be installed with dpkg and apt-get:

```
sudo dpkg -i <file>.deb
sudo apt-get install -f
```

##### RedHat

```
sudo yum install <package name>
```

If you have a downloaded RedHat package, it will likely be a .rpm file. These can be installed using rpm, but it's usually safer with yum as yum will attempt to handle dependencies:

```
sudo rpm install <file>.rpm
	OR
sudo yum install <file>.rpm
```

#### Removing a Package

Ubuntu: ```sudo apt-get remove <package>```

RedHat: ```sudo yum remove <package>```



### Define a Default Home Directory Structure

The default home directory pattern is found in ```/etc/skel```. It should currently contain the usual folders, such as  

```
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```





## git

Password for user "git": duckduckgit

I'm used to using the command line version of git, but there are several applications for Windows and Mac to make it easier. On Linux though, the command line is still the standard method, so I will describe the most important commands here.

### Standard git Commands

Do NOT copy a remote repository by hand. Clone a repo instead, to create a local copy of a repository. Two examples, one for a github repo, and one for a repo on lp-1.
```
git clone https://github.com/pateli3/Sudoku.git
git clone git@lp-research-linux-1:/home/swapnil/DCNN
```

Show current state of files in the local repo:

```
git status
```

Add files that have been changed:  

```
git add <file>
```

Commit files with a message (commit message is required):  

```
git commit -m "This is my commit message"
```

Push the changes to the remote repository:  

```
git push
```

For a repo cloned from lp-1, this command may be necessary to push changes:  

```
git push origin master
```

To undo a "git add" command, use "reset":

```
git reset HEAD <file>
```

To discard changes that you've made to a file, checkout the file:

```
git checkout <file>
```



### Create a New git Repo with Remote on lp-1

For my example, I have /home/opencv on lp-2. I want to make a remote repository on lp-1, and push the contents of /home/opencv on lp-2 to the remote repository. So the local copy is /home/opencv on lp-2, and the remote will be in /home/swapnil on lp-2. This is the process I followed

As the "git" user, in /home/swapnil/ on lp-1:

```
mkdir ubuntu_opencv.git
cd ubuntu_opencv.git
git init --bare
```

On lp-research-linux-2, in /home/opencv (because I wanted to include opencv and opencv_contrib):  

```
git init  
git add "*.c"  
git add **.cpp"  
git add "*.h"  
git add "*.hpp"  
git add "*Makefile*"  
git add "*make*"  
git add "*mk*"  
git add "*Mk*"  
git commit -m "First time check in of our local opencv build"  
git remote add origin ssh://git@lp-research-linux-1/home/swapnil/ubuntu_opencv.git  
git push origin master  

git add opencv-3.2.0/modules/*  
git add opencv_contrib-3.2.0/modules/*  
git comit -m "Added everything under modules"  
git push origin master  
```

What you ```git add``` to the repo is up to you. I included all .c, .cpp, .h, .hpp, and Makefiles from opencv. Most likely code files are a must.  





## Installing opencv from Source

Check the opencv github page for the latest version of opencv. Installation instructions should also be available on the page, but this generally worked for me.  
```
mkdir /home/opencv  
cd /home/opencv  
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.2.0.zip  
wget -O opencv.zip https://github.com/Itseez/opencv_contrib/archive/3.2.0.zip  
unzip opencv.zip  
unzip opencv_contrib.zip  
cd opencv-3.2.0/  
mkdir build  
cd build  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES=/home/opencv/opencv_contrib-3.2.0/modules ..  
make -j16  
sudo make install -j16  
sudo ldconfig  
```





## VNC:
Note: I only had experience performing the first-time set up for VNC on Ubuntu.

### Ubuntu VNC First-Time Setup

#### Install some Prerequisites:  

```
sudo apt-get install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal  
sudo apt-get install vnc4server  
```

#### Install TigerVNC
I've tried several different VNC packages on Ubuntu, but TigerVNC is the only one I could get to work correctly. TigerVNC also appears to have changed a bit with the 1.8.0 release, so installation may be different now. I installed 1.7.0 for lp-2 and 1.7.1 for lp-3 as described below though.  

Get the binary from [Tigervnc’s github page](https://github.com/TigerVNC/tigervnc/releases). Look under Files for the download that suits your system,
and copy the link to use with "wget".  
```
wget -O tigervnc.deb https://bintray.com/tigervnc/stable/download_file?file_path=ubuntu-16.04LTS%2Famd64%2Ftigervncserver_1.7.1-1ubuntu1_amd64.deb
sudo dpkg –i tigervnc.deb
sudo apt-get –f install
```

#### xstartup File
Change your own ~/.vnc/xstartup file to:  
```
#!/bin/sh

export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &

gnome-session &
gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &
```
All current users should also get the same xstartup file under /home/\<user\>/.vnc

Edit (with sudo) the /usr/bin/vnc4server file, and change the $defaultXStartup section to:
```
$defaultXStartup
    = ("#!/bin/sh\n\n".
        "export XKL_XMODMAP_DISABLE=1\n".
        "unset SESSION_MANAGER\n".
        "unset DBUS_SESSION_BUS_ADDRESS\n\n".
        "[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup\n".
        "[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources\n".
        "xsetroot -solid grey\n".
        "vncconfig -iconic &\n\n".
        "gnome-session &\n".
		"gnome-panel &\n".
        "gnome-settings-daemon &\n".
        "metacity &\n".
        "nautilus &\n".
        "gnome-terminal &\n");
```
When you create a new user now, they should get the appropriate xstartup file automatically.

#### Automatic VNC Start on System Startup
Go to /etc/init.d/. Move the current "vncserver" file to a backup file.

```
sudo mv vncserver vncserver_old  
```

Create a new file (with sudo) called "vncserver", and put something like this, where each user gets a line under start and top:  

```
#!/bin/sh -e
### BEGIN INIT INFO
# Provides:        vncserver
# Required-Start:  networking
# Required-Stop:   networking
# Default-Start:   2 3 4 5
# Default-Stop:    0 6
### END INIT INFO

PATH="$PATH:/usr/X11R6/bin"

case "$1" in
start)
su pearlstl -c   "/usr/bin/vncserver :5  -geometry 1800x1000 -depth 24"
su mensch -c     "/usr/bin/vncserver :6  -geometry 1800x1000 -depth 24"
su pearlstl -c   "/usr/bin/vncserver :7  -geometry 1800x1000 -depth 24"
su mun -c        "/usr/bin/vncserver :8  -geometry 1800x1000 -depth 24"
su pateli3 -c    "/usr/bin/vncserver :19 -geometry 1800x1000 -depth 24"
su shanleo1 -c   "/usr/bin/vncserver :20 -geometry 1800x1000 -depth 24"
su sieberb1 -c   "/usr/bin/vncserver :21 -geometry 1800x1000 -depth 24"
su rezkalr1 -c   "/usr/bin/vncserver :22 -geometry 1800x1000 -depth 24"
su setow1 -c     "/usr/bin/vncserver :23 -geometry 1800x1000 -depth 24"
su mike_iup -c   "/usr/bin/vncserver :24 -geometry 1800x1000 -depth 24"
su maxwels2 -c   "/usr/bin/vncserver :26 -geometry 1800x1000 -depth 24"
;;

stop)
su pearlstl -c   "/usr/bin/vncserver -kill :5"
su mensch -c     "/usr/bin/vncserver -kill :6"
su pearlstl -c   "/usr/bin/vncserver -kill :7"
su mun -c        "/usr/bin/vncserver -kill :8"
su pateli3 -c    "/usr/bin/vncserver -kill :19"
su shanleo1 -c   "/usr/bin/vncserver -kill :20"
su sieberb1 -c   "/usr/bin/vncserver -kill :21"
su rezkalr1 -c   "/usr/bin/vncserver -kill :22"
su setow1 -c     "/usr/bin/vncserver -kill :23"
su mike_iup -c   "/usr/bin/vncserver -kill :24"
su maxwels2 -c   "/usr/bin/vncserver -kill :26"
;;

restart)
$0 stop
$0 start
;;
esac

exit 0
```

Make the file executable:  

```
sudo chmod +x vncserver
```

Register the file as a startup service:  

```
sudo update-rc.d vncserver defaults
sudo update-rc.d vncserver enable
```
Give each user a vnc password (I usually default to their username).

```
sudo su <username> -c “vncpasswd”
```

Type their password as prompted. You can answer no to the view-only password question. You MUST do this for each user in the vncserver script you just created before trying to run the script. It will fail otherwise. Once you've done that, start the VNC servers with:  

```
sudo service vncserver start
	OR
sudo /etc/init.d/vncserver start  
```



### Give a New User a VNC Server

#### Ubuntu

Assuming the /etc/init.d/vncserver file already exists and vncservers are set up correctly, edit (with sudo) the /etc/init.d/vncserver file and add two new lines for the user, following the usual pattern:

```
su <user> -c   "/usr/bin/vncserver :<vnc number> -geometry 1800x1000 -depth 24"
	AND
su <user> -c   "/usr/bin/vncserver -kill :<vnc number>"
```

Run vncpasswd as the user:

```
sudo su <username> -c "vncpasswd"
```

Set a default password and tell them what it is. The user can change their own VNC password later with ```vncpasswd```. Start their VNC server with the service or by hand:  

```
sudo service vncserver start
	OR
sudo su <user> -c "/usr/bin/vncserver :<vnc number> -geometry 1800x1000 -depth 24"
```

#### RedHat

Note: Setup on a new RedHat computer may make these instructions invalid. For lp-1 though, this can be used to give a new user a VNC server.

Run vncpasswd as the user:

```
sudo su <username> -c "vncpasswd"
```

Set a default password and tell them what it is.

Edit (as root) the /etc/sysconfig/vncservers file. There should be one long line of VNC servers to start. Pick a new VNC number for the new user, and add them to this list, following the pattern. Also add a line at the bottom of the file like:

```
VNCSERVERARGS[<vnc number>]="-extension RANDR -geometry 1800x1000 -depth 24"
```

Now edit (as root) the /etc/sysconfig /iptables file. Add three lines near the end of the file and continue the pattern:

```
-A INPUT -p tcp -m state --state NEW -m tcp --dport 58<vnc number> -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 59<vnc number> -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 60<vnc number> -j ACCEPT
```

Restart the iptables service:

```
sudo /sbin/service iptables restart
```

Then start the user's vncserver:

```
sudo su <user> -c “vncserver :<number> -extension RANDR –geometry 1800x1000 –depth 24
```

In the future, the /etc/sysconfig/vncservers file will take care of starting the vncserver on reboot.



### Restarting a VNC Server

Due to how this is set up, every user should have control over his or her own VNC server. If a user's VNC server freezes or is messed up, they should be able to restart it with:

```
vncserver -kill :<number>
vncserver :<number> -geometry 1800x1000 -depth 24
```





## Samba

### Installation

Ubuntu: ```sudo apt-get install samba```

RedHat: ```sudo yum install samba```



### Register a User for Samba

```
sudo smbpasswd –a <username>
```

Give them some default password. The user can change their own password later with ```smbpasswd```.



### Samba Shares

The file /etc/samba/smb.conf has the configuration for which directories to share through samba. After you alter this file, restart the samba service with:

Ubuntu: ```sudo service smbd restart```

RedHat: ```sudo service smb restart```

I’ve found that the easiest way to control access to samba shares is to share the folder for a Linux group. Then anyone in the group can access the contents of the folder. Example for sharing a home directory so that multiple people can view it:

```
[mun]
comment = Mun's Home
path = /home/mun
read only = no
writeable = yes
browseable = yes
valid users = +research
create mask = 0770
directory mask = 0770
force user = mun
```

#### Breakdown

* ```[mun]```  this samba share will be named "mun"
* ```path=/home/mun```  shares the directory /home/mun
* ```read only = no```
  ```writeable = yes ``` these three all say that the share can be read from and written to
  ```browseable = yes```
* ```valid users = +research```  indicates that anyone in the "research" group can access share. The + is necessary, and is followed by the group name
* ```create mask = 0770```  means that new files created in this share will take the 770 permission by default
* ```directory mask = 0770``` means that new directories created in this share will take the 770 permission by default
* ```force user = mun```  means that when new files or directories are created in this share, the user own will be "mun" by default

#### Notes

If you intend for another computer to automatically mount this share on startup, you (or an admin) will also need to be in the group.

If you want to share something with everyone, use the "all" group. The "all" group contains all the standard users for the machine, so everyone will be able to use the shared folder.



### Automatic samba mountings
#### Setup

I will use lp-3 as my example. Install prerequisites for mounting samba shares:

```
sudo apt-get install cifs-utils nfs-common
```

Make directories /home/lp-research-linux-1 and /home/lp-research-linux-2. In these two, make a folder for each samba share you want to mount.

#### Automatic Mountings

/etc/fstab contains a listing of mount commands that a Linux computer should perform on startup. To add commands for samba mounting, edit (with sudo) /etc/fstab, one line for each mounting. On lp-3, the file looks like this:

```
//lp-research-linux-1/scratch1 /home/lp-research-linux-1/scratch1 cifs uid=pateli3,gid=all,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm       0 0
//lp-research-linux-1/pearlstl /home/lp-research-linux-1/pearlstl cifs uid=pearlstl,gid=all,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm      0 0

//lp-research-linux-1/media    /home/lp-research-linux-1/media    cifs uid=pateli3,gid=all,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm       0 0

//lp-research-linux-1/mun      /home/lp-research-linux-1/mun      cifs uid=mun,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm      0 0

//lp-research-linux-1/maxwels2 /home/lp-research-linux-1/maxwels2 cifs uid=maxwels2,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0

//lp-research-linux-1/setow1   /home/lp-research-linux-1/setow1   cifs uid=setow1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm   0 0

//lp-research-linux-1/shanleo1 /home/lp-research-linux-1/shanleo1 cifs uid=shanleo1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0

//lp-research-linux-1/sieberb1 /home/lp-research-linux-1/sieberb1 cifs uid=sieberb1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0

//lp-research-linux-2/pearlstl /home/lp-research-linux-2/pearlstl cifs uid=pearlstl,gid=all,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm      0 0

//lp-research-linux-2/mun      /home/lp-research-linux-2/mun      cifs uid=mun,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm      0 0

//lp-research-linux-2/maxwels2 /home/lp-research-linux-2/maxwels2 cifs uid=maxwels2,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0

//lp-research-linux-2/setow1   /home/lp-research-linux-2/setow1   cifs uid=setow1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm   0 0

//lp-research-linux-2/shanleo1 /home/lp-research-linux-2/shanleo1 cifs uid=shanleo1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0

//lp-research-linux-2/sieberb1 /home/lp-research-linux-2/sieberb1 cifs uid=sieberb1,gid=research,credentials=/home/pateli3/.smbcredentials,iocharset=utf8,sec=ntlm 0 0
```

For each of these lines, the pattern is:

```
<samba share> <local location to mount> cifs uid=<user owner>,gid=<group>,credentials=<path to samba credentials>,iocharset=utf8,sec=ntlm 0 0
```

The \<user owner\> and \<group> define the permissions that will be on the mounted share.

To mount these shares automatically, Linux requires a samba username and password, which I've stored in my /home/pateli3/.smbcredentials file. The permissions on this file should be read only, so use

```
chmod 400 ~/.smbcredentials
```

The credential file in general should look like this:

```
username=<my username>
password=<my password>
```

#### Mounting

After adding to the /etc/fstab, you can do the following to perform the mount commands you just defined:

```
sudo mount –a
```

Linux may complain if you try to mount several samba shares all at once. Just wait a bit and then repeat the command, and the rest of the shares should get mounted. By putting these in /etc/fstab, these should also get automatically mounted on reboot too.

Once a share is mounted, you may need to chmod the folder so that it has the right permissions. Generally, you need:

```
sudo chmod 770 <share folder>
```

If you altered a line for an already mounted samba share, unmount and remount the share to see the changes take effect:

```
sudo umount <path to mounted samba share>
sudo mount -a
```





## Installing caffe2 on Ubuntu

I followed: [http://caffe2.ai/docs/getting-started.html?platform=ubuntu&configuration=compile](http://caffe2.ai/docs/getting-started.html?platform=ubuntu&configuration=compile)

### Install Dependencies

```
sudo apt-get update
sudo apt-get install -y--no-install-recommends build-essential cmake git libgoogle-glog-dev libprotobuf-dev protobuf-compiler python-dev python-pip
sudo pip install numpy protobuf
```



### Install CUDA

I followed: http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions)

- Check for CUDA-capable GPU: ```lspci |grep –i nvidia```
- Check that the results are listed here: [https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)
- Check for x86_64 system: ```uname -m && cat /etc/*release```
- Check that gcc is installed: ```gcc--version```
- Make sure kernels are updated: ```sudo apt-get install linux-headers-$(uname -r)```
- Download the deb from: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
- It’ll give you instructions to install it. Follow them.



### Install cuDNN

```
CUDNN_URL="http://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-8.0-linux-x64-v5.1.tgz"
wget ${CUDNN_URL}
sudo tar -xzf cudnn-8.0-linux-x64-v5.1.tgz -C /usr/local
rm cudnn-8.0-linux-x64-v5.1.tgz && sudo ldconfig
```



### Install Optional Dependencies

```
sudo apt-get install -y --no-install-recommends libgflags-dev
sudo apt-get install -y --no-install-recommends libgtest-dev libiomp-dev libleveldb-dev liblmdb-dev libopencv-dev libopenmpi-dev libsnappy-dev openmpi-bin openmpi-doc python-pydot
sudo pip install flask graphviz hypothesis jupyter matplotlib pydot python-nvd3 pyyaml requests scikit-image scipy setuptools tornado
```



### Clone and Build caffe2:

```
git clone --recursive https://github.com/caffe2/caffe2.git
cd caffe2
make –j20
cd build
sudo make install –j20
python -c 'from caffe2.python import core' 2> /dev/null && echo "Success" || echo "Failure"
python -m caffe2.python.operator_test.relu_op_test
```

The second to last command should print “Success” if everything went right.
The last command should indicate whether or not GPU support was enabled correctly.
