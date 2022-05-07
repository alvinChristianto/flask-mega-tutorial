# Flask Mega Tutorial 

Here I'm following tutorial on how to build web application using flask framework. The **[tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)** created by Miguel Grinberg, it has 23 chapters to build complete flask framework. Flask is a micro web framework written in Python.  The “micro” means Flask aims to keep the core simple but extensible. 

---

## 🧱 Installation 

### python

flask recommend using the latest version of Python. Flask supports Python 3.7 and newer, although older versions still support older version of python. 

to check your python version
```bash
python -V
```

### Virtual Environments

Use virtual environment to manage dependencies between you projects. Here I  use pyenv to manage multiple versions of python and pipenv to manage packages. Pyenv will create .python-version file that contains python version that I used in this project. Pipenv will create Pipfile dan Pipfile.lock that contains all packages to run this project. For more info about pyenv and pipenv, [check this](https://www.rootstrap.com/blog/how-to-manage-your-python-projects-with-pipenv-pyenv/)

## 📁 Cloning Repo 
You can start cloning this repo
```bash
git clone https://github.com/alvinChristianto/flask-mega-tutorial
```
After clone successfully, inside the folder you will see :
1. .python-version that contain information about my python version to this project. Its not necessary to use the exact same version. 
2. Pipfile, this file is a reference what packages need to install in order to run this project. Pipfile then generate Pipfile.lock which is used to produce [deterministic builds](https://pipenv.pypa.io/en/latest/)

## 🧱 Setting Virtual Environment(pyenv and pipenv) 

Once you install pyenv and pipenv, it`s time to setting the environment.

### Setting pyenv 
To install the same python version (I use 3.7.2) :
```bash
pyenv install 3.7.2
```
To check your python version in your computer
```bash
pyenv versions
```

To check your python version inside a cloned folder 
```bash
pyenv version
```

To set python 3.7.2 only on your cloned folder  : 
```bash
pyenv local 3.7.2
```

### Setting pipenv

To install the packages lists in Pipfile you need to create and enter virtual environment with this command: 
```bash
pipenv shell
```
you will automatically enter the virtual environment.
To install all packages inside Pipfile :
```bash
pipenv install
```
To run the project
```bash
flask run
```



## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## 🎫 License
[MIT](https://choosealicense.com/licenses/mit/)