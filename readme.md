# Alien Arithmetic

## FAQ

#### Python Version

Python Version : 3.9.7
pip Version : 23.3.2

#### Getting Started

Clone REPO: https://repo.csd.uwo.ca/scm/compsci2212_w2024/group55.git
cmd : "git clone https://repo.csd.uwo.ca/scm/compsci2212_w2024/group55.git"

Install Requirements (assumming you have pip since we all did 1026)

cmd : "pip install -r requirements.txt"

You're ready to start coding or to play a desktop application.

## Compile Game

To convert the source code into a working desktop application ie exe or mac equal you need pyinstaller.

cmd : cd src\
cmd : pyinstaller test_main.spec

If you have conflicts reach out and I'll help create a virtual envoirnment. You guys shouldn't have any since most of you have not done a lot of python programming so it should be fine.

## Description
Our educational game's main focus is creating an educational and entertaining experience for young children. This game's goal is to teach kids simple math (basic addition, subtraction, multiplication, division) with visually stimulating imagery and game play. Our game takes inspiration from the classic Space Invaders, where the player must destroy the obstacle corresponding to the answer of a given math equation. The player will control a ship with a math equation appearing on the screen. Asteroids will start approaching the player's ship, each with a different number on it. The player must destroy the asteroid with the correct number on it to continue, where the process repeats.

## FAQ

#### File Formats
File format for storing game data will be in a text file.
Text file will store a json string in a file.
Username
Score
Level
Correct Answers
Total Questions Answered

#### Development Environment
Visual Studio Code (VS Code) is the code editor that we will be using as it provides some essential features to allow us to seamlessly develop the program. Pydoc is the built-in documentation tool that we will use to document the code effectively. It provides valuable information on modules, classes, functions, and methods. The unittest framework will allow us to write and run tests allowing us to define organize and execute them to ensure the code is correct.
For external libraries, Pygame is a library for developing games in Python which we will be using. It provides functionalities for handling graphics, sound, input devices, and other aspects of game development, making it suitable for implementing the game. Pydantic is a library for data manipulation and validation. It provides a way to model data for the asteroid, player, and scoreboard class to be stored in a CSV file or converted into JSON based on the requirements of the project.
Additional tools we will be using are Bitbucket, Jira, and Confluence. Bitbucket for version control, Jira for project management, Confluence for collaborative documentation and diagrams, and established coding standards to maintain code consistency. The application, designed for Windows 10 systems, will be self-contained, requiring no internet connection, and will s
