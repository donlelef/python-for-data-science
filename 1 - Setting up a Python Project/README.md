# 1. Setting up a Python Project
In this seminar, we will cover the basics of setting up a Python project.

In the `solution` directory, you will find the final project structure that we will create in this seminar.

### Installing Python
To get started with Python, you will need to install it on your computer. 

> [!NOTE]  
> We'll write this tutorial assuming you're running a Windows machine, but the steps are similar for Mac and Linux.

1. Install `uv` from Astral: it is an open-source Python package and project manager. We'll use it to install different versions of Python and manage our project dependencies.
    ```shell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    You may want to add the autocompletion feature to your shell. To do so, check the official documentation [here](https://docs.astral.sh/uv/getting-started/installation/).
2. Install Python 3.13 using `uv`:
    ```shell
    uv python install 3.13
    ```
    Try running `uv run python --version` to check if the installation was successful.

In case you get an error, you may need to restart PyCharm or even your laptop. This is necessary to have the environment variables set correctly.

You may also want to try running some statement in the Python REPL to check if everything is working as expected.
Start the Python REPL by running:
```shell
uv run python
```
Then, type `print("Hello, World!")` and press Enter. You should see the output `Hello, World!`.

> [!NOTE]  
> In a Windows system, just typing `python` will default to the system app alias, and will not use the `uv`-managed Python installations.

### Setting up a project
Before setting up the project, you may want to check out uv's features on the [official documentation](https://docs.astral.sh/uv/getting-started/features/).

Then create a new directory called `power-load-pipeline` for your project and navigate to it. Then run:
```shell
uv init
```
You will see three new files in your project directory:
- `pyproject.toml`: a file that contains the project's metadata and dependencies.
- `hello.py`: a Python script that will be the entry point of your project.
- `.python-version`: a file that contains the Python version used in the project.
Open the `pyproject.toml` file and check the content. You will find the full specification of the file [in the Python packaging guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
But that's not important for now. You can leave the file as it is.

### Creating a virtual environment
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.
To create a virtual environment, run the following command:
```shell
uv venv
```
This command will create a new directory called `.venv` in your project directory. 
This directory will contain the Python installation and the packages you install in your project.

### Creating the project structure
For a general Python project, you will need to create a few directories to organize your code.
Usually, for a simple project, you will have the following structure:
```
project-name/
│   .gitignore -> tells Git which files to ignore
│   .python-version -> contains the Python version used in the project
│   pyproject.toml -> contains the project's metadata and dependencies
│   README.md -> a file that contains information about the project and how to run it
│   uv.lock -> a file that contains the dependencies and their versions (NOT TO EDIT BY HAND)
│
├───.venv -> the virtual environment directory (NOT TO COMMIT NOR TO EDIT BY HAND)
│
├───data -> a directory to store data files, not to be traked by Git
│
├───src -> the source code directory
│   │   main.py
│   │   paths.py
│   │
│   ├───package 1
│   │
│   ├───package 2
│   │
│   └───package 3
│
└───test -> the test directory
    ├───e2e
    │
    └───unit
```

### Our first project
Now we'll write some code and run some tests in our new project.
If you ever get lost, you can always check the `solution` directory for the final project structure.