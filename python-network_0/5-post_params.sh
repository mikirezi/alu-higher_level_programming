#!/bin/bash
# Sends a POST request with email and subject params, displays the body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
