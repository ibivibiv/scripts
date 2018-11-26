#!/bin/bash
apt-get install -y python
apt-get install -y python-pip
apt-get install -y wget
mkdir conductor
cd conductor
wget https://raw.githubusercontent.com/ibivibiv/scripts/master/conductor/__init__.py
wget https://raw.githubusercontent.com/ibivibiv/scripts/master/conductor/conductor.py
cd ..
wget https://raw.githubusercontent.com/ibivibiv/scripts/master/brutal_worker.py
wget https://raw.githubusercontent.com/ibivibiv/scripts/master/brutal_workflow.py
