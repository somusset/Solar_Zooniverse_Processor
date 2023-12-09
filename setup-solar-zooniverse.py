import os
import subprocess
from pathlib import Path
import shutil
import sys

"""
Make sure this script is run OUTSIDE of the Solar_Zooniverse_Processor directory.
"""

def execute_command(command, working_dir):
    """
    Execute a command in the specified working directory.
    Returns True if the command succeeds, False otherwise.
    """
    print(f"Executing in dir: {working_dir}\nCommand: {command}")
    process = subprocess.Popen(command, cwd=working_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output and error
    print(out.decode('utf-8'))
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(err.decode('utf-8'))
        return False

    return True

def setup_zooniverse(timeframe):
    """
    Sets up the directory structure as well as the dependencies needed for solar zooniverse processing.
    Then executes the make_movie.py script for the timeframe argument.
    """
    base_dir = Path(os.getcwd()).expanduser()
    timeframe_dir = base_dir / f"{timeframe}"
    venv_dir = timeframe_dir / "myenv"
    repo_dir = base_dir / "Solar_Zooniverse_Processor"
    examples_dir = repo_dir / "examples"

    # Create and change to month directory
    execute_command(f"mkdir -p {timeframe}", working_dir=base_dir)

    # Create virtual environment
    execute_command(f"python3 -m venv {venv_dir}", working_dir=timeframe_dir)

    # Clone repository
    execute_command(f"git clone {repo_dir}", working_dir=timeframe_dir)

    # Install setup.py
    execute_command(f"{venv_dir / 'bin' / 'python'} setup.py install", working_dir=repo_dir)

    # Install additional packages
    packages = "git+https://github.com/zooniverse/aggregation-for-caesar.git peewee requests tqdm sunpy"
    execute_command(f"{venv_dir / 'bin' / 'pip'} install {packages}", working_dir=repo_dir)

    """
    The below code can be uncommented if you want the script to run the make_movie.py script for you as well as move the generated files and delete the unneeded repo and venv.
    Running the script manually allows you to keep track of the progress that is output to the terminal, which can be helpful for troubleshooting. 
    I wasn't able to get the progress to output to the terminal within this script unfortunately. 
    """
    # Execute the make_movie.py script
    # execute_command(f"{venv_dir / 'bin' / 'python'} make_movie.py -oi {timeframe}", working_dir=examples_dir)

    # Move mp4s to top of the timeframe dir delete unneeded dirs
    # execute_command(f"mv {examples_dir / 'files'} {timeframe_dir}", working_dir=base_dir)
    # execute_command(f"rm -rf {venv_dir}", working_dir=timeframe_dir)
    # execute_command(f"rm -rf {timeframe_dir / 'Solar_Zooniverse_Processor'}", working_dir=timeframe_dir)

if __name__ == "__main__":
    # Checks for inclusion of timeframe as an argument
    if len(sys.argv) >= 2:
        timeframe = sys.argv[1]
        setup_zooniverse(timeframe)
    else:
        print("No timeframe provided. Please provide the timeframe that you'd like to process mp4s for as an argument.\nUse the format 'yyyy-mm-dd' and know that you can specify solely yyyy or yyyy-mm.")

