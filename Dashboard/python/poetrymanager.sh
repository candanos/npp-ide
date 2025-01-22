#!/bin/bash
function="build"
function="start"
function="dependencies"
function="run"

appPath="c:/github"
projectName="premier-league-book"
projectdir=$appPath'/'$projectName

new() {
# start a new application
    cd $appPath
    poetry new --src $projectName
    cd $projectdir
    poetry config --local virtualenvs.in-project true
    poetry config --local virtualenvs.create true
    poetry config --local virtualenvs.options.always-copy true
    poetry config --local virtualenvs.options.no-pip true
    poetry config --local virtualenvs.options.no-setuptools true
    poetry config --local virtualenvs.options.system-site-packages false
    poetry config --list --local
    poetry env info
}

dependencies() {
    cd $projectdir
    poetry add jupyter-book
    poetry add requests
    poetry add pyodbc
}


run() {
    cd $projectdir
    # premier_league_book is the package name of the poetry project.
    # poetry run command provides that the command you run use poetry configuration and .venv
    # if you want to run internal commands/scripts which is inside of you poetry project,
    # such as pytest, sphinx, jupyter-book you shoud use them with poetry run. poetry run creates 
    # an internal runtime environment for your commands.
    poetry run jupyter-book create src/premier_league_book/book
}

if [[ $function == "start" ]]
then
    new
#    
elif [[ $function == "dependencies" ]]
then 
    dependencies
#
elif [[ $function == "build" ]]
then 
    build
#
elif [[ $function == "run" ]]
then 
    run
else
    exit 99
fi





# poetry install

# poetry build

# export POETRY_HTTP_BASIC_NEXUS_USERNAME=mydeploymentuser
# export POETRY_HTTP_BASIC_NEXUS_PASSWORD=https://pypi.example.org/legacy/
# export POETRY_REPOSITORIES_NEXUS=mydeploymentpassword

# poetry config repositories.nexus https://pypi.example.org/legacy/
# poetry config http-basic.nexus <username> <password>


# poetry config repositories.artifactory "https://myartifactory/artifactory/api/pypi/my-py-local"
# poetry publish -vvv --repository artifactory

read -p "Press [Enter] key to go on."