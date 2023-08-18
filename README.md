
# 0x00. AirBnB Clone - The Console

![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)

![Author](https://img.shields.io/badge/Author-Jealous%20Matsikachando-blue.svg)


Welcome to the **AirBnB Clone - The Console** project! This project is  a command-line interface (CLI) application that simulates the core functionalities of an Airbnb clone. Through this console, users can manage properties, users, bookings, and more, all from the comfort of their machine.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Commands](#supported-commands)
- [Execution](#Execution)
- [Requirements](#Requirements)

## Introduction

The **AirBnB Clone - The Console** is a project aimed at building a basic command-line interface for interacting with an Airbnb clone system. This console allows users to perform various actions related to property management, user profiles, bookings, and more.

## Features

- Create, read, update, and delete properties, users, reviews, and bookings.
- Interactive command-line interface for easy user interaction.
- Efficient data storage and manipulation using object-oriented programming.
- Support for basic data persistence using file I/O.
- Validation and error handling to ensure smooth user experience.
- Modular code structure for maintainability and extensibility.

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/azukauteh/AirBnB_clone.git
   ```

2. Navigate to the project directory:

   ```
   cd airbnb
   ```

3. Run the console application:

   ```
   python console.py
   ```

## Usage

Once you have the console running, you can interact with it by entering commands. The console will guide you through various operations, such as creating objects, viewing information, updating attributes, and more.

For a list of supported commands and their usage, refer to the [Supported Commands](#supported-commands) section below.

## Supported Commands

- `create <class>`: Create a new object of the specified class.
- `show <class> <id>`: Display information about a specific object.
- `update <class> <id> <attribute> <value>`: Update the attributes of a specific object.
- `destroy <class> <id>`: Delete a specific object.
- `all <class>`: Display a list of all objects of a specific class.
- `quit` or `EOF`: Exit the console.

Refer to the in-console help feature for more information about each command's syntax and usage.

## Execution

Shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: 

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

## Requirements

#Python Scripts

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

Your code should use the pycodestyle (version 2.8.*)

All your files must be executable

The length of your files will be tested using wc

All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__
import__("my_module").MyClass.my_function.__doc__)')

#Python Unit Tests

All your files should end with a new line

All your test files should be inside a folder tests

You have to use the unittest module

All your test files should be python files (extension: .py)

All your test files and folders should start by test_

Your file organization in the tests folder should be the same as your project

e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py

e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py

All your tests should be executed by using this command: python3 -m unittest discover tests

You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py

All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__
import__("my_module").MyClass.my_function.__doc__)')
