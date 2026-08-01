# python-network_1

This project covers using Python's `urllib` and `requests` modules to interact with web servers: making GET and POST requests, reading response headers and bodies, handling HTTP errors, working with JSON responses, and using Basic Authentication with the GitHub API.

## Tasks

### 0. What's my status? #0
`0-hbtn_status.py` fetches `https://intranet.hbtn.io/status` using `urllib` and displays the response body type, content, and UTF-8 decoded content.

### 1. Response header value #0
`1-hbtn_header.py` takes a URL, sends a request using `urllib`, and displays the value of the `X-Request-Id` header.

### 2. POST an email #0
`2-post_email.py` takes a URL and an email, sends a POST request using `urllib` with the email as a parameter, and displays the response body.

### 3. Error code #0
`3-error_code.py` takes a URL, sends a request using `urllib`, and displays the response body or the HTTP error code if an `HTTPError` occurs.

### 4. What's my status? #1
`4-hbtn_status.py` fetches `https://alu-intranet.hbtn.io/status` using `requests` and displays the response type and content.

### 5. Response header value #1
`5-hbtn_header.py` takes a URL, sends a request using `requests`, and displays the value of the `X-Request-Id` header.

### 6. POST an email #1
`6-post_email.py` takes a URL and an email, sends a POST request using `requests` with the email as a parameter, and displays the response body.

### 7. Error code #1
`7-error_code.py` takes a URL, sends a request using `requests`, and displays the response body, or the error code if the status is 400 or above.

### 8. Search API
`8-json_api.py` takes a letter, sends a POST request to `search_user` using `requests`, and displays the matching user's id and name, or an appropriate message if there's no result or invalid JSON.

### 9. My GitHub!
`10-my_github.py` takes a GitHub username and personal access token, and displays the authenticated user's GitHub id using Basic Authentication.

## Author
Guillaume
