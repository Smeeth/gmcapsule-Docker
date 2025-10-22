#!/usr/bin/env python3
import os
import sys

# Titan-Daten lesen
titan_data = sys.stdin.read()

# Gemini-Response Header
print("20 text/gemini\r")

# Content
print("# CGI Test")
print()
print("Client cert hash:", os.getenv('REMOTE_IDENT', 'none'))
print("Titan token:", os.getenv('TITAN_TOKEN', 'none'))
print(f"Uploaded bytes: {len(titan_data)}")
