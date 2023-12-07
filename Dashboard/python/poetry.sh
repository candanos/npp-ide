appPath="c:/Cloud/github/main-repo/lab/python"
cd $appPath
projectName="poetry-demo"
repodir=$appPath'/'$projectName


poetry new $projectName # this Created package poetry_demo in poetry-demo

cd $repodir
# poetry env info
# poetry config virtualenvs.in-project true 
poetry env list --full-path
poetry config --local virtualenvs.in-project true 
poetry config --list --local
# poetry add pendulum
# poetry install
# poetry build
# poetry config --list

# export POETRY_HTTP_BASIC_NEXUS_USERNAME=mydeploymentuser
# export POETRY_HTTP_BASIC_NEXUS_PASSWORD=https://pypi.example.org/legacy/
# export POETRY_REPOSITORIES_NEXUS=mydeploymentpassword

# poetry config repositories.nexus https://pypi.example.org/legacy/
# poetry config http-basic.nexus <username> <password>


# poetry config repositories.artifactory "https://myartifactory/artifactory/api/pypi/my-py-local"
# poetry publish -vvv --repository artifactory

read -p "Press [Enter] key to go on."