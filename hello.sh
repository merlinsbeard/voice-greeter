#!/bin/bash

cd "$(dirname "$0")"
pwd
echo "Starting daily run"
venv/bin/python hello.py -c life bj manila
cd Sounds/
mpc stop
mpg123 *.mp3
rm *.mp3
mpc play

# TODO: send mail
