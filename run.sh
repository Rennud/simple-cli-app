#!/bin/bash
echo "1 - flask run, 2 - run tests, 3 for quit: "
read CONFIRMATION

VENV="Virtual environmet activated"

# run flask app
if [ $CONFIRMATION == '1' ]; then
    # activate venv
    cd env/bin
    source activate
    echo $VENV

    cd ../../
    cd src
    python3 app.py

    # return to root dir and deactivate venv
    cd ../../../
    deactivate

# run tests
elif [ $CONFIRMATION == '2' ]; then
    # activate venv
    cd env/bin
    source activate
    echo $VENV

    # run tests
    cd ../../
    pytest -v

    deactivate

# exit
elif [ $CONFIRMATION == '3' ]; then
    echo "Code more next time."
fi
