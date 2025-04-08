#!/bin/bash
appPath="c:/github"
projectName="my-book"
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
    # poetry add jupyter-book
    # poetry add requests
    # poetry add pyodbc
    # poetry add livereload
    poetry add sphinxcontrib-mermaid
}


create_book() {
    cd $projectdir
    poetry run jupyter-book create src/$projectName/book/
}

build_book() {
    cd $projectdir
    poetry run jupyter-book build src/$projectName/book
}

run_book() {
    cd $projectdir
    poetry run python live_server.py
}

function="start"
function="dependencies"
function="create_book"
function="run_book"
function="build_book"

build_book
run_book

# if [[ $function == "start" ]]
# then
    # new
   
# elif [[ $function == "dependencies" ]]
# then 
    # dependencies

# elif [[ $function == "build" ]]
# then 
    # build

# elif [[ $function == "run" ]]
# then 
    # run
# else
    # exit 99
# fi





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