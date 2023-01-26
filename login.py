#!/usr/bin/env python3

import os
import cgi
import cgitb
from http.cookies import SimpleCookie

import secret
from templates import login_page, secret_page, after_login_incorrect
cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')

form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
  cookie_username = cookie.get("username").value
if cookie.get("password"):
  cookie_password = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

print("Content-Type: text/html")
if form_ok:
  print(f"Set-Cookie: username={username};")
  print(f"Set-Cookie: password={password};")
print()

if username and not password:
  print(login_page())
elif cookie_ok:
  print(secret_page(cookie_username, cookie_password))
elif username == secret.username and password == secret.password:
  print(secret_page(username, password))
else:
  print(login_page())
  print("username and password: ", username, password)