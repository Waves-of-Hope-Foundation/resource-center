#!/bin/sh

## Usage:
## Set the PROXY_LOCATION and INSTANCE_CONNECTION_NAME
## environment variables
## Run `$ ./encrypt_secret.sh`

# Run cloud sql proxy
$PROXY_LOCATION/cloud_sql_proxy -instances=$INSTANCE_CONNECTION_NAME=tcp:3306
