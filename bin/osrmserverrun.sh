#!/bin/bash

source .env
docker pull mpwilbur/smarttransit-osrm-server:$OSRM_TAG
docker run --name osrm-server -m=12g -p $OSRM_PORT:5000 -d --restart unless-stopped mpwilbur/smarttransit-osrm-server:$OSRM_TAG
#docker run --name osrm-server -m=12g -p $OSRM_PORT:5000 -d --restart unless-stopped mpwilbur/smarttransit-osrm-server:tennessee-extended-prod-amd64