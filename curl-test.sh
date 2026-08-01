#!/bin/bash

# GET requests
curl --request GET http://localhost:5000/api/timeline_post 
{"timeline_posts":[]}

curl http://localhost:5000/api/timeline_post 
{"timeline_posts":[]}

# POST requests
curl --request POST http://localhost:5000/api/timeline_post -d 
'name=Wei&email=wei.he@mlh.io&content=Just Added Database to my portfolio site!'
{"content": "Just Added Database to my portfolio site!", "created_at": "Mon, 02 May 
2022 06:14:30 GMT", "email": "wei.he@mlh.io", "id":3, "name": "Wei"}

curl -X POST http://localhost:5000/api/timeline_post -d 
'name=Wei&email=wei.he@mlh.io&content=Just Added Database to my portfolio site!'
{"content": "Just Added Database to my portfolio site!", "created_at": "Mon, 02 May 
2022 06:14:30 GMT", "email": "wei.he@mlh.io", "id":3, "name": "Wei"}

curl http://localhost:5000/api/timeline_post 
{"timeline_posts":[{"content": "Testing my endpoints with postman and 
curl.", "created_at": "Mon, 02 May 2022 06:15:08 
GMT", "email": "wei.he@mlh.io", "id":4, "name": "Wei"},{"content":"Just Added Database 
to my portfolio site!", "created_at": "Mon, 02 May 2022 06:14:31 
GMT", "email": "wei.he@mlh.io", "id":3, "name": "Wei"}]}