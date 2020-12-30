#!/usr/bin/env python3

import requests
import json

URL = 'https://contact.plaid.com/jobs' #the URL defines the API endpoint.

post_fields = {"name": "William Loo",
  "email": "williamloo@berkeley.edu",
  "resume": "linkedin.com/in/williamlooo",
  "phone": "",
  "job_id": "58690464-4e63-4180-8dc7-a1e87a18fb6d",
  "github": "github.com/williamlooo", 
  "website": "williamlooo.github.io", 
  "location": "San Francisco",
  "favorite_candy": "m&ms",
  "superpower": "i can look at food and know exactly how long to microwave it for"
}

payload = json.dumps(post_fields)

response = requests.post(URL, data = payload)
print(response.text)