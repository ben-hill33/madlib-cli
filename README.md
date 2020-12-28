# Lab: 03 - Errors, Files, and Packaging
## Project: Madlib CLI
### Author: Ben Hill
### Overview: 
- In this lab assignment you will be creating a command line application which takes advantage of Python’s built in capabilities for reading and writing files.

### Feature Checklist
- [x] Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
- [x] Create a file called test_madlib.py in root of tests folder which will be used to test your executable command line script.
- [x] Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle), build a command line tool which will perform the following:
  - [x] Print a welcome message to the user, explaining the Madlib process and command line interactions
  - [ ] Read a template Madlib file ([Example](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/make_me_a_video_game_template.txt)), and parse that file into usable parts.
- [ ] You need to decide what components of this file are useful, and how to break those useful pieces apart
- [ ] Once you know what parts of the template need user input, such as **Adjective**, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
- [ ] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
- [ ] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
- [ ] Write the completed text ([Example](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/make_me_a_video_game_output.txt))to a new file on your file system (in the repo).
- [ ] Note: A [smaller example file](https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/dark_and_stormy_night_template.txt) is included as well which can be handy when developing/testing.

### Links and Resources:
- [Pull Request URL](https://github.com/ben-hill33/madlib-cli/compare/madlib?expand=1)
- [python-poetry](https://python-poetry.org/)
### Setup
This program uses python-poetry for dependency package manager. In order to create this project, follow the python-poetry link in the **Links and Resources** section above and install poetry.

Then enter the following commands into your CLI from the directory you want your project to live:
```
$ poetry new example-lab
$ cd example-lab
$ poetry add --dev black --allow-prereleases
$ touch example_lab/example_lab.py
$ mv README.rst README.md
$ git init
$ git add .
$ git commit -m "first commit"
```
### How to initialize/run your application
Now that your program is scaffolded you can run poetry virtual environment.
To initialize, run this command in CLI:
```$ poetry shell```
To check output:
```$ python madlib_cli.py```
### Tests
This program is tested with pytest

