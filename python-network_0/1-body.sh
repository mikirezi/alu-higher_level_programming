#!/bin/bash
# Displays body of response only if status code is 200
response=$(curl -s -w "%{http_code}" "$1"); http_code=${response: -3}; body=${response%???}; [ "$http_code" = "200" ] && echo -n "$body"
