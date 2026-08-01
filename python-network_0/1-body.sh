#!/usr/bin/env bash
# Sends a GET request and displays the body only if the response is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')
if [ "$status_code" -eq 200 ]; then
    echo "$body"
fi
