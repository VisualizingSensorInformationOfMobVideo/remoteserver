# Simple server for fetching XML-data
This is a very simple implementation for a server listening for XML-data from a remote client. It will store the data as files in the ```output```-directory.

## Running
Simple run the python script:
```python server.py 8080``` (specifying port is optional, 8080 is default)

## Sending requests
The requests have to specify a ```Content-Type``` of ```text/xml``` and send the correct ```Content-Length```. There is no checking on URL-part, all requests will be handled.

Testing with curl:
```curl -H "Content-Type:text/xml" -d "data being sent, should be xml" http://localhost:8080```
