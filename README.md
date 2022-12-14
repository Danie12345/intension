# intension - v0.1.0
A procedural pattern-generating template library for tensor-like objects using the Wave Function Collapse method in Python.

> Leave a star if you like this project! :)


---

## Prerequisites
Have Python 3.10.5+ installed in your system.
Have git installed in your system.

## Clone repo
Clone the repo using this command `git clone https://github.com/Danie12345/intension.git`

## Try it
Navigate to the repo directory on a new terminal.

To create the virtual environment run: `python -m venv .\venv`. Then run: `.\venv\scripts\activate` to activate the virtual environment. (To deactivate run: `deactivate`.)

To install dependencies from requirements.txt run: `python -m pip install -r requirements.txt`

To add a dependency run: `python -m pip install DEPENDENCY`

To update requirements.txt run: `python -m pip freeze > requirements.txt`

> For more help see the [docs](https://docs.python.org/3/installing/index.html) on virtual environments and how to install from requirements [here](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from).

## Testing
To run all tests run: `pytest tests/ --verbose`

## Linters
To use pylint run: `pylint intension`

To fix errors with autopep8 run: `autopep8 -i -a -a intension/filepath`

## Building
To build the library run: `python setup.py bdist_wheel`

---

## Author
### [Daniel Malo](https://github.com/Danie12345)

---

### License
Licensed under [GPL v3](LICENSE)