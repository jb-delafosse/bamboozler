#!/bin/bash
virtualenv /tmp/bamboo_env
source /tmp/bamboo_env/bin/activate
pip install -t lib -r requirements.txt
python $APPENGINE/dev_appserver.py app.yaml
