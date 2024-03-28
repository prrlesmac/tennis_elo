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
