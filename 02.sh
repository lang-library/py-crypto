#! /usr/bin/env bash
set -uvx
set -e
cp -rp ~/.pypirc $USERPROFILE/
./py64.cmd -m pip install twine
./py64.cmd -m twine upload dist/*
