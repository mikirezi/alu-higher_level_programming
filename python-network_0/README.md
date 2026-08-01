# python-network_0

This project covers the basics of networking with Python and Bash, focusing on using `curl` to interact with HTTP servers: sending requests, reading response bodies, checking status codes, setting custom headers, and sending different HTTP methods (GET, POST, DELETE, OPTIONS).

## Tasks

### 0. cURL body size
`0-body_size.sh` takes a URL, sends a request to it, and displays the size of the response body in bytes.

### 1. cURL to the end
`1-body.sh` takes a URL, sends a GET request, and displays the response body only if the status code is 200.

### 2. cURL Method
`2-delete.sh` sends a DELETE request to a URL and displays the response body.

### 3. cURL only methods
`3-methods.sh` takes a URL and displays all HTTP methods the server accepts.

### 4. cURL headers
`4-header.sh` takes a URL, sends a GET request with the header `X-HolbertonSchool-User-Id: 98`, and displays the response body.

### 5. cURL POST parameters
`5-post_params.sh` takes a URL, sends a POST request with `email=test@gmail.com` and `subject=I will always be here for PLD`, and displays the response body.

## Usage

./0-body_size.sh <url>
./1-body.sh <url>
./2-delete.sh <url>
./3-methods.sh <url>
./4-header.sh <url>
./5-post_params.sh <url>

## Author
Guillaume
