import json

file_path = '/drone/src/myfile.json'

with open(file_path, 'r') as f:
    data = json.load(f)