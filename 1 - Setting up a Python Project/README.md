# 1. Setting up a Python Project
In this seminar, we will cover the basics of setting up a Python project.

In the `solution` directory, you will find the final project structure that we will create in this seminar.

### Installing Python
To get started with Python, you will need to install it on your computer. 
We'll write this tutorial assuming you're running a Windows machine, but the steps are similar for Mac and Linux.

1. Install `uv` from Astral: it is an open-source Python package and project manager. We'll use it to install different versions of Python and manage our project dependencies.
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
You may want to add the autocompletion feature to your shell. To do so, check the official documentation [here](https://docs.astral.sh/uv/getting-started/installation/).
2. Install Python 3.13 using `uv`:
```shell
uv python install 3.13
```
Try running `python --version` to check if the installation was successful.
You may also want to try running some statement in the Python REPL to check if everything is working as expected.
Start the Python REPL by running:
```shell
python
```
Then, type `print("Hello, World!")` and press Enter. You should see the output `Hello, World!`.

### Setting up a project
Before setting up the project, you may want to check out uv's features on the [official documentation](https://docs.astral.sh/uv/getting-started/features/).

Now that you have Python installed, let's set up a new project.
Create a new directory for your project and navigate to it:
```shell
uv init
```
You will see three new files in your project directory:
- `pyproject.toml`: a file that contains the project's metadata and dependencies.
- `hello.py`: a Python script that will be the entry point of your project.
- `.python-version`: a file that contains the Python version used in the project.
Open the `pyproject.toml` file and check the content. You will find the full specification of the file [in the Python packaging guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
But that's not important for now. You can leave the file as it is.

### Creating the project structure
For a general Python project, you will need to create a few directories to organize your code.
