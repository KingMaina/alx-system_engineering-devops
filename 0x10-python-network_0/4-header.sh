#!/bin/bash
# Sends a GET request with a header variable and displays the body
curl -sX GET "$1" -H "X-School-User-Id: 98" -L
