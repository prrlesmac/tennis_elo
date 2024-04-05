Virtualenv and requirements.txt
When setting up a new project, list out the Python dependencies in a requirements.txt file, including the version numbers. Commit this file to the repository, so that every new user can replicate the environment your codebase needs to run in.

Users can create a new environment by using virtualenv:

# This creates the virtual environment
cd $PROJECT_PATH
python -m venv venv
and then install the dependencies by referring to the requirements.txt:

# This installs the modules
pip install -r requirements.txt

# This activates the virtual environment
If microsoft doesnt allow activating venv go to website https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows
execute Set-ExecutionPolicy Unrestricted -Scope Process

.\venv\Scripts\activate



Black as a pre-commit linter
Black is used as a pre-commit linter. You should follow the instructions in their repo on how to set it up. In essence you need to:

Install black using pip.
Install pre-commit using pip.
Copy the .pre-commit-config.yaml file into your repository.
Run pre-commit install.

# Running tests
pytest tennis_elo

#To install package execute: python setup.py install
or try: pip install .



# setup docker
In a CMD containing the repo run the following:
docker build -t tennis_elo .

To run the container
docker run -it --rm tennis_elo

To view inside container
docker exec -it tennis_elo sh

To clear space
docker system prune --force

to run fast api
docker run -d -p 8000:8000 tennis_elo

push the image to dockerhub
docker push tennis_elo:latest

To run process inside the container, after building image
docker run --name tennis_elo -d -p 8000:8000 tennis_elo
docker exec tennis_elo python tennis_elo/pipeline/run_elo.py



# to start the app locally
uvicorn main:app --reload
go to browser: http://localhost:8000/get?data={"key":"value"}

# installing jenkins on ec2 instbance
## 1. installing Jenkins on Linux system
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

( note you'll get an error that it failed to start jenkins, but it's OK bc java has not been installed)

# 2. intalling JAva
sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version
(note you'll also get an erro bc Jenkins isnt started)

# 3. starting jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

# 4. make sure you open the port of 8080
(Note this will open all ports which is just for test purposes. PRod should only open needed ports)
1. In EC2 instance, go to "Security" tab
2. Click on the specific Security group
3. Click on edit inbound rules
4. Click on Add Rule --> Select "All TCP" in the dropdown for Type __> Select "Anywhere Ipv4" for Source dropdown
5. Do the same but select "Anywhere IPv6" for Source dropdown
6. Click on "Save rules"

# 5. finish installation via browser
1. in EC2 instance find public IPv4 address (i.e. 44.204.43.20) and go to http://44.204.43.20:8080/
2. find admin password in file, and install suggested plugins


# install docker on ec2 instance
## Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

## Add the repository to Apt sources:
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

## to check if install works then run
sudo docker run hello-world

## add permissions to non-super users and to Jenkins to run docker
sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER
(note restart the instance for permissions to work)
