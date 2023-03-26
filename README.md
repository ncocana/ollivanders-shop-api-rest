# Ollivanders Shop — REST API

**Table of contents**

-   [**Introduction**](#introduction)
-   [**How to install**](#how-to-install)
-   [**How to use**](#how-to-use)
-   [**Testing and development**](#testing-and-development)
-   [**Docker**](#docker)

## Introduction

Ollivanders Shop is a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) that allows you to make [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations (such as get, update, create, or delete data from a database) using the website created for it. This website will allow you to see the content of the database and choose if you want to update it, insert new data, or delete an already existing one, by just hitting a button (and if neccessary, write the data asked to do such operations).   

I will leave the [link to the project](https://github.com/dfleta/flask-rest-ci-boilerplate) statement to those curious about the instructions we were given.   

## How to install

The first thing you need to know is that you don't to install or create an account for any database, as Ollivanders uses an [SQLite database](https://docs.python.org/3/library/sqlite3.html). SQLite, or more precisely ```sqlite3```, is a module in Python's standard library that provides a simple and efficient way to interact with SQLite databases from within Python programs. This means that you only will need to execute one command to create your local database.   

Let's start the tutorial:

1. First, create a directory/folder in which you will store the application. If you doing this with the terminal, you will need to use this commands:

```
mkdir .\ollivanders
cd ollivanders
```

2. Clone the repository inside that directory.

```
git clone https://github.com/ncocana/ollivanders-shop-api-rest.git
```

3. Create a virtual environment and move inside it. This is an important step because it allows you to create an isolated environment for this project, with its own set of dependencies, without interfering with other Python projects or the system Python installation.

```
python -m venv venv
```

4. Move inside the virtual environment. Depending on what terminal you're on, you will need to execute the required file. For Windows Powershell, it will be the one with extension ".ps1"; for the CMD, it will be ".bat"; and for Unix or MacOS, it will be called "activate". In this case, I will use the Powershell one:

```
.\venv\Scripts\Activate.ps1
```

It's possible that when executing this command, you get an error along the lines of "cannot be loaded because the execution of scripts is disabled on this system". If this happens, you will need to open Windows Powershell as administrator and execute the following command. When asked if you're sure, say "yes". This will allow you to execute scripts on your PC, such as the one you need to activate the virtual environment.

```
Set-executionpolicy remotesigned
```

5. Install the requirements. There are two type of requirements: ```requirements.txt``` for the requirements needed for the project to function properly, and ```dev-requirements.txt``` for the requirements needed to testing and development. For now, we will install just ```requirements.txt```.

```
pip install -r requirements.txt
```

## How to use



## Testing and development



## Docker

