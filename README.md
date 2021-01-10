# Set up the environment

You are suggested to use a Python Virtual Environment to run this program.
Python Virtual Environment is a quarantine environment on your machine to separate different required dependencies for different projects.
To set up a Python Virtual Environment on you machine, you can follow the procedures below.

## Setup the pip package manager
Check to see if your Python installation has pip. Enter the following in your terminal: 

```$ pip -h```

If you see the help text for pip then you have pip installed, otherwise download and install pip

## Install the virtualenv package
The virtualenv package is required to create virtual environments. You can install it with pip:

```$ pip install virtualenv```

## Create the virtual environment
To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:

virtualenv mypython

## Activate the virtual environment
You can activate the python environment by running the following command:

Mac OS / Linux

```$ source mypython/bin/activate```

Windows

```> mypthon\Scripts\activate```

You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).

Any python commands you use will now work with your virtual environment

## Deactivate the virtual environment
To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’.

```$ deactivate```

## Install dependencies
The **requirements.txt** file stores all the dependencies packages and the associated version.

To install all the dependencies packages specified in the requirements.txt, you can execute the following command.

```$ pip install -r requirements.txt```