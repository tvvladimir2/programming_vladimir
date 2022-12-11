# pythonLython
guguzela

# compile-python
This is a repo for compiling and installing python from scratch

Check installed Python version:
`python`

Command is used to download package information from all configured sources.
`sudo apt-get update`

## Compile python and Create a VirtualEnv with it
Install libraries:
`sudo apt-get install build-essential gdb lcov libbz2-dev libffi-dev libgdbm-dev liblzma-dev libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev`

Do not type it, only for safe keeping. How to stop script from running?
`Ctrl+Z`

Open new terminal and run htop service to monitore the cores and memory:
VSC virtual terminal panel >> new terminal >> bash >> `htop`

Download latest version of python:
Go to this page > find latest version >> copy link from `Gzipped source tarball` >>
https://www.python.org/downloads/release/python-3110/
Download locally using this link:
`wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz`

Uncompress this file using file name:
`tar zxvf Python-3.11.0.tgz`

Delete python tar file, we don't need it anymore:
`rm Python-3.11.0.tgz`

See available folders:
`ls`

Change to directory we extracted files to:
`cd Python-3.11.0`

Configure the optimizations for it:
`./configure --enable-optimizations`

Fully saturate all X cores, we have 4 now:
`make -j 4`

Put python exacutable inside a location where we can use it and install the setup tools
`sudo make altinstall`

Test out python:
`python`
`exit()`

If previous python is still there:
Exit from Python-3.11.0 directory
`cd ..`
`/usr/local/bin/python3.11`
`exit()`

Make python a default in our bashrc, we modify the file:
`
vim ~/.bashrc`
Add line at the end of the file:
`#new python
alias python="/usr/local/bin/python3.11"
#source venv virtual environment
source ~/.venv/bin/activate
`
To exit the file:
Esc >> Shift + Z + Z

Source this (does not work):
`source ~/.bashrc`

Check the source for python:
`which python`
> /home/codespace/.python/current/bin/python
`python`
> Python 3.11.0
`exit()`

# SETUP A TEMPLATE FOR PYTHON PROJECT
Create files:
`touch requirements.txt`
`touch Makefile`

Makefile contents:
`
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test
`

VSC will ask to install Makefile Tools extension >> install

Install pip:
`make install`

Install extension:
Name: GitHub Copilot
Id: GitHub.copilot
Description: Your AI pair programmer, helps to tell you what code to write
Version: 1.61.7372
Publisher: GitHub
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot

requirements.txt contents:
`
ludwig

VSC terminal panel >> open new terminal >> `git status`

Add file to git:
`git add README.md`

Remove extracted folder for python installation:
`rm -rf Python-3.11.0`

`vim .gitignore`

Add file to git
`git add .gitignore`
`git add *`

`git commit -m "adding skeleton"`

`git push`














