#!/usr/bin/env bash
# Displays all HTTP methods the server will accept for a given URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
