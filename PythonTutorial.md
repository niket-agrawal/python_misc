# Lesson 1 - Using Virtual Environment Module in Python

[venv](https://docs.python.org/3/library/venv.html) is an inbuilt Python module to deal with virtual environments during product development.

## Installation

In-built module with Python 3.3 onward. To check, type `python -m venv` in command line. If following appears, then go ahead with using it.

```bash
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
```

## Usage

Using `venv` module usually consists of 5 steps - Creation, Activation, Actual Use, Deactivation and Deletion. I've summarized each step with its basic commands.

### Step 0 - Recommendations

> Before playing with virtual environments, it is highly recommended to make a separate directory to store all your new environments.

There are 2 ways to do this.

```bash
Way 1 - for Environment Oriented Coding
      - Create a "New Folder" e.g. "Niks_virtual_envs"
      - cd inside this folder, and proceed with *Step1* to create new environments here.
      - Renaming new environment according to your project e.g. "env_proj1" is recommended.

Way 2 - for Project Oriented Coding
      - Create a "New Folder" e.g. "Niks_projects"
      - Again, create "New Folder" inside this project folder and name it for e.g. "Project1"
      - Now, cd inside this "Project1" folder, and proceed with *Step1* to create new environment here.
      - Renaming new environment "venv" is recommended.

```

### Step 1 - Create New Environment

General usage: `python -m venv new_venv`

If you followed Way 1 - 
```bash
niks@home > mkdir Niks_virtual_envs
niks@home > cd Niks_virtual_envs
niks@home\Niks_virtual_envs > python -m venv env_proj1
niks@home\Niks_virtual_envs > dir
```
If you followed Way 2 - 
```bash
niks@home > mkdir Niks_projects
niks@home > cd Niks_projects
niks@home\Niks_projects > mkdir Project1
niks@home\Niks_projects > python -m venv Project1\venv
niks@home\Niks_projects > dir Project1
```

### Step 2 - Activate your Environment

Navigate to directory containing your environment and type: `new_venv\Scripts\activate.bat`

for e.g. if you followed Way1 - 
```bash
niks@home\Niks_virtual_envs > env_proj1\Scripts\activate.bat
(env_proj1) niks@home\Niks_virtual_envs >
```
or if you followed Way2 - 
```bash
niks@home\Niks_projects > cd Project1
niks@home\Niks_projects\Project1 > venv\Scripts\activate.bat
(venv) niks@home\Niks_projects\Project1 >
```

### Step 3 - Actual Use

Haha are you kidding, do `pip list` and `where python` and go ahead. Make something awesome.

To save your environment dependencies for distribution in the form of `requirements.txt`, use this command.
```bash
(venv) niks@home\Niks_projects\Project1 > pip freeze > requirements.txt
```

### Step 4 - Deactivate your Environment

Deactivating your virtual environment is fairly simple, just write `deactivate` 

```bash
(venv) niks@home\Niks_projects\Project1 > deactivate
niks@home\Niks_projects\Project1 >
```

### Step 5 - Delete your Environment

Deleting the environment is as simple as deleting your environment directory. Just go to respective directory, if you did started with **Way 1** - write `rmdir env_proj1`, or for **Way 2** - write `rmdir venv`. 

```bash
niks@home\Niks_projects\Project1 > rmdir venv /s
Are you sure (Y/N)? y
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
