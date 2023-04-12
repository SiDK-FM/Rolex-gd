#!/bin/bash

# Install dependencies
pip install --trusted-host pypi.python.org -r requirements.txt

# Start the WebStreamer
python3 -m WebStreamer
