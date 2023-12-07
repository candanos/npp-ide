#!/bin/bash
# generate project folder using cookiecutter
appPath="c:/Cloud/github/main-repo/lab/Python"
cd $appPath
packname="zosapi"
# create template cookiecutter directories.
cookiecutter "cookiecutter-pypackage" --no-input
# cookiecutter file://server/folder/project.git
# cookiecutter "https://github.com/audreyr/cookiecutter-pypackage.git"
# cookiecutter /path/to/template.zip

#start venv 
repodir=$appPath'/'$packname
cd $repodir
pwd
# rm -r $repodir
virtualenv venv
. "venv/Scripts/activate"

# cd $appPath
# virtualenv venv 
# rm -r $repodir
read -p "Press [Enter] key to go on."