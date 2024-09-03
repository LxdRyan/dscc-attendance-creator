# DSCC Attendance Creator

## About
Creates attendance-taking messages for start and end of lessons for DSCC NTU-WLP.

## Installation
```
git clone https://github.com/LxdRyan/dscc-attendance-creator.git
pip install -e dscc-attendance-creator
```
Ensure you have Python (and pip) installed.
> Note: `-e` is the `--editable` flag, which allows pip to install the package using the files in the folder itself, instead of installing a normal package. This is a temporary workaround to fix the fact that the `config` folder does not install together with the package (for some reason I have yet to figure out), and that the current way of creating the `output` folder does not work with a normal package.

## Usage
`attendance` displays a help message which contains a list of commands.
### Create
To use, enter `attendance create` in a terminal and follow the prompts to input details.
### Config
To use, enter `attendance config` followed by the options for editing the config.

e.g. To change the default rank to _CPL_, use `attendance config --rank CPL`.

Multiple configs can be edited at the same time, e.g. `attendance config --rank CPL --batch 04/24`.
