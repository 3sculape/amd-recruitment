# Amd Recruiment Exercices


## AUTHORS
 - Samuel Quesne samu3lquesne@gmail.com


## Github Action for Python Virtual Environments
### Files
 - `.github/actions/run-python-venv/action.yml`
 - `.github/scripts/run-python-venv/install-script.sh`

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
To solve this exercise, I used two parts : one action yaml configuration and one installation script.

The yaml is basic, it defines a composite action with all inputs defined above.
The only inputs set to required are the python-version and run field.
This is because they are the only mandatory field for the venv to work.
Next, the composite action is split in four parts.
 - The python installation with the setup-python action.
 - The venv setup.
 - Launching the pip install script with the venv activated.
 - Running the given command with the venv activated.

I used a shell script to install the dependencies because of the need to build a constraints file with the constraints field.
This allows the script to execute tests on the input fields and build the right pip command.


## Github Action for notifying mentioned PRs
### Files
 - `.github/workflows/update-checkbox.yml`
 - `.github/scripts/update-checkbox.py`

### Usage
This workflow execute itself when closing a pr.

### Approch to the problem
This exercise was more challenging as there was many more pitfalls.
To solve this exercise, We needed a config that launched when closing a pr, with the right permission and information, and a script to communicate with the Github API.

Since with the previous exercises we now have a ready python environment, I choose to do a python script with the PyGithub package to communicate with the API.
Then, the yaml file first define the `on` field defining that the workflow is run on closing pr, then the job to run.
The job will check out the repository and then setup a python environment running the script.
It also adds two environment variable necessary to the API communication.

The script is also straightforward.
After getting the arguments from the environment, a communication with the API is setup.
Then, it gets the timeline event information in the pr, and search for a cross-reference event.
If found, it will search for any comment with the format `[ ] PR #pr_number` and will update the comment with the checkbox ticked.

I did not manage to get the comment to update, as I was stuck on a permission problem.
The token used for authentication did not have the right to update the comment, even when setting write permission for issues and pr.
