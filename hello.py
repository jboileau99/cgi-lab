#!/usr/bin/env python3
import os
import json

print("Content-Type: application/json")
print()
env = json.dumps(dict(os.environ))
print(env)

# print("Content-Type: text/html")
# print()
# print(os.environ["HTTP_USER_AGENT"])
# print(os.environ["QUERY_STRING"])
