#!/bin/bash
# Displays all the HTTP methods a server will accept
curl -sLX OPTIONS "$1" | grep Allow | cut -d " " -f2-
