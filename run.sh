#!/bin/bash
echo "1 - install environment, 2 - flask run, 3 - run tests, 4 for quit: "
read CONFIRMATION

# install env
if [ $CONFIRMATION == '1' ]; then
    python3 -m venv env
    source env/bin/activate

    python3 setup.py install

# run flask app
elif [ $CONFIRMATION == '2' ]; then
    source env/bin/activate

    cd src
    python3 app.py

# run tests
elif [ $CONFIRMATION == '3' ]; then
    source env/bin/activate

    # run tests
    pytest -v

# exit
elif [ $CONFIRMATION == '4' ]; then
    echo "Code more next time."
fi
