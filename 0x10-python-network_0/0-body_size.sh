#!/bin/bash
# Sends a request to a URL and displays the response body size
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
