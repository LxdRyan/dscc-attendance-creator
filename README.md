# DSCC Attendance Creator

## About
Creates attendance-taking messages for start and end of lessons for DSCC NTU-WLP.

## Installation
```
git clone https://github.com/LxdRyan/dscc-attendance-creator.git
pip install dscc-attendance-creator
```
Ensure you have Python (and pip) installed.

## Usage
`attendance` displays a help message which contains a list of commands.
### Create
To use, enter `attendance create` in a terminal and follow the prompts to input details.
### Config
To use, enter `attendance config` followed by the options for editing the config.

e.g. To change the default rank to _CPL_, use `attendance config --rank CPL`.

Multiple configs can be edited at the same time, e.g. `attendance config --rank CPL --batch 04/24`