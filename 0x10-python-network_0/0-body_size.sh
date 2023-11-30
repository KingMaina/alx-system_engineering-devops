#!/bin/bash
# Sends a request to a URL given as a paramater and displays the size of the body response
curl -sL "$1" | wc -c
