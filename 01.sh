#! /usr/bin/env bash
set -uvx
set -e
./py64.cmd -m pip install wheel setuptools
rm -rf dist
./py64.cmd setup.py bdist_wheel
