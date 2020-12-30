# Send POST Requests in Python
simple python code to send http POST requests to an API endpoint.

## How it works:
Upon calling __python3 main.py__:
1. constructs a dictionary for the data payload.
1. converts dictionary into a JSON object[1].
1. sends the payload to the specified API via POST request, using the python requests package[2].
1. prints out the result of the POST request. 

## Futher readings:
[[1] Python JSON encoder and decoder documentation](https://docs.python.org/3/library/json.html)

[[2] Python Requests - Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request)