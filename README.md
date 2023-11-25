# Amd Recruiment Exercices

## AUTHORS
 - Samuel Quesne samu3lquesne@gmail.com

## Github Action for Python Virtual Environments
### Files
 - .github/actions/run-python-venv/action.yml
 - .github/scripts/run-python-venv/install-script.sh

### Usage
```yaml
python:
  uses: .github/actions/run-python-venv/action.yml
  with:
    python-version: 'x.x'
    run: python -c 'print("Hello World!")'
```
Input:
 - `python-version`: Python version for venv
 - `requirements-file`: Path to pip requirements file
 - `constraints-file`: Path to pip constraints file
 - `requirements`: Package version to be installed in the venv
 - `constraints`: constraints on individual package versions
 - `run`: Shell commands to run with activated python venv

### Approach to the problem

To solve this exercices, I used two parts : one action yaml configuration and one installation script.

The yaml is basic, it defines a composite action with all inputs defined above.
The only inputs set to required are the python-version and run field.
This is because they are the only mandatory field for the venv to work.
Next, the composite action is split in four parts.
 - the python installation with the setup-python action.
 - the venv setup.
 - Launching the pip install script with the venv activated.
 - Running the given command with the venv activated.

I used a shell script to install the dependecies because of the need to build a constraints file with the constraits field.
This allow the script to execute test on the input field and build the right pip command.

## Github Action for notifying mentioned PRs

