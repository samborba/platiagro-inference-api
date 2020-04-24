# PlatIAgro API for Model Inference
Integration between Dojot and Platiagro. Apply models over the data coming from the IoT platform (Dojot).

## Algorithms
Isolation Forest & Logistic Regression modules [scikit-learn](https://scikit-learn.org/) library;

## Dataset
Data generated from emulated IoT devices. Check [mqtt-emulator](https://github.com/dojot/mqtt-emulator) from Dojot repository for more details;

## How to Use
1. Download and install Python version 3.7+ and the Pip package manager. Follow the instructions (according to your operating system) on the [official website](https://www.python.org/downloads/) of the distributor.
2. Create a Python [virtual environment](https://virtualenv.pypa.io/en/stable/) for the project using Virtualenv. This will cause project dependencies to be isolated from your Operating System. Once you create the python environment, enable it before proceeding to the next steps. Ex: You should see ``(env)your-user-name:$`` in the terminal.
3. Run ``$ pip install -r requirements.txt`` to install dependencies.
4. Run ``(env)$ python src/app.py``. The application port is set to 3003 as the default, however, you can choose another port by changing the properties in the [config.py](../master/src/api/config.py) file.

## Notes
1. [Dojot](https://github.com/dojot) GitHub;
2. [PlatIAgro](https://github.com/platiagro/) GitHub;
3. [PlatIAoT](https://github.com/samborba/PlatIAoT) GitHub;
