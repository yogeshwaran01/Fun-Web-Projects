#!/usr/bin/bash

mode=$1

export FLASK_APP="app"
export SECRET_KEY="somesecretkeyfordev"

if [[ $mode == "debug" ]]; then
    export FLASK_ENV="development"
    export SQLALCHEMY_DATABASE_URL="sqlite:///"$(pwd)"/users.db"
    flask run

elif [[ $mode == "test" ]]; then
    echo "Running tests ..."
    export FLASK_ENV="test"
    pytest -v

elif [[ $mode == "testlint" ]]; then
    echo "Running flake8 tests ..."
    flake8 -v

else
    echo "Please provide the mode to run" 
fi
