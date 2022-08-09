import json

file_path = 'myfile.json'

with open(file_path, 'r') as f:
    data = json.load(f)