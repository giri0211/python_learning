# Python fundamentals

## Create virtual environment

to avoid conflicts between differetn application dependeing in different versions of the packAges or libraries, create virtual environment specific to each project. this vistual environment helps in seperating the installable dependies by project.

1. The below command is used to crate a virtual environment in the python project. This creates a folder with name **venv** in the project directory.

    ```pshell
    python -m venv venv
    ```

1. Activate the virtual environment by executing the activate command

    ```pshell
    # on windows machine activate the virtual environment in the project with running the activate script.
    ./venv/scripts/activate
    ```

1. install the required packages through pip.

    for *example*: install the *requests* package with below command

    ```pshell
    pip3 install requests
    ```

1. Execute the required programs and make sure all the packages are installed in the virtual environment.

1. Deactivate the virtual environment, when its not needed anymore.

    ```pshell
    rm ./venv
    # say Yes for the following option to deleted the virtual environment.
    ```

